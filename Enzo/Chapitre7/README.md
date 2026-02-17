# Chapitre 7

## Objectif

Mettre en place un gestionnaire de signal afin d'intercepter le raccourci clavier `Ctrl+C` (signal `SIGINT`) et d'arrêter le programme proprement au lieu de provoquer une interruption brutale.

## Exemple de script

```python
import signal
import sys
import time


def _interrupt_handler(signum, frame):
    """
    Fonction appelée lorsqu'un SIGINT (Ctrl+C) est reçu.
    Elle affiche un message puis termine l'exécution.
    """
    print("\nInterruption clavier détectée, arrêt du script.")
    sys.exit(0)


def main():
    # On enregistre le gestionnaire pour le signal SIGINT
    signal.signal(signal.SIGINT, _interrupt_handler)

    print("Appuyez sur Ctrl+C pour quitter proprement ce programme.")

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
```