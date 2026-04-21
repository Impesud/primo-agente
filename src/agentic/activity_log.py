from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any


def _now_iso() -> str:
    # ISO-ish senza dipendenze esterne
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())


def _log_path() -> Path:
    # Default: ./logs/agentic.log (relativo alla cwd di esecuzione)
    raw = os.environ.get("AGENTIC_LOG_PATH", "").strip()
    if raw:
        return Path(raw)
    return Path("logs") / "agentic.log"


def _jsonable(value: Any) -> Any:
    try:
        json.dumps(value)
        return value
    except TypeError:
        return repr(value)


def log_event(event: str, **fields: Any) -> None:
    path = _log_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    payload: dict[str, Any] = {"ts": _now_iso(), "event": event}
    for k, v in fields.items():
        payload[k] = _jsonable(v)

    # JSONL: una riga per evento
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

