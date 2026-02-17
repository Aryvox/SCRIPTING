from paramiko import SSHClient, AutoAddPolicy


def run_remote_command(
    hostname: str,
    username: str,
    password: str,
    command: str = "ls",
) -> None:
    """
    Établit une connexion SSH simple, exécute une commande puis affiche
    la sortie standard et la sortie d'erreur éventuelle.
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
