import typer
from rich import print


# Fonction pour savoir si une année est bissextile ou non
def bissextile(annee):
    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        return True
    return False


# Fonction d'affichage
def affichage(annee):
    if bissextile(annee):
        print(f"[green]L'année {annee} est bissextile[/green]")
    else:
        print(f"[magenta]L'année {annee} n'est pas bissextile[/magenta]")


# Fonctin qui garde le menu, pour ne pas avoir à le copier/coller
def menu():
    print()
    print("[bold yellow]************************************************************************[/bold yellow]")
    print("Pour tester si une année est [bold blue]bissextile[/bold blue], [italic green]tapez 1[/italic green].")
    print(
        "Pour connaitre toues les [bold blue]années bissextile entre deux dates[/bold blue], [italic green]tapez 2[/italic green].")
    print("Pour [bold blue] quiter[/bold blue] le programme, [italic green]tapez 3[/italic green].")
    try:
        choix = int(input("Faites votre choix : "))
        return choix

    # On fait attention que l'utilisateur saisisse un nombre
    except ValueError:
        print("[bold red]Il faut rentrer un nombre pour naviguer dans le menu.[/bold red]")


# Fonction principale qui gère le programme
def main():
    choix = menu()
    while choix != 3:

        if choix == 1:
            try:
                # On demande à l'utilisateur l'année qu'il souhaite tester
                annee = int(input("Entrez l'année à tester : "))
                affichage(annee)

            # On fait attention, si l'utilisateur fait une saisie invalide, le programme doit continuer
            except ValueError:
                print("[bold red]Année invalide.[/bold red]")

        elif choix == 2:
            # On demande les années "bornes" pour chercher les années bissextiles entre les deux
            print("Entrez les années bornes pour le test")
            try:
                annee_debut = int(input("Année de début : "))
                annee_fin = int(input("Année de fin : "))
                # On créer une liste qui va stocker toutes les années bissextiles comprises entre les deux bornes
                annees_bissextiles = []

                if annee_debut > annee_fin:
                    print("L'année de début doit être la plus petite.")

                else:
                    for i in range(annee_fin - annee_debut + 1):
                        # On récupère toutes les années bissextile comprises entre les deux dates et on les stocke dans une liste
                        if bissextile(annee_debut):
                            annees_bissextiles.append(annee_debut)
                        annee_debut += 1

                # On affiche toutes les années bissextiles que l'on a récupéré
                for i in range(len(annees_bissextiles)):
                    affichage(annees_bissextiles[i])

            # On fait attention, si l'utilisateur fait une saisie invalide, le programme doit continuer
            except ValueError:
                print("[bold red]Saisie invalide.[/bold red]")

        else:
            # Si le choix n'est pas valide, on le signale à l'utilsateur
            print("[bold red]Choix invalide.[/bold red]")

        choix = menu()


if __name__ == "__main__":
    typer.run(main)
