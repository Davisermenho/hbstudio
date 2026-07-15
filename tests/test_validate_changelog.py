from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_changelog.py"
SPEC = importlib.util.spec_from_file_location("validate_changelog", MODULE_PATH)
assert SPEC and SPEC.loader
validate_changelog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_changelog)


class ChangelogValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline_path = ROOT / "changes" / "CHG-2026-001.json"
        cls.baseline = json.loads(cls.baseline_path.read_text(encoding="utf-8"))
        cls.publication_path = ROOT / "changes" / "publications" / "PUB-2026-001.json"
        cls.publication = json.loads(cls.publication_path.read_text(encoding="utf-8"))

    def test_branch_validation_accepts_current_repository(self) -> None:
        errors, warnings = validate_changelog.validate_repository(ROOT)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_release_is_blocked_when_required_gates_are_pending(self) -> None:
        record = deepcopy(self.baseline)
        record["evaluation"]["quality"] = {
            "status": "pending",
            "before": None,
            "after": None,
            "unit": None,
            "evidence": None,
        }
        record["approval"] = {
            "status": "pending",
            "approved_by": None,
            "approved_at": None,
            "evidence": None,
        }
        errors = validate_changelog.validate_record(
            record,
            self.baseline_path,
            release=True,
        )
        self.assertTrue(any("não aprovada" in error for error in errors))
        self.assertTrue(any("métrica pendente: quality" in error for error in errors))

    def test_prerelease_record_is_valid_without_own_commit_hash(self) -> None:
        record = deepcopy(self.baseline)
        record["version_control"]["commit"] = None
        errors = validate_changelog.validate_record(
            record,
            self.baseline_path,
            release=True,
        )
        self.assertEqual([], errors)

    def test_self_referential_commit_is_rejected(self) -> None:
        record = deepcopy(self.baseline)
        record["version_control"]["commit"] = "a" * 40
        errors = validate_changelog.validate_record(record, self.baseline_path)
        self.assertTrue(any("commit deve ser nulo" in error for error in errors))

    def test_compatible_tag_and_github_sha_are_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("0.4.1\n", encoding="utf-8")
            sha = "a" * 40
            errors = validate_changelog.validate_tag_context(
                root,
                ref_name="v0.4.1",
                github_sha=sha,
                head_sha=sha,
            )
        self.assertEqual([], errors)

    def test_incompatible_tag_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("0.4.1\n", encoding="utf-8")
            sha = "a" * 40
            errors = validate_changelog.validate_tag_context(
                root,
                ref_name="v0.4.0",
                github_sha=sha,
                head_sha=sha,
            )
        self.assertTrue(any("tag do evento" in error for error in errors))

    def test_github_sha_must_match_tag_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "VERSION").write_text("0.4.1\n", encoding="utf-8")
            errors = validate_changelog.validate_tag_context(
                root,
                ref_name="v0.4.1",
                github_sha="a" * 40,
                head_sha="b" * 40,
            )
        self.assertTrue(any("difere do commit da tag" in error for error in errors))

    def test_published_version_is_registered_separately(self) -> None:
        errors = validate_changelog.validate_publication(
            self.publication,
            self.publication_path,
        )
        self.assertEqual([], errors)
        self.assertEqual("CHG-2026-001", self.publication["change_id"])
        self.assertEqual("released", self.publication["status"])

    def test_publication_cannot_be_declared_early_in_change(self) -> None:
        record = deepcopy(self.baseline)
        record["publication"] = {
            "status": "released",
            "published_at": "2026-07-15T17:14:00-03:00",
        }
        errors = validate_changelog.validate_record(record, self.baseline_path)
        self.assertTrue(any("não pode ser declarada antecipadamente" in error for error in errors))

    def test_baseline_manifests_are_valid(self) -> None:
        self.assertEqual([], validate_changelog.validate_baseline_manifests(ROOT))

    def test_missing_required_field_is_rejected(self) -> None:
        record = deepcopy(self.baseline)
        del record["rollback"]
        errors = validate_changelog.validate_record(record, self.baseline_path)
        self.assertTrue(any("rollback" in error for error in errors))

    def test_duplicate_change_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            changes = root / "changes"
            changes.mkdir()
            (root / "VERSION").write_text("0.4.1\n", encoding="utf-8")
            (root / "CHANGELOG.md").write_text(
                "[0.4.0] CHG-2026-001\n[0.4.1] CHG-2026-001\n",
                encoding="utf-8",
            )
            first = deepcopy(self.baseline)
            second = deepcopy(self.baseline)
            second["version_to"] = "0.4.1"
            second["version_control"]["tag"] = "v0.4.1"
            (changes / "CHG-2026-001.json").write_text(json.dumps(first), encoding="utf-8")
            (changes / "CHG-2026-002.json").write_text(json.dumps(second), encoding="utf-8")
            errors, _ = validate_changelog.validate_repository(root)
            self.assertTrue(any("nome do arquivo" in error for error in errors))
            self.assertTrue(any("change_id duplicado" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
