# main.py
import sys
from pathlib import Path

# Permette di importare i moduli da ./src senza installazione del pacchetto
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from agentic.agent import SimpleAgent

def main():
    # Inizializziamo l'agente
    bot = SimpleAgent(name="Zeta")

    print("--- BENVENUTO NEL SISTEMA AGENTICO ---")

    # Esempio 1: Calcolo
    risultato_somma = bot.execute_command(
        task="Calcola la somma di 15 e 30", 
        command="somma",
        a=15, 
        b=30
    )
    print(risultato_somma)

    # Esempio 2: Ora attuale
    risultato_ora = bot.execute_command(
        task="Dimmi che ore sono", 
        command="ora"
    )
    print(risultato_ora)

if __name__ == "__main__":
    main()