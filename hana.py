import csv
import json
from display import clear_console, display_header, display_message

class Historique:
    def init(self, name: str, date: str, score: int,categorie: str):
        self.name = name
        self.date = date
        self.score = score
        self.categorie = categorie


def ajouter_historique( nom: str, date: str, score: int,categorie: str) -> None:
    # Append the new history entry to the CSV file
    try:
        with open("resultats.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["nom","categorie", "score", "date"])
            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"nom": nom,"categorie":categorie, "score": score, "date": date})
    except Exception as e:
        print(f"Erreur lors de l'ajout dans le fichier CSV : {e}")

        
#...................................................................................................................................................................
def view_user_responses(username: str) -> None:
    """Affiche les réponses détaillées de l'utilisateur depuis le fichier JSON."""
    clear_console()
    display_header("Historique Détaillé des Réponses")

    try:
        with open("reponse_user.json", "r", encoding="utf-8") as f:
            responses = json.load(f)

        user_entries = [entry for entry in responses if entry["username"] == username]

        if not user_entries:
            display_message("Aucune réponse trouvée pour cet utilisateur.", "info")
            return

        for entry in user_entries:
            print(f"\n{'='*50}")
            print(f"Catégorie: {entry['category']}")
            print(f"Date: {entry['date']}")
            print(f"Score: {entry['score']}/5")
            print(f"{'='*50}")

            for i, q in enumerate(entry["questions"], 1):
                print(f"\nQuestion {i}: {q['question']}")
                if q['user_response'] == "Pas de réponse":
                    print("\033[93mPas de réponse (temps écoulé)\033[0m")
                else:
                    if q['user_response'] == q['correct_response']:
                        print(f"\033[92mVotre réponse: {q['user_response']} (Correct)\033[0m")
                    else:
                        print(f"\033[91mVotre réponse: {q['user_response']} (Incorrect)\033[0m")
                    print(f"\033[92mBonne réponse: {q['correct_response']}\033[0m")
                print("-" * 40)

    except FileNotFoundError:
        display_message("Aucun historique de réponses trouvé.", "error")
    except json.JSONDecodeError:
        display_message("Erreur lors de la lecture du fichier de réponses.", "error")
    except Exception as e:
        display_message(f"Une erreur est survenue: {str(e)}", "error")