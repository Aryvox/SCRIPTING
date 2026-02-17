import socket


def start_client(host: str = "localhost", port: int = 12345) -> None:
    """
    Se connecte à un serveur TCP, envoie un message et affiche la réponse.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))

        message = "Hello World!"
        client.sendall(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        print(f"Réponse du serveur : {response}")

    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur.")
    finally:
        client.close()


if __name__ == "__main__":
    start_client()
