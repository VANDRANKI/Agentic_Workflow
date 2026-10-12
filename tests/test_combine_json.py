"""Tests for combine_json.combine_corrected_json."""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import combine_json  # noqa: E402


def _paper(base, subdir, name, files):
    folder = base / subdir / name
    folder.mkdir(parents=True)
    for filename, content in files.items():
        (folder / filename).write_text(content, encoding="utf-8")
    return folder


def _combine(base, subdirs, out):
    combine_json.combine_corrected_json(str(base), subdirs, str(out))
    return json.loads(out.read_text(encoding="utf-8")) if out.exists() else None


def test_combines_one_corrected_file_per_paper_across_subdirs(tmp_path):
    _paper(tmp_path, "setA", "p1", {"p1_Correct_Extraction.json": json.dumps({"id": 1})})
    _paper(tmp_path, "setB", "p2", {"p2_Correct_Extraction.json": json.dumps({"id": 2})})
    out = tmp_path / "combined.json"
    data = _combine(tmp_path, ["setA", "setB"], out)
    assert sorted(d["id"] for d in data) == [1, 2]


def test_files_without_the_corrected_suffix_are_ignored(tmp_path):
    _paper(tmp_path, "setA", "p1", {
        "p1_extracted_data.json": json.dumps({"id": "raw"}),
        "p1_Correct_Extraction.json": json.dumps({"id": "good"}),
    })
    data = _combine(tmp_path, ["setA"], tmp_path / "combined.json")
    assert data == [{"id": "good"}]


def test_unicode_is_written_as_characters_not_escapes(tmp_path):
    _paper(tmp_path, "setA", "p1", {"p1_Correct_Extraction.json": json.dumps({"unit": "°C"})})
    out = tmp_path / "combined.json"
    _combine(tmp_path, ["setA"], out)
    assert "°C" in out.read_text(encoding="utf-8")


def test_invalid_json_is_skipped_and_the_rest_still_combine(tmp_path):
    _paper(tmp_path, "setA", "bad", {"bad_Correct_Extraction.json": "{not json"})
    _paper(tmp_path, "setA", "good", {"good_Correct_Extraction.json": json.dumps({"id": 1})})
    data = _combine(tmp_path, ["setA"], tmp_path / "combined.json")
    assert data == [{"id": 1}]


def test_missing_subdirectory_is_skipped(tmp_path):
    _paper(tmp_path, "setA", "p1", {"p1_Correct_Extraction.json": json.dumps({"id": 1})})
    data = _combine(tmp_path, ["nope", "setA"], tmp_path / "combined.json")
    assert data == [{"id": 1}]


def test_no_output_file_when_nothing_was_found(tmp_path):
    _paper(tmp_path, "setA", "p1", {"notes.txt": "x"})
    out = tmp_path / "combined.json"
    assert _combine(tmp_path, ["setA"], out) is None


def test_missing_base_directory_exits_with_status_1(tmp_path):
    with pytest.raises(SystemExit) as exc:
        combine_json.combine_corrected_json(str(tmp_path / "missing"), ["a"], str(tmp_path / "o.json"))
    assert exc.value.code == 1
