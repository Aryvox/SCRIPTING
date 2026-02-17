import signal
import sys
import time


def _interrupt_handler(signum, frame):
    """
    Gestionnaire appelé lorsqu'un SIGINT (Ctrl+C) est reçu.

    Il affiche un court message informatif puis termine proprement
    l'exécution du programme.
    """
    # On évite d'avoir une ligne "sale" dans le terminal
    print("\nInterruption clavier détectée, arrêt du script.")
    sys.exit(0)


def main():
    """Boucle principale qui attend indéfiniment un SIGINT."""
    signal.signal(signal.SIGINT, _interrupt_handler)

    print("Appuyez sur Ctrl+C pour quitter proprement ce programme.")

    while True:
        # On dort une seconde pour ne pas monopoliser le CPU
        time.sleep(1)


if __name__ == "__main__":
    main()