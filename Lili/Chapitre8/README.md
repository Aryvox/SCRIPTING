# Chapitre 8 : MySQL et subprocess

## Objectif

- Créer une base de données MySQL et une table simple.
- Insérer un enregistrement de test.
- Utiliser le module `subprocess` pour interroger la base via la commande `mysql`.

## Script d'exemple

```python
import mysql.connector
from mysql.connector import Error
import subprocess


def configure_database():
    """
    Crée une base de données de test, une table simple et insère une entrée,
    puis affiche le contenu de la table via la CLI `mysql`.
    """
    try:
        connexion = mysql.connector.connect(
            host="localhost",
            user="user",
            password="password",
        )

        if not connexion.is_connected():
            print("Connexion MySQL non établie.")
            return

        cursor = connexion.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS test")
        cursor.execute("USE test")

        requete_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            password VARCHAR(100)
        )
        """
        cursor.execute(requete_table)

        cursor.execute(
            "INSERT INTO users (name, password) VALUES ('admin', 'secret')"
        )
        connexion.commit()

        commande = [
            "mysql",
            "-u",
            "user",
            "-ppassword",
            "-D",
            "test",
            "-e",
            "SELECT * FROM users;",
        ]

        resultat = subprocess.run(
            commande,
            capture_output=True,
            text=True,
            check=True,
        )
        print(resultat.stdout)

    except Error as exc:
        print(f"Erreur MySQL : {exc}")
    except subprocess.CalledProcessError as exc:
        print(f"Erreur lors de l'appel à mysql : {exc.stderr}")
    finally:
        if "connexion" in locals() and connexion.is_connected():
            cursor.close()
            connexion.close()


if __name__ == "__main__":
    configure_database()
```