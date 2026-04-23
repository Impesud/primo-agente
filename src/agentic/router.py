from __future__ import annotations

from .activity_log import log_event

COMMAND_TO_TOOL: dict[str, str] = {
    "ora": "get_current_time",
    "somma": "add_numbers",
    "llm": "ask_llm",
}


def route_command(command: str) -> str:
    cmd = (command or "").strip().lower()
    if not cmd:
        log_event("router_error", command=command, reason="empty_command")
        raise ValueError("Comando vuoto.")

    tool_name = COMMAND_TO_TOOL.get(cmd)
    if tool_name is None:
        log_event("router_error", command=command, reason="unknown_command")
        raise ValueError(f"Comando sconosciuto: {command}")

    log_event("router_routed", command=command, normalized=cmd, tool_name=tool_name)
    return tool_name

