from typing import List, Optional
from datetime import datetime
import json
import csv

class Player:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Question:
    def __init__(self, id: int, qst: str, arrayResponse: List[str], correctResponse: int, categorie: str):
        self.id = id
        self.qst = qst
        self.arrayResponse = arrayResponse
        self.correctResponse = correctResponse
        self.categorie = categorie

class Historique:
    def __init__(self, name: str, date: str, score: int):
        self.name = name
        self.date = date
        self.score = score

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

# Gestion des Questions
def charger_questions(fichier: str) -> List[Question]:
    questions = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                question = Question(
                    id=item.get('id', 0),
                    qst=item['qst'],
                    arrayResponse=item['arrayResponse'],
                    correctResponse=item['correctResponse'],
                    categorie=item['categorie']
                )
                questions.append(question)
    except FileNotFoundError:
        print(f"Erreur : fichier '{fichier}' introuvable.")
    except Exception as e:
        print(f"Erreur lors du chargement des questions : {e}")
    return questions

def filtrer_questions(questions: List[Question], categorie: str) -> List[Question]:
    return [q for q in questions if q.categorie == categorie]

# Gestion de l'Historique
def ajouter_historique(historiques: List[Historique], nom: str, date: str, score: int) -> None:
    historique = Historique(nom, date, score)
    historiques.append(historique)
    # Append the new history entry to the CSV file
    try:
        with open("resultats.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["nom", "score", "date"])
            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"nom": nom, "score": score, "date": date})
    except Exception as e:
        print(f"Erreur lors de l'ajout dans le fichier CSV : {e}")

def afficher_historique_joueur(historiques: List[Historique], name: str) -> str:
    historique_joueur = [h for h in historiques if h.name == name]
    if not historique_joueur:
        return "Aucun historique trouvé pour ce joueur."
    
    historique_str = f"Historique pour le joueur {name}:\n"
    for h in historique_joueur:
        historique_str += f"Date: {h.date}, Score: {h.score}\n"
    return historique_str

def lire_historique_csv(fichier: str) -> List[Historique]:
    historiques = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                historique = Historique(
                    name=row['nom'],
                    date=row['date'],
                    score=int(row['score'])
                )
                historiques.append(historique)
    except FileNotFoundError:
        print(f"Erreur : fichier '{fichier}' introuvable.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
    return historiques
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
            for i, row in enumerate(reader):
                if row["nom"] == username:
                    scores_found = True
                    print(f"{i + 1}. Score: {row['score']} - Date: {row['date']}")

        if not scores_found:
            display_message("Aucun historique trouvé.", "info")
    except FileNotFoundError:
        display_message("Le fichier resultats.csv est introuvable.", "error")
    except KeyError:
        display_message("Le fichier resultats.csv ne contient pas les colonnes attendues.", "error")
