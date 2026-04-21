from agentic.agent import SimpleAgent


def test_agent_execute_ok_contains_result():
    agent = SimpleAgent(name="TestBot")
    out = agent.execute(task="Somma", tool_name="add_numbers", a=1, b=2)
    assert "3" in out


def test_agent_execute_unknown_tool_fallback():
    agent = SimpleAgent(name="TestBot")
    out = agent.execute(task="X", tool_name="non_esiste")
    assert "non so come usare" in out.lower()


def test_agent_execute_command_routes_and_runs():
    agent = SimpleAgent(name="TestBot")
    out = agent.execute_command(task="Somma", command="somma", a=2, b=3)
    assert "5" in out


def test_agent_logging_smoke(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTIC_LOG_PATH", str(tmp_path / "agentic.log"))
    agent = SimpleAgent(name="TestBot")
    agent.execute_command(task="Somma", command="somma", a=1, b=2)
