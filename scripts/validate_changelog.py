#!/usr/bin/env python3
"""Valida os registros estruturados do changelog sem dependências externas."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any


CHANGE_ID_RE = re.compile(r"^CHG-(\d{4})-(\d{3})$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
REQUIRED_FIELDS = {
    "change_id",
    "date",
    "version_from",
    "version_to",
    "responsible",
    "components",
    "reason",
    "evidence",
    "changes",
    "expected_behavior",
    "known_risks",
    "compatibility",
    "evaluation",
    "approval",
    "rollback",
    "version_control",
    "publication",
}
METRICS = ("quality", "security", "latency", "cost")


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_iso_date(value: Any) -> bool:
    if not _non_empty_string(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _validate_iso_datetime(value: Any) -> bool:
    if not _non_empty_string(value):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def validate_record(record: Any, path: Path, release: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return [f"{path}: a raiz deve ser um objeto JSON"]

    missing = sorted(REQUIRED_FIELDS - record.keys())
    if missing:
        errors.append(f"{path}: campos obrigatórios ausentes: {', '.join(missing)}")
        return errors

    change_id = record["change_id"]
    if not _non_empty_string(change_id) or not CHANGE_ID_RE.fullmatch(change_id):
        errors.append(f"{path}: change_id inválido")
    elif path.stem != change_id:
        errors.append(f"{path}: nome do arquivo deve ser {change_id}.json")

    if not _validate_iso_date(record["date"]):
        errors.append(f"{path}: date deve usar AAAA-MM-DD")
    if not _non_empty_string(record["version_from"]):
        errors.append(f"{path}: version_from não pode ser vazio")
    if not _non_empty_string(record["version_to"]) or not SEMVER_RE.fullmatch(record["version_to"]):
        errors.append(f"{path}: version_to deve seguir SemVer")

    for field in ("responsible", "components", "changes", "expected_behavior"):
        value = record[field]
        if not isinstance(value, list) or not value or not all(_non_empty_string(item) for item in value):
            errors.append(f"{path}: {field} deve ser uma lista não vazia de textos")

    if not _non_empty_string(record["reason"]):
        errors.append(f"{path}: reason não pode ser vazio")
    if not isinstance(record["known_risks"], list):
        errors.append(f"{path}: known_risks deve ser uma lista")

    evidence = record["evidence"]
    if not isinstance(evidence, list):
        errors.append(f"{path}: evidence deve ser uma lista")
    else:
        for index, item in enumerate(evidence):
            if not isinstance(item, dict) or not all(
                _non_empty_string(item.get(field))
                for field in ("type", "reference", "description")
            ):
                errors.append(f"{path}: evidence[{index}] está incompleta")

    compatibility = record["compatibility"]
    if not isinstance(compatibility, dict):
        errors.append(f"{path}: compatibility deve ser um objeto")
    else:
        if not isinstance(compatibility.get("breaking_changes"), list):
            errors.append(f"{path}: compatibility.breaking_changes deve ser uma lista")
        if not isinstance(compatibility.get("migration_required"), bool):
            errors.append(f"{path}: compatibility.migration_required deve ser booleano")

    evaluation = record["evaluation"]
    if not isinstance(evaluation, dict):
        errors.append(f"{path}: evaluation deve ser um objeto")
    else:
        for metric_name in METRICS:
            metric = evaluation.get(metric_name)
            if not isinstance(metric, dict):
                errors.append(f"{path}: evaluation.{metric_name} deve ser um objeto")
                continue
            if metric.get("status") not in {"measured", "pending", "not_applicable"}:
                errors.append(f"{path}: status inválido em evaluation.{metric_name}")
            if release and metric.get("status") == "pending":
                errors.append(f"{path}: release bloqueada por métrica pendente: {metric_name}")
            if release and metric.get("status") == "measured" and not metric.get("evidence"):
                errors.append(f"{path}: métrica {metric_name} não possui evidência")

        regressions = evaluation.get("regressions")
        if not isinstance(regressions, dict):
            errors.append(f"{path}: evaluation.regressions deve ser um objeto")
        elif regressions.get("status") not in {"passed", "failed", "pending", "not_applicable"}:
            errors.append(f"{path}: status inválido em evaluation.regressions")
        elif release and regressions.get("status") not in {"passed", "not_applicable"}:
            errors.append(f"{path}: release bloqueada pela avaliação de regressões")

    approval = record["approval"]
    if not isinstance(approval, dict) or approval.get("status") not in {"pending", "approved", "rejected"}:
        errors.append(f"{path}: approval inválida")
    elif approval["status"] == "approved":
        if not _non_empty_string(approval.get("approved_by")):
            errors.append(f"{path}: aprovação não identifica o aprovador")
        if not _validate_iso_datetime(approval.get("approved_at")):
            errors.append(f"{path}: aprovação não possui data/hora ISO válida")
        if not _non_empty_string(approval.get("evidence")):
            errors.append(f"{path}: aprovação não possui evidência")
    elif release:
        errors.append(f"{path}: release bloqueada: mudança não aprovada")

    rollback = record["rollback"]
    if not isinstance(rollback, dict):
        errors.append(f"{path}: rollback deve ser um objeto")
    else:
        procedure = rollback.get("procedure")
        if not isinstance(procedure, list) or not procedure:
            errors.append(f"{path}: rollback.procedure deve ter ao menos uma etapa")
        if rollback.get("validation_status") not in {"not_tested", "passed", "failed", "not_applicable"}:
            errors.append(f"{path}: rollback.validation_status inválido")
        if release and rollback.get("validation_status") not in {"passed", "not_applicable"}:
            errors.append(f"{path}: release bloqueada: rollback não validado")

    version_control = record["version_control"]
    if not isinstance(version_control, dict):
        errors.append(f"{path}: version_control deve ser um objeto")
    elif release and (
        not _non_empty_string(version_control.get("commit"))
        or not _non_empty_string(version_control.get("tag"))
    ):
        errors.append(f"{path}: release bloqueada: commit e tag não registrados")

    publication = record["publication"]
    if not isinstance(publication, dict) or publication.get("status") not in {
        "not_released", "released", "rolled_back"
    }:
        errors.append(f"{path}: publication inválida")

    return errors


def validate_repository(root: Path, release: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    changes_dir = root / "changes"
    paths = sorted(changes_dir.glob("CHG-*.json"))
    if not paths:
        return [f"{changes_dir}: nenhum registro de mudança encontrado"], warnings

    records: list[tuple[Path, dict[str, Any]]] = []
    identifiers: set[str] = set()
    versions: set[str] = set()
    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: JSON inválido: {exc}")
            continue
        errors.extend(validate_record(record, path, release=release))
        if isinstance(record, dict):
            for item in record.get("evidence", []):
                if not isinstance(item, dict) or item.get("type") != "file":
                    continue
                reference = item.get("reference")
                if not _non_empty_string(reference):
                    continue
                evidence_path = (root / reference).resolve()
                try:
                    evidence_path.relative_to(root.resolve())
                except ValueError:
                    errors.append(f"{path}: evidência aponta para fora do repositório: {reference}")
                else:
                    if not evidence_path.is_file():
                        errors.append(f"{path}: arquivo de evidência inexistente: {reference}")

            change_id = record.get("change_id")
            version_to = record.get("version_to")
            if change_id in identifiers:
                errors.append(f"{path}: change_id duplicado: {change_id}")
            if version_to in versions:
                errors.append(f"{path}: version_to duplicada: {version_to}")
            identifiers.add(change_id)
            versions.add(version_to)
            records.append((path, record))

    if records:
        latest_version = records[-1][1].get("version_to")
        version_file = root / "VERSION"
        try:
            declared_version = version_file.read_text(encoding="utf-8").strip()
        except OSError as exc:
            errors.append(f"{version_file}: não foi possível ler: {exc}")
        else:
            if declared_version != latest_version:
                errors.append(
                    f"{version_file}: versão {declared_version!r} difere da última mudança {latest_version!r}"
                )

        changelog_path = root / "CHANGELOG.md"
        try:
            changelog = changelog_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{changelog_path}: não foi possível ler: {exc}")
        else:
            for _, record in records:
                if record.get("change_id") not in changelog:
                    errors.append(f"{changelog_path}: não referencia {record.get('change_id')}")
                if f"[{record.get('version_to')}]" not in changelog:
                    errors.append(f"{changelog_path}: não referencia a versão {record.get('version_to')}")

    if not release:
        for path, record in records:
            if record.get("approval", {}).get("status") == "pending":
                warnings.append(f"{path}: aprovação pendente")
            pending = [
                name for name in METRICS
                if record.get("evaluation", {}).get(name, {}).get("status") == "pending"
            ]
            if pending:
                warnings.append(f"{path}: métricas pendentes: {', '.join(pending)}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--release",
        action="store_true",
        help="Aplica os gates obrigatórios para publicação de uma versão.",
    )
    args = parser.parse_args()

    errors, warnings = validate_repository(args.root.resolve(), release=args.release)
    for warning in warnings:
        print(f"[AVISO] {warning}")
    for error in errors:
        print(f"[ERRO] {error}", file=sys.stderr)
    if errors:
        print(f"Changelog inválido: {len(errors)} erro(s).", file=sys.stderr)
        return 1
    print("Changelog válido." if not args.release else "Changelog apto para release.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
