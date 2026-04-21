# main.py
import sys
from pathlib import Path

# Permette di importare i moduli da ./src senza installazione del pacchetto
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from agentic.agent import SimpleAgent
from agentic.router import route_command

def main():
    # Inizializziamo l'agente
    bot = SimpleAgent(name="Zeta")

    print("--- BENVENUTO NEL SISTEMA AGENTICO ---")

    # Esempio 1: Calcolo
    comando_somma = "somma"
    risultato_somma = bot.execute(
        task="Calcola la somma di 15 e 30",
        tool_name=route_command(comando_somma),
        a=15, 
        b=30
    )
    print(risultato_somma)

    # Esempio 2: Ora attuale
    comando_ora = "ora"
    risultato_ora = bot.execute(
        task="Dimmi che ore sono",
        tool_name=route_command(comando_ora),
    )
    print(risultato_ora)

if __name__ == "__main__":
    main()