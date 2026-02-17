import socket


def start_server(host: str = "localhost", port: int = 12345) -> None:
    """
    Démarre un petit serveur TCP qui accepte un client,
    affiche son message puis renvoie une réponse.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))
    server.listen(1)
    print(f"Serveur en écoute sur {host}:{port}")

    client_socket, address = server.accept()
    print(f"Connexion établie avec {address}")

    data = client_socket.recv(1024).decode("utf-8")
    print(f"Message reçu : {data}")

    client_socket.sendall("Message de confirmation du serveur".encode("utf-8"))

    client_socket.close()
    server.close()


if __name__ == "__main__":
    start_server()