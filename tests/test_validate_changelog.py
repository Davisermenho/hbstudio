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

    def test_repository_contract_is_valid(self) -> None:
        errors, _ = validate_changelog.validate_repository(ROOT)
        self.assertEqual([], errors)

    def test_release_is_blocked_when_required_gates_are_pending(self) -> None:
        record = deepcopy(self.baseline)
        record["approval"] = {
            "status": "pending",
            "approved_by": None,
            "approved_at": None,
            "evidence": None,
        }
        record["version_control"] = {"commit": None, "tag": None}
        errors = validate_changelog.validate_record(
            record,
            self.baseline_path,
            release=True,
        )
        self.assertTrue(any("não aprovada" in error for error in errors))
        self.assertTrue(any("commit e tag não registrados" in error for error in errors))

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
            (changes / "CHG-2026-001.json").write_text(json.dumps(first), encoding="utf-8")
            (changes / "CHG-2026-002.json").write_text(json.dumps(second), encoding="utf-8")
            errors, _ = validate_changelog.validate_repository(root)
            self.assertTrue(any("nome do arquivo" in error for error in errors))
            self.assertTrue(any("change_id duplicado" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
