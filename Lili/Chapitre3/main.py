import tempfile
import time


def create_and_display_tempfile() -> None:
    """
    Crée un fichier temporaire, y écrit quelques lignes puis les relit.

    Le `sleep` est conservé pour laisser le temps d'inspecter le fichier
    temporaire sur le système si besoin.
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