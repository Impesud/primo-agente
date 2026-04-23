import pytest

from agentic.tools import add_numbers, ask_llm, get_current_time


def test_add_numbers():
    assert add_numbers(15, 20) == 35


def test_get_current_time_returns_():
    value = get_current_time()
    assert isinstance(value, str)
    assert value.strip() != ""


def test_ask_llm_requires_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(RuntimeError) as e:
        ask_llm("ciao")
    assert "OPENAI_API_KEY" in str(e.value)
