from agentic.tools import add_numbers, get_current_time


def test_add_numbers():
    assert add_numbers(15, 20) == 35


def test_get_current_time_returns_():
    value = get_current_time()
    assert isinstance(value, str)
    assert value.strip() != ""
