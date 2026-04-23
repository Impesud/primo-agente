import datetime
import os

def get_current_time():
    """Restituisce l'ora attuale in formato stringa."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def add_numbers(a: int, b: int):
    """Somma due numeri interi."""
    return a + b


def ask_llm(
    prompt: str,
    system: str | None = None,
    model: str | None = None,
    temperature: float = 0.2,
):
    """
    Chiama un LLM via OpenAI.

    Richiede `OPENAI_API_KEY` nell'ambiente. Modello configurabile via argomento o `OPENAI_MODEL`.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY mancante: imposta la variabile d'ambiente o un file .env.")

    resolved_model = model or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"

    try:
        from openai import OpenAI
    except Exception as e:  # pragma: no cover
        raise RuntimeError("Dipendenza 'openai' non disponibile. Installa il progetto con le dipendenze.") from e

    client = OpenAI(api_key=api_key)
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model=resolved_model,
        messages=messages,
        temperature=temperature,
    )
    return resp.choices[0].message.content or ""

# Mappa dei tool per l'agente
AVAILABLE_TOOLS = {
    "get_current_time": get_current_time,
    "add_numbers": add_numbers,
    "ask_llm": ask_llm,
}
