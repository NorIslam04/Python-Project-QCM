from datetime import datetime
import json
import csv
from display import clear_console, display_header, display_message



def view_scores(username):
    
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


def save_user_responses(username: str, category: str, responses: list, questions: list) -> None:

    # Prépare les données à sauvegarder
    user_data = {
        "username": username,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "questions": []
    }

    # Pour chaque question et réponse
    for i, (question, response) in enumerate(zip(questions, responses)):
        q_data = {
            "question": question["qst"],
            "user_response": -1 if response is None else response,
            "correct_response": question["correctResponse"]
        }
        user_data["questions"].append(q_data)

    try:
        # Charge les données existantes
        existing_data = []
        try:
            with open("reponse_user.json", "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Ajoute les nouvelles données
        if not isinstance(existing_data, list):
            existing_data = []
        existing_data.append(user_data)

        # Sauvegarde dans le fichier
        with open("reponse_user.json", "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        display_message(f"Erreur lors de la sauvegarde des réponses: {e}", "error")
