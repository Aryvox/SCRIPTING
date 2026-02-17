# Chapitre 10 : Visualisation de la charge CPU

## Objectif

Interroger la commande `sar` pour récupérer des statistiques d'utilisation processeur, puis représenter graphiquement l'évolution de la charge CPU au fil du temps à l'aide de `matplotlib`.

## Script d'exemple

```python
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt  # noqa: E402
import subprocess  # noqa: E402


def extraire_donnees_sar(intervalle: int = 1, iterations: int = 5):
    """
    Récupère les mesures CPU fournies par la commande sar.
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
    except subprocess.CalledProcessError as exc:
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
            continue

        temps.append(horodatage)
        cpu_idle.append(idle_val)

    return temps, cpu_idle


def generer_graphique(temps, idle):
    """
    Trace la charge CPU (100 - %idle) en fonction du temps.
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
```
