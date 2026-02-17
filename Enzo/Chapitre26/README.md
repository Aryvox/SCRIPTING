# Chapitre 26: Adresse MAC

## Consigne

- Changez l'adresse MAC d’une interface réseau manuellement.
- Réalisez un script Python qui va changer l’adresse MAC.
- Prenez en argument l’interface à modifier.
- Vérifiez que l’interface prise en argument est au bon format.

## 1. Changez l'adresse MAC d’une interface réseau manuellement.

Down l'interface
```bash
sudo ip link set dev eth0 down
```
On change l'addresse
```bash
sudo ip link set dev eth0 address 00:11:22:33:44:55
```
et on la remet up
```bash
sudo ip link set dev eth0 up
```

## Le rest est dans le script python `main.py`