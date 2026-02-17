# Chapitre 11

## Consigne

- Utilisez Scapy pour lancer un sniffer de paquets afin de capturer le trafic réseau.
- Générez du trafic réseau à partir de votre machine pour observer les différents types de paquets capturés.
- Affichez la capture du trafic à l'écran de manière claire et lisible pour une analyse rapide.

## Script

```python
from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "Autre"

        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
        elif packet.haslayer(ICMP):
            proto = "ICMP"

        print(f"[{proto}] {src_ip} -> {dst_ip}")


try:
    sniff(prn=packet_callback, store=0)
except KeyboardInterrupt:
    print("\nArrêt du sniffer.")
```