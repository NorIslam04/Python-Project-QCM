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

def display_message(message, type="info"):
    types = {
        "info": "\033[94m[INFO]\033[0m",
        "success": "\033[92m[SUCCESS]\033[0m",
        "error": "\033[91m[ERROR]\033[0m",
        "warning": "\033[93m[WARNING]\033[0m",
    }
    print(f"{types.get(type, '[INFO]')} {message}")

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# QCM Data
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choices": ["1. Paris", "2. Londres", "3. Berlin", "4. Madrid"],
        "correct": 1
    },
    {
        "question": "Quel est le langage de programmation utilisé pour Django ?",
        "choices": ["1. Java", "2. Python", "3. C#", "4. Ruby"],
        "correct": 2
    },
    {
        "question": "Combien de continents y a-t-il dans le monde ?",
        "choices": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "correct": 3
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
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for choice in q["choices"]:
            print(choice)
        while True:
            try:
                answer = int(input("Votre réponse (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    display_message("Veuillez entrer un nombre entre 1 et 4.", "warning")
            except ValueError:
                display_message("Entrée invalide. Essayez encore.", "error")

        if answer == q["correct"]:
            display_message("Bonne réponse !", "success")
            score += 1
        else:
            display_message("Mauvaise réponse.", "error")
    
    display_message(f"Votre score: {score}/{len(questions)}", "info")
    if username in user_scores:
        user_scores[username].append({"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    else:
        user_scores[username] = [{"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

def view_scores(username):
    clear_console()
    display_header("Historique des Scores")
    if username in user_scores:
        for i, entry in enumerate(user_scores[username]):
            print(f"{i + 1}. Score: {entry['score']}/{len(questions)} - Date: {entry['date']}")
    else:
        display_message("Aucun historique trouvé.", "info")

def main():
    clear_console()
    display_header("Application QCM")
    typewriter_effect("Bienvenue dans l'application QCM...", delay=0.05)
    
    username = input("Veuillez entrer votre nom: ").strip()
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
                display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                break
            else:
                display_message("Choix invalide. Essayez encore.", "warning")
        except ValueError:
            display_message("Entrée invalide. Veuillez entrer un nombre.", "error")
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
