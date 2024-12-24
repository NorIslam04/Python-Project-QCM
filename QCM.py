import os
import sys
import time
from datetime import datetime

# Utilities for display
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def display_message(message, type):
    types = {
        "info": "\033[94m[INFO]\033[0m",
        "success": "\033[92m[SUCCESS]\033[0m",
        "error": "\033[91m[ERROR]\033[0m",
        "warning": "\033[93m[WARNING]\033[0m",
    }
    print(f"{types.get(type, '[INFO]')} {message}")#si le type n'est pas trouvé, afficher [INFO]

def typewriter_effect(text, delay):#effet machine à écrire
    for char in text:
        sys.stdout.write(char)#affiche le caractère
        sys.stdout.flush()#vide le tampon de sortie
        time.sleep(delay)#délai entre chaque caractère
    print()#saut de ligne

    current_user="user_name" #input
    array_current_res=[] #.append() <- input
    current_category="category" #input

# QCM Data
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Madrid", "5. Quitter et voir le score"],
        "correct": 1
    },
    {
        "question": "Quel est le langage de programmation utilisé pour Django ?",
        "choices": ["1. Java", "2. Python", "3. C#", "4. Ruby", "5. Quitter et voir le score"],
        "correct": 2
    },
    {
        "question": "Combien de continents y a-t-il dans le monde ?",
        "choices": ["1. 5", "2. 6", "3. 7", "4. 8", "5. Quitter et voir le score"],
        "correct": 3
    },
    {
        "question": "Quelle est la couleur du ciel ?",
        "choices": ["1. Rouge", "2. Vert", "3. Jaune", "4. Bleu", "5. Quitter et voir le score"],
        "correct": 4
    },
    {
        "question": "Quelle est la capitale de l'Espagne ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Madrid", "5. Quitter et voir le score"],
        "correct": 4
    },
    {
        "question": "Quel est le résultat de 2 + 2 ?",
        "choices": ["1. 3", "2. 4", "3. 5", "4. 6", "5. Quitter et voir le score"],
        "correct": 2
    },
    {
        "question": "Quelle est la capitale de l'Allemagne ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Madrid", "5. Quitter et voir le score"],
        "correct": 3
    },
    {
        "question": "Quelle est la capitale du Royaume-Uni ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Madrid", "5. Quitter et voir le score"],
        "correct": 2
    },
    {
        "question": "Quelle est la capitale de l'Italie ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Rome", "5. Quitter et voir le score"],
        "correct": 4
    },
    {
        "question": "Quelle est la capitale du Japon ?",
        "choices": ["1. Paris", "2. Tokyo", "3. Berlin", "4. Madrid", "5. Quitter et voir le score"],
        "correct": 2
    }
]

user_scores = {}

# Main Functions
def display_menu():
    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Répondre à un QCM")
    print("2. Voir l'historique des scores")
    print("3. Quitter")
    print("-" * 20)

def take_quiz(username):
    score = 0
    clear_console()
    display_header("Répondre au QCM")
    for i, q in enumerate(questions):# i:nombre de question, q:question
        print(f"\nQuestion {i + 1}: {q['question']}")
        for choice in q["choices"]:#affiche tous les choix
            print(choice)
        while True:
            try:
                answer = int(input("Votre réponse (1-5): "))
                if 1 <= answer <= 4:
                    break
                if answer == 5:
                    display_message(f"Votre score: {score}/{len(questions)}", "info")
                    display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                    sys.exit()
                else:#traitement de l'erreur si la réponse n'est pas entre 1 et 5
                    display_message("Veuillez entrer un nombre entre 1 et 5.", "warning")
            except ValueError:#traitement de l'erreur si la réponse n'est pas un nombre
                display_message("Entrée invalide. Essayez encore.", "error")

        if answer == q["correct"]:
            display_message("Bonne réponse !", "success")
            score += 1
        else:
            display_message("Mauvaise réponse.", "error")
    
    display_message(f"Votre score: {score}/{len(questions)}", "info")
    # a la fin du QCM, on enregistre le score dans un fichier CSV
    if username in user_scores:#si l'utilisateur existe déjà
        # save output to a file CSV "existe user"
        user_scores[username].append({"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    else: # save output to a file CSV "nouveau user"
        user_scores[username] = [{"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

def view_scores(username):
    clear_console()
    display_header("Historique des Scores")
    if username in user_scores:
        for i, entry in enumerate(user_scores[username]):#i:nombre de score, entry:score
            print(f"{i + 1}. Score: {entry['score']}/{len(questions)} - Date: {entry['date']}")
    else:
        display_message("Aucun historique trouvé.", "info")

def main():
    clear_console()
    display_header("Application QCM")
    typewriter_effect("Bienvenue dans l'application QCM...",0.07)
    
    username = input("Veuillez entrer votre nom: ").strip()
    while True:
        clear_console()
        display_header(f"Bienvenue, {username}")
        display_menu()
        try:#traitement de l'erreur si le choix n'est pas un nombre
            choice = int(input("Votre choix: "))
            if choice == 1:
                take_quiz(username)
            elif choice == 2:
                view_scores(username)
            elif choice == 3:
                display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                break
            else:
                display_message("Choix invalide. Essayez encore.", "warning")
        except ValueError:
            display_message("Entrée invalide. Veuillez entrer un nombre.", "error")
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
