import datetime

def get_current_time():
    """Restituisce l'ora attuale in formato stringa."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def add_numbers(a: int, b: int):
    """Somma due numeri interi."""
    return a + b

# Mappa dei tool per l'agente
AVAILABLE_TOOLS = {
    "get_current_time": get_current_time,
    "add_numbers": add_numbers
}
