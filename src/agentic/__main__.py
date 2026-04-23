from __future__ import annotations

import sys
from typing import Any

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    load_dotenv = None

from .agent import SimpleAgent
from .router import route_command


def _print_usage() -> None:
    print(
        "Uso:\n"
        "  python -m agentic ora\n"
        "  python -m agentic somma <a> <b>\n"
        "  python -m agentic llm <prompt...>\n"
        "\n"
        "Esempi:\n"
        "  python -m agentic ora\n"
        "  python -m agentic somma 15 30\n"
        "  python -m agentic llm \"Spiega cos'è un agente\" \n"
    )


def _run(argv: list[str]) -> int:
    if load_dotenv is not None:
        load_dotenv()

    if len(argv) < 2:
        _print_usage()
        return 2

    command = argv[1]

    kwargs: dict[str, Any] = {}
    if command.strip().lower() == "somma":
        if len(argv) != 4:
            print("Errore: per 'somma' servono due numeri: somma <a> <b>.")
            _print_usage()
            return 2
        try:
            kwargs["a"] = int(argv[2])
            kwargs["b"] = int(argv[3])
        except ValueError:
            print("Errore: <a> e <b> devono essere interi.")
            return 2
    elif command.strip().lower() == "llm":
        if len(argv) < 3:
            print("Errore: per 'llm' serve un prompt: llm <prompt...>.")
            _print_usage()
            return 2
        kwargs["prompt"] = " ".join(argv[2:]).strip()

    bot = SimpleAgent(name="Zeta")
    try:
        tool_name = route_command(command)
    except ValueError as e:
        print(f"Errore: {e}")
        _print_usage()
        return 2

    out = bot.execute(task=f"Esegui comando: {command}", tool_name=tool_name, **kwargs)
    print(out)
    return 0


def main() -> None:
    raise SystemExit(_run(sys.argv))


if __name__ == "__main__":
    main()

