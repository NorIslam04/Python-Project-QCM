from typing import List, Optional
from datetime import datetime
import json
import csv



class Player:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

# Gestion des Joueurs
def joueur_existe(joueurs: List[Player], name: str) -> bool:
    return any(joueur.name == name for joueur in joueurs)

def ajouter_joueur(joueurs: List[Player], id: int, name: str) -> Player:
    joueur = Player(id, name)
    joueurs.append(joueur)
    return joueur

def rechercher_joueur(joueurs: List[Player], id: int) -> Optional[Player]:
    for joueur in joueurs:
        if joueur.id == id:
            return joueur
    return None

def view_scores(username):
    def clear_console():
        print("\033[H\033[J", end="")  # Efface l'écran (fonctionne sur les systèmes compatibles ANSI)

    def display_header(header):
        print(f"\n{'=' * 20}\n{header}\n{'=' * 20}")

    def display_message(message, msg_type="info"):
        prefix = "[INFO]" if msg_type == "info" else "[ERROR]"
        print(f"{prefix} {message}")

    clear_console()
    display_header("Historique des Scores")

    scores_found = False
    try:
        with open("resultats.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            j=0
            for i, row in enumerate(reader):
                if row["nom"] == username:
                    scores_found = True
                    j+=1
                    print(f"{j}.categorie: {row['categorie']}- Score: ({row['score']}/5) - Date: {row['date']}")

        if not scores_found:
            display_message("Aucun historique trouvé.", "info")
    except FileNotFoundError:
        display_message("Le fichier resultats.csv est introuvable.", "error")
    except KeyError:
        display_message("Le fichier resultats.csv ne contient pas les colonnes attendues.", "error")
