# Chapitre 6

## Objectif

Mettre en place une petite application en ligne de commande en utilisant le module `argparse`.  
L'idée est de définir plusieurs options obligatoires et de récupérer leurs valeurs lorsqu'on lance le script.

## Script d'exemple

```python
import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    Construit un analyseur de paramètres avec trois options obligatoires.
    """
    parser = argparse.ArgumentParser(
        description="Petit exemple d'utilisation d'argparse."
    )
    parser.add_argument(
        "-f",
        "--foo",
        help="Valeur associée à l'option foo.",
        required=True,
    )
    parser.add_argument(
        "-b",
        "--bar",
        help="Texte à afficher en sortie.",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--coo",
        help="Argument factice supplémentaire pour l'exemple.",
        required=True,
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # Ici on se contente d'afficher la valeur passée à --bar
    print(args.bar)


if __name__ == "__main__":
    main()
```