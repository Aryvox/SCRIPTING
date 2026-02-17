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
