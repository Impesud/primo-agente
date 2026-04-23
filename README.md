## primo-agente

Mini demo “agentic” in Python: un agente che esegue tool locali e (opzionale) chiama un LLM via riga di comando.

### Quickstart

Requisiti: Python 3.10+ e `pip`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

### Comandi demo

```bash
python3 -m agentic ora
python3 -m agentic somma 15 30
python3 -m agentic llm "Spiega cos'è un agente in 3 punti"
```

### Configurazione `.env` (opzionale)

```bash
cp .env.example .env
```

Variabili principali:
- `AGENTIC_LOG_PATH`: path del log JSONL (default `logs/agentic.log`)
- `OPENAI_API_KEY`: necessaria per `llm`
- `OPENAI_MODEL`: modello di default per `llm` (es. `gpt-4o-mini`)

### Test

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
python -m pytest
```

### Dove mettere le mani

- `src/agentic/__main__.py`: CLI (`python -m agentic ...`)
- `src/agentic/router.py`: mapping comando → tool
- `src/agentic/tools.py`: implementazione tool + `AVAILABLE_TOOLS`
- `src/agentic/agent.py`: `SimpleAgent`
