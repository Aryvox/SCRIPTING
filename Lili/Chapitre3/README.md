# Chapitre 3

## Objectif

Manipuler des fichiers temporaires en Python : création, écriture, relecture et suppression automatique à la fermeture.

## Script d'exemple

```python
import tempfile
import time


def create_and_display_tempfile() -> None:
    """
    Crée un fichier temporaire, y écrit quelques lignes puis les relit.
    """
    with tempfile.NamedTemporaryFile(
        mode="w+",
        delete=True,
        encoding="utf-8",
    ) as fp:
        print(f"Fichier temporaire créé : {fp.name}\n")

        fp.write("test\ntest")
        fp.flush()

        fp.seek(0)
        # Pause prolongée pour pouvoir examiner le fichier à la main
        time.sleep(600)
        print("Contenu du fichier :")
        print(fp.read())


if __name__ == "__main__":
    create_and_display_tempfile()
```
