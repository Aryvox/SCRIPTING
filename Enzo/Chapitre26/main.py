import subprocess
import re

def change_mac(interface, new_mac):
    if not re.match(r"^[a-zA-Z0-9]+$", interface):
        print("[-] Format d'interface invalide.")
        return

    print(f"[+] Modification de la MAC pour {interface} via 'ip link'...")

    # Nouvelles commandes utilisant 'ip'
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])