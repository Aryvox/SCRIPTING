#!/usr/bin/env python3
import sys

from scapy.all import IP, ICMP, sr1


def build_icmp_echo_request(target_ip: str):
    """Construit un paquet ICMP Echo Request destiné à l'adresse fournie."""
    return IP(dst=target_ip) / ICMP()


def send_and_inspect_packet(packet, timeout: int = 2):
    """
    Envoie le paquet fourni et affiche un résumé de la réponse.

    La fonction ne retourne rien mais se contente de journaliser les étapes
    afin de faciliter la compréhension du flux ICMP.
    """
    print("\n--- [3] Envoi du paquet et attente de la réponse ---")
    response = sr1(packet, timeout=timeout, verbose=0)

    print("\n--- [4] Observation de la réponse reçue ---")
    if not response:
        print("Aucune réponse reçue (délai dépassé ou paquet perdu).")
        return

    print(f"Réponse reçue depuis {response[IP].src}")
    response.show()

    if response[ICMP].type == 0:
        print("\n>> Le paquet retourné est bien un 'Echo Reply'.")


def main():
    target_ip = "8.8.8.8"

    print(f"--- [1] Construction d'un paquet ICMP vers {target_ip} ---")
    packet = build_icmp_echo_request(target_ip)

    print("\n--- [2] Détail du paquet ICMP généré ---")
    packet.show()

    send_and_inspect_packet(packet)


if __name__ == "__main__":
    main()