# Chapitre 9

## Objectif

Effectuer une requête HTTP simple vers un petit service web et afficher le code de statut retourné.

## Script d'exemple

```python
import requests


def check_endpoint(url: str) -> None:
    """
    Interroge une URL et affiche le code de retour HTTP.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Succès, code HTTP {response.status_code}")
        else:
            print(f"Réponse inattendue, code HTTP : {response.status_code}")
    except Exception as exc:
        print(f"Erreur lors de la requête : {exc}")


if __name__ == "__main__":
    check_endpoint("https://hello-world.zdarkblackshadow.com")
```