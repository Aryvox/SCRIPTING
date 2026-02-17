import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt  # noqa: E402
import subprocess  # noqa: E402


def extraire_donnees_sar(intervalle: int = 1, iterations: int = 5):
    """
    Lance la commande `sar` pour récupérer l'évolution de l'activité CPU.

    On retourne deux listes parallèles :
    - une liste de timestamps (chaînes),
    - une liste de valeurs d'inactivité CPU (idle) sous forme de flottants.
    """
    temps: list[str] = []
    cpu_idle: list[float] = []

    try:
        resultat = subprocess.run(
            ["sar", "-u", str(intervalle), str(iterations)],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:  # noqa: BLE001
        print(f"Impossible d'exécuter sar (est-il installé ?) : {exc}")
        return [], []

    lignes = resultat.stdout.strip().split("\n")

    for ligne in lignes:
        colonnes = ligne.split()
        if not colonnes or ":" not in colonnes[0] or "Average" in colonnes[0]:
            continue

        try:
            horodatage = colonnes[0]
            idle_val = float(colonnes[-1].replace(",", "."))
        except ValueError:
            # Ligne non exploitable, on l'ignore simplement
            continue

        temps.append(horodatage)
        cpu_idle.append(idle_val)

    return temps, cpu_idle


def generer_graphique(temps, idle):
    """
    Produit un graphique représentant la charge CPU au fil du temps.
    """
    if not temps:
        print("Aucune donnée collectée, aucun graphique généré.")
        return

    charge_cpu = [100 - valeur_idle for valeur_idle in idle]

    plt.figure(figsize=(10, 5))
    plt.plot(
        temps,
        charge_cpu,
        marker="o",
        linestyle="-",
        color="r",
        label="Charge CPU (%)",
    )
    plt.ylim(0, 100)
    plt.xlabel("Temps")
    plt.ylabel("Activité (%)")
    plt.title("Évolution de l'activité du serveur (100 - %idle)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    horodatages, valeurs_idle = extraire_donnees_sar()
    generer_graphique(horodatages, valeurs_idle)