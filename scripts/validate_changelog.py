#!/usr/bin/env python3
"""Valida os registros estruturados do changelog sem dependências externas."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any


CHANGE_ID_RE = re.compile(r"^CHG-(\d{4})-(\d{3})$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
PUBLICATION_ID_RE = re.compile(r"^PUB-(\d{4})-(\d{3})$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
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
    else:
        if version_control.get("commit") is not None:
            errors.append(
                f"{path}: version_control.commit deve ser nulo; "
                "o commit é registrado após a publicação"
            )
        tag = version_control.get("tag")
        expected_tag = f"v{record['version_to']}"
        if tag is not None and tag != expected_tag:
            errors.append(
                f"{path}: version_control.tag {tag!r} difere da versão esperada {expected_tag!r}"
            )

    publication = record["publication"]
    if not isinstance(publication, dict):
        errors.append(f"{path}: publication inválida")
    elif publication.get("status") != "not_released" or publication.get("published_at") is not None:
        errors.append(
            f"{path}: publicação não pode ser declarada antecipadamente no registro da mudança; "
            "use um registro PUB posterior"
        )

    return errors


def validate_publication(record: Any, path: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return [f"{path}: a raiz deve ser um objeto JSON"]

    required = {
        "publication_id", "change_id", "version", "commit", "tag",
        "release_url", "status", "tag_immutable", "ci",
    }
    missing = sorted(required - record.keys())
    if missing:
        return [f"{path}: campos obrigatórios ausentes: {', '.join(missing)}"]

    publication_id = record.get("publication_id")
    if not _non_empty_string(publication_id) or not PUBLICATION_ID_RE.fullmatch(publication_id):
        errors.append(f"{path}: publication_id inválido")
    elif path.stem != publication_id:
        errors.append(f"{path}: nome do arquivo deve ser {publication_id}.json")

    if not _non_empty_string(record.get("change_id")) or not CHANGE_ID_RE.fullmatch(record["change_id"]):
        errors.append(f"{path}: change_id inválido")
    if not _non_empty_string(record.get("version")) or not SEMVER_RE.fullmatch(record["version"]):
        errors.append(f"{path}: version deve seguir SemVer")
    if not _non_empty_string(record.get("commit")) or not COMMIT_RE.fullmatch(record["commit"]):
        errors.append(f"{path}: commit deve ser um SHA-1 Git completo")
    expected_tag = f"v{record.get('version')}"
    if record.get("tag") != expected_tag:
        errors.append(f"{path}: tag {record.get('tag')!r} difere da versão esperada {expected_tag!r}")
    if not _non_empty_string(record.get("release_url")) or not record["release_url"].startswith("https://"):
        errors.append(f"{path}: release_url deve usar HTTPS")
    if record.get("status") not in {"released", "rolled_back"}:
        errors.append(f"{path}: status de publicação inválido")
    if record.get("tag_immutable") is not True:
        errors.append(f"{path}: tag_immutable deve ser true")

    ci = record.get("ci")
    if not isinstance(ci, dict):
        errors.append(f"{path}: ci deve ser um objeto")
    else:
        for field in ("main", "tag"):
            if ci.get(field) not in {"passed", "failed", "not_run"}:
                errors.append(f"{path}: ci.{field} inválido")
        if ci.get("tag") == "failed" and not _non_empty_string(ci.get("failure_category")):
            errors.append(f"{path}: falha de CI da tag deve possuir categoria")
        if ci.get("tag") == "failed" and not _non_empty_string(ci.get("run_url")):
            errors.append(f"{path}: falha de CI da tag deve possuir URL da execução")

    return errors


def validate_tag_context(
    root: Path,
    ref_name: str | None,
    github_sha: str | None,
    head_sha: str | None = None,
) -> list[str]:
    errors: list[str] = []
    version_path = root / "VERSION"
    try:
        version = version_path.read_text(encoding="utf-8").strip()
    except OSError as exc:
        return [f"{version_path}: não foi possível ler: {exc}"]

    expected_tag = f"v{version}"
    if ref_name != expected_tag:
        errors.append(f"tag do evento {ref_name!r} difere da versão esperada {expected_tag!r}")

    if not _non_empty_string(github_sha) or not COMMIT_RE.fullmatch(github_sha):
        errors.append("GITHUB_SHA deve ser um SHA-1 Git completo")
        return errors

    if head_sha is None:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError) as exc:
            errors.append(f"não foi possível resolver o commit da tag: {exc}")
            return errors
        head_sha = result.stdout.strip()

    if head_sha != github_sha:
        errors.append(f"GITHUB_SHA {github_sha!r} difere do commit da tag {head_sha!r}")
    return errors


def validate_baseline_manifests(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_paths = sorted((root / "changes" / "baselines").glob("*.sha256"))
    if not manifest_paths:
        return [f"{root / 'changes' / 'baselines'}: nenhum manifesto de baseline encontrado"]

    for manifest_path in manifest_paths:
        try:
            lines = manifest_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            errors.append(f"{manifest_path}: não foi possível ler: {exc}")
            continue
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            parts = line.split(maxsplit=1)
            if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
                errors.append(f"{manifest_path}:{line_number}: entrada SHA-256 inválida")
                continue
            expected_hash, relative_path = parts
            relative_path = relative_path.lstrip("* ")
            target = (root / relative_path).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{manifest_path}:{line_number}: caminho fora do repositório")
                continue
            try:
                actual_hash = hashlib.sha256(target.read_bytes()).hexdigest()
            except OSError as exc:
                errors.append(f"{manifest_path}:{line_number}: não foi possível ler {relative_path}: {exc}")
                continue
            if actual_hash != expected_hash:
                errors.append(f"{manifest_path}:{line_number}: hash divergente para {relative_path}")
    return errors


def validate_repository(root: Path, release: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    changes_dir = root / "changes"
    paths = sorted(changes_dir.glob("CHG-*.json"))
    if not paths:
        return [f"{changes_dir}: nenhum registro de mudança encontrado"], warnings

    records: list[tuple[Path, dict[str, Any]]] = []
    records_by_id: dict[str, dict[str, Any]] = {}
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
            if _non_empty_string(change_id):
                records_by_id[change_id] = record

    publication_ids: set[str] = set()
    publications_dir = changes_dir / "publications"
    for path in sorted(publications_dir.glob("PUB-*.json")):
        try:
            publication = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: JSON inválido: {exc}")
            continue
        errors.extend(validate_publication(publication, path))
        if not isinstance(publication, dict):
            continue
        publication_id = publication.get("publication_id")
        if publication_id in publication_ids:
            errors.append(f"{path}: publication_id duplicado: {publication_id}")
        publication_ids.add(publication_id)
        referenced_change = records_by_id.get(publication.get("change_id"))
        if referenced_change is None:
            errors.append(f"{path}: mudança referenciada não existe: {publication.get('change_id')}")
        elif publication.get("version") != referenced_change.get("version_to"):
            errors.append(f"{path}: versão da publicação difere da mudança referenciada")

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
    parser.add_argument(
        "--tag-context",
        action="store_true",
        help="Confere a tag do evento e GITHUB_SHA contra VERSION e o HEAD do Git.",
    )
    args = parser.parse_args()

    errors, warnings = validate_repository(args.root.resolve(), release=args.release)
    if args.release:
        errors.extend(validate_baseline_manifests(args.root.resolve()))
    if args.tag_context:
        errors.extend(validate_tag_context(
            args.root.resolve(),
            os.environ.get("GITHUB_REF_NAME"),
            os.environ.get("GITHUB_SHA"),
        ))
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
