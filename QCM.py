import msvcrt
import os
import sys
import time
import json
from datetime import datetime
from ramy import view_scores
from hana import ajouter_historique
from display import clear_console, display_header, display_message, typewriter_effect, display_menu, display_categories


questions = []
user_answers = []
score = 0
chosen_category = ""


# Load questions from the `QST` directory based on the chosen category
def load_questions_by_category(category, directory="QST"):
    global questions
    try:
        filepath = os.path.join(directory, f"{category}.json")  # Construct path to category file
        if os.path.exists(filepath):  # Check if the file exists
            with open(filepath, "r", encoding="utf-8") as f:
                questions = json.load(f)  # Load JSON file contents
        else:  # If the file is missing, display a warning
            display_message(f"La catégorie {category} n'existe pas.", "warning")
    except Exception as e:
        display_message(f"Erreur lors du chargement des questions: {e}", "error")
    return questions  # Return the loaded questions


# Function to display questions with user's answers and correct answers
def display_questions_reponses(questions, user_answers):
    clear_console()
    display_header("Résultats du QCM")
    global score

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['qst']}")
        for idx, choice in enumerate(q["arrayResponse"]):
            if idx == q["correctResponse"]:  # Met en évidence la bonne réponse en vert
                print(f"\033[92m{idx + 1}. {choice} (Bonne réponse)\033[0m")
            elif i < len(user_answers) and user_answers[i] is not None and user_answers[i] == idx:  
                # Met en évidence la mauvaise réponse de l'utilisateur en rouge
                print(f"\033[91m{idx + 1}. {choice} (Votre réponse)\033[0m")
            else:
                print(f"{idx + 1}. {choice}")

        # Affiche un message pour chaque question
        if i < len(user_answers):
            if user_answers[i] is None:  # Si pas de réponse (timeout)
                display_message("Vous n'avez pas répondu à cette question !!", "warning")
            elif user_answers[i] == q["correctResponse"]:
                display_message("Bonne réponse !", "success")
                score += 1
            else:
                display_message("Mauvaise réponse.", "error")
        else:
            display_message("Vous n'avez pas répondu à cette question !!", "warning")

# Function to ask questions and get user's answers
def ask_questions(questions, chosen_category, duree_max=10):
    clear_console()
    display_header(f"Répondre au QCM - {chosen_category.capitalize()}")
    user_answers = []

    for i, q in enumerate(questions):
        temps_debut = time.time()
        
        print(f"\nQuestion {i + 1}: {q['qst']}")
        for idx, choice in enumerate(q["arrayResponse"], start=1):
            print(f"{idx}. {choice}")
        print("5. Quitter et voir le score")
        
        while True:
            temps_ecoule = time.time() - temps_debut
            temps_restant = duree_max - temps_ecoule
            
            if temps_restant <= 0:
                display_message(f"\nTemps écoulé ! Vous aviez {duree_max} secondes pour répondre.", "warning")
                user_answers.append(None)
                break
            
            if temps_restant <= 10:
                sys.stdout.write(f"\rTemps restant: {int(temps_restant)} secondes!   ")
                sys.stdout.flush()
            
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key in ['1', '2', '3', '4', '5']:
                    answer = int(key)
                    if answer == 5:
                        display_message("Vous avez choisi de quitter le quiz.", "info")
                        return user_answers
                    elif 1 <= answer <= 4:
                        user_answers.append(answer - 1)
                        print(f"\nVous avez choisi: {answer}")
                        break
            
            time.sleep(0.1)

    return user_answers


# Function to take the quiz
# Modifiez la fonction take_quiz pour réinitialiser le score
def take_quiz(username):
    clear_console()
    display_header("Choisissez une catégorie")
    display_categories()

    global score
    score = 0  # Réinitialiser le score au début de chaque quiz

    # Get category choice
    while True:
        try:
            category_choice = int(input("Votre choix de catégorie (1-8): "))
            if 1 <= category_choice <= 8:
                categories = [
                    "basics",
                    "data_structures",
                    "control_flow",
                    "file_handling",
                    "functions",
                    "oop",
                    "exceptions",
                    "modules_libraries"
                ]
                global chosen_category 
                chosen_category = categories[category_choice - 1]
                break
            else:
                display_message("Veuillez entrer un nombre entre 1 et 8.", "warning")
        except ValueError:
            display_message("Entrée invalide. Essayez encore.", "error")

    global questions 
    questions = load_questions_by_category(chosen_category)
    if not questions:
        display_message(f"Aucune question disponible pour la catégorie {chosen_category}.", "error")
        return

    global user_answers
    user_answers = ask_questions(questions, chosen_category)
    display_questions_reponses(questions, user_answers)
    if chosen_category != "":
        ajouter_historique(username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), score, chosen_category)

# Vérifie si le nom contient uniquement des lettres et des espaces
def is_valid_username(username):
    return username and username.replace(" ", "").isalpha()

def main():
    clear_console()
    display_header("Application QCM")
    typewriter_effect("Bienvenue dans l'application QCM...", 0.07)
    
    # Boucle de validation du nom d'utilisateur
    while True:
        username = input("Veuillez entrer votre nom: ").strip()
        if not username:
            display_message("Le nom ne peut pas être vide.", "error")
        elif not is_valid_username(username):
            display_message("Le nom doit contenir uniquement des lettres.", "error")
        else:
            break
    
    while True:
        clear_console()
        display_header(f"Bienvenue, {username}")
        display_menu()
        try:
            choice = int(input("Votre choix: "))
            if choice == 1:
                take_quiz(username)
            elif choice == 2:
                view_scores(username)
            elif choice == 3:
                display_message(f"Votre score: {score}/{len(questions)}", "info")
                display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                break
            else:
                display_message("Choix invalide. Essayez encore.", "warning")
        except ValueError:
            display_message("Entrée invalide. Veuillez entrer un nombre.", "error")
        input("\nAppuyez sur Entrée pour continuer...")
if __name__ == "__main__":
    main()  # Entry point for the program
