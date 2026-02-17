import smtplib
from email.message import EmailMessage


def build_message(sender: str, recipient: str) -> EmailMessage:
    """
    Construit un message très simple à envoyer pour les tests.
    """
    message = EmailMessage()
    message["Subject"] = "Test"
    message["From"] = sender
    message["To"] = recipient
    message.set_content("Hello world")
    return message


def send_mail(
    smtp_host: str,
    smtp_port: int,
    username: str,
    password: str,
    recipient: str,
) -> None:
    """
    Établit une connexion SMTP chiffrée et envoie un email de test.
    """
    msg = build_message(username, recipient)

    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp:
            smtp.login(username, password)
            smtp.send_message(msg)
        print("Courriel envoyé avec succès.")
    except Exception as exc:  # noqa: BLE001 - pour un exemple pédagogique
        print(f"Échec de l'envoi du mail : {exc}")


if __name__ == "__main__":
    EMAIL_ADDRESS = ""
    EMAIL_PASSWORD = ""
    DESTINATAIRE = ""

    send_mail(
        smtp_host="smtp.gmail.com",
        smtp_port=465,
        username=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
        recipient=DESTINATAIRE,
    )