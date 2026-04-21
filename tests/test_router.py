import pytest

from agentic.router import route_command


def test_route_command_ok():
    assert route_command("ora") == "get_current_time"
    assert route_command("somma") == "add_numbers"


def test_route_command_normalization():
    assert route_command("  ORA  ") == "get_current_time"


def test_route_command_empty_raises():
    with pytest.raises(ValueError):
        route_command("")


def test_route_command_unknown_raises():
    with pytest.raises(ValueError):
        route_command("non_esiste")


def test_router_logging_smoke(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTIC_LOG_PATH", str(tmp_path / "agentic.log"))
    route_command("ora")
