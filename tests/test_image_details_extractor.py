"""Tests for image_details_extractor: base64 encoding and the Vision API call."""
import base64
import os
import sys
from types import SimpleNamespace

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

pytest.importorskip("openai")

import image_details_extractor as ide  # noqa: E402


class TestEncodeImageToBase64:
    def test_png_is_encoded_as_a_data_uri(self, tmp_path):
        path = tmp_path / "fig.png"
        path.write_bytes(b"\x89PNG-bytes")
        out = ide.encode_image_to_base64(str(path))
        assert out == "data:image/png;base64," + base64.b64encode(b"\x89PNG-bytes").decode()

    def test_jpeg_mime_type_follows_the_extension(self, tmp_path):
        path = tmp_path / "fig.jpg"
        path.write_bytes(b"abc")
        assert ide.encode_image_to_base64(str(path)).startswith("data:image/jpeg;base64,")

    def test_unknown_extension_defaults_to_png(self, tmp_path, capsys):
        path = tmp_path / "fig.unknownext"
        path.write_bytes(b"abc")
        out = ide.encode_image_to_base64(str(path))
        assert out.startswith("data:image/png;base64,")
        assert "Warning" in capsys.readouterr().err

    def test_missing_file_returns_none(self, tmp_path, capsys):
        assert ide.encode_image_to_base64(str(tmp_path / "nope.png")) is None
        assert "not found" in capsys.readouterr().err

    def test_directory_returns_none(self, tmp_path, capsys):
        assert ide.encode_image_to_base64(str(tmp_path)) is None
        assert "not a file" in capsys.readouterr().err


class _FakeCompletions:
    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
        self.kwargs = None

    def create(self, **kwargs):
        self.kwargs = kwargs
        if self.error:
            raise self.error
        return self.response


def _client(completions):
    return SimpleNamespace(chat=SimpleNamespace(completions=completions))


def _response(content):
    return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])


@pytest.fixture
def image(tmp_path):
    path = tmp_path / "fig.png"
    path.write_bytes(b"data")
    return str(path)


class TestGetImageDetails:
    def test_returns_the_model_text_and_sends_prompt_and_image(self, monkeypatch, image):
        comp = _FakeCompletions(_response("A bar chart."))
        monkeypatch.setattr(ide, "client", _client(comp))
        assert ide.get_image_details(image, "Describe it") == "A bar chart."
        content = comp.kwargs["messages"][0]["content"]
        assert content[0] == {"type": "text", "text": "Describe it"}
        assert content[1]["image_url"]["url"].startswith("data:image/png;base64,")

    def test_no_client_returns_none(self, monkeypatch, image, capsys):
        monkeypatch.setattr(ide, "client", None)
        assert ide.get_image_details(image, "Describe it") is None
        assert "not initialized" in capsys.readouterr().err

    def test_unreadable_image_does_not_call_the_api(self, monkeypatch, tmp_path):
        comp = _FakeCompletions(_response("x"))
        monkeypatch.setattr(ide, "client", _client(comp))
        assert ide.get_image_details(str(tmp_path / "nope.png"), "Describe it") is None
        assert comp.kwargs is None

    def test_api_error_returns_none(self, monkeypatch, image, capsys):
        monkeypatch.setattr(ide, "client", _client(_FakeCompletions(error=RuntimeError("down"))))
        assert ide.get_image_details(image, "Describe it") is None
        assert "down" in capsys.readouterr().err

    def test_empty_choices_returns_none(self, monkeypatch, image):
        comp = _FakeCompletions(SimpleNamespace(choices=[]))
        monkeypatch.setattr(ide, "client", _client(comp))
        assert ide.get_image_details(image, "Describe it") is None
