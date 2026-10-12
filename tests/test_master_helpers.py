"""Tests for the small helpers in master_extractor and for process_paper's output handling."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import master_extractor as me  # noqa: E402


class TestFindFiles:
    def test_returns_the_markdown_file_and_images_dir(self, tmp_path):
        (tmp_path / "paper.md").write_text("# t")
        (tmp_path / "images").mkdir()
        md, images = me.find_files(str(tmp_path))
        assert os.path.basename(md) == "paper.md"
        assert os.path.basename(images) == "images"

    def test_no_markdown_file_gives_none_none(self, tmp_path):
        assert me.find_files(str(tmp_path)) == (None, None)

    def test_missing_images_dir_is_none_but_markdown_is_still_returned(self, tmp_path):
        (tmp_path / "paper.md").write_text("# t")
        md, images = me.find_files(str(tmp_path))
        assert md is not None and images is None


class TestParseMarkdownTable:
    TABLE = "| a | b |\n| :-: | :-: |\n| 1 | 2 |\n| 3 | 4 |"

    def test_rows_become_dicts_keyed_by_header(self):
        assert me.parse_markdown_table(self.TABLE) == [
            {"a": "1", "b": "2"},
            {"a": "3", "b": "4"},
        ]

    def test_header_and_separator_only_gives_no_rows(self):
        assert me.parse_markdown_table("| a | b |\n| - | - |") == []

    def test_malformed_row_is_skipped_not_fatal(self):
        text = "| a | b |\n| - | - |\n| 1 | 2 |\n| only one |\n| 5 | 6 |"
        assert me.parse_markdown_table(text) == [{"a": "1", "b": "2"}, {"a": "5", "b": "6"}]

    def test_surrounding_whitespace_is_ignored(self):
        assert me.parse_markdown_table("\n\n" + self.TABLE + "\n\n")[0] == {"a": "1", "b": "2"}


class TestReadImageJson:
    def test_reads_a_valid_file(self, tmp_path):
        path = tmp_path / "img-0.json"
        path.write_text(json.dumps({"figure": "XRD"}), encoding="utf-8")
        assert me.read_image_json(str(path)) == {"figure": "XRD"}

    def test_missing_file_gives_none(self, tmp_path):
        assert me.read_image_json(str(tmp_path / "nope.json")) is None

    def test_corrupt_file_gives_none(self, tmp_path):
        path = tmp_path / "bad.json"
        path.write_text("{oops")
        assert me.read_image_json(str(path)) is None


class TestProcessPaper:
    def test_folder_without_markdown_writes_nothing(self, tmp_path, monkeypatch):
        out = tmp_path / "out"
        monkeypatch.setattr(me, "OUTPUT_DIR", str(out))
        paper = tmp_path / "paper1"
        paper.mkdir()
        me.process_paper(str(paper))
        assert not out.exists()

    def test_output_is_named_after_the_paper_folder(self, tmp_path, monkeypatch):
        sample_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "Input_Md_Images", "0220_CMP_Slurries", "1_k9dmxr",
        )
        out = tmp_path / "out"
        monkeypatch.setattr(me, "OUTPUT_DIR", str(out) + os.sep)
        me.process_paper(sample_dir)
        written = out / "1_k9dmxr_extracted_data.json"
        assert written.exists()
        assert json.loads(written.read_text(encoding="utf-8"))
