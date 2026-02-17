# Chapitre 2

## Objectif

Établir une connexion SSH vers une machine distante à l'aide d'un script Python et exécuter une commande simple à distance.

## Prérequis

```bash
pip install paramiko
```

## Script d'exemple

```python
from paramiko import SSHClient, AutoAddPolicy

def run_remote_command(
    hostname: str,
    username: str,
    password: str,
    command: str = "ls",
) -> None:
    """
    Ouvre une session SSH, exécute une commande et affiche la sortie.
    """
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode("utf-8")
        error = stderr.read().decode("utf-8")

        if output:
            print("Sortie standard :")
            print(output)
        if error:
            print("Sortie d'erreur :")
            print(error)
    finally:
        client.close()


if __name__ == "__main__":
    run_remote_command("192.168.122.195", username="adrien", password="password")
```