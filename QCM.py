import os
import sys
import time
import json
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
    print(f"{types.get(type, '[INFO]')} {message}")

def typewriter_effect(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Load questions from the `QST` directory based on the chosen category
def load_questions_by_category(category, directory="QST"):
    questions = []  # Initialize an empty list to store questions
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

user_scores = {}  # Dictionary to store user scores

# Main Functions
def display_menu():
    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Répondre à un QCM")
    print("2. Voir l'historique des scores")
    print("3. Quitter")
    print("-" * 20)

# Function to display categories
def display_categories():
    categories = [
        "1. basics",
        "2. datastructure",
        "3. control_flow",
        "4. functions",
        "5. file_handling",
        "6. oop",
        "7. exceptions",
        "8. modules_libraries"
    ]
    print("\nCHOISISSEZ UNE CATÉGORIE")
    print("-" * 20)
    for category in categories:
        print(category)
    print("-" * 20)


# Function to take the quiz
def take_quiz(username):
    clear_console()
    display_header("Choisissez une catégorie")
    display_categories()

    # Get category choice
    while True:
        try:
            category_choice = int(input("Votre choix de catégorie (1-8): "))
            if 1 <= category_choice <= 8:
                categories = [
                    "basics",
                    "datastructure",
                    "debugging",
                    "file_handling",
                    "functions",
                    "oop",
                    "recursion",
                    "modules_libraries"
                ]
                chosen_category = categories[category_choice - 1]  # Map choice to category name
                break
            else:
                display_message("Veuillez entrer un nombre entre 1 et 8.", "warning")
        except ValueError:
            display_message("Entrée invalide. Essayez encore.", "error")

    # Load questions for the chosen category
    questions = load_questions_by_category(chosen_category)
    if not questions:  # If no questions are available, return to the menu
        display_message(f"Aucune question disponible pour la catégorie {chosen_category}.", "error")
        return

    score = 0
    clear_console()
    display_header(f"Répondre au QCM - {chosen_category.capitalize()}")
    for i, q in enumerate(questions):  # Iterate through the list of questions
        print(f"\nQuestion {i + 1}: {q['qst']}")  # Display question text
        for idx, choice in enumerate(q["arrayResponse"], start=1):  # Display answer choices
            print(f"{idx}. {choice}")
        print("5. Quitter et voir le score")  # Allow the user to quit the quiz

        while True:
            try:
                answer = int(input("Votre réponse (1-5): "))
                if 1 <= answer <= 4:  # Check if answer is a valid choice
                    break
                if answer == 5:  # Quit the quiz and display score
                    display_message(f"Votre score: {score}/{len(questions)}", "info")
                    display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                    sys.exit()  # Exit the program
                else:
                    display_message("Veuillez entrer un nombre entre 1 et 5.", "warning")
            except ValueError:
                display_message("Entrée invalide. Essayez encore.", "error")

        if answer - 1 == q["correctResponse"]:  # Check if the answer is correct
            display_message("Bonne réponse !", "success")
            score += 1  # Increment score for a correct answer
        else:
            display_message("Mauvaise réponse.", "error")
    
    display_message(f"Votre score: {score}/{len(questions)}", "info")
    if username in user_scores:  # Check if the user already exists in the scores
        user_scores[username].append({"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    else:  # If user is new, create an entry in the scores
        user_scores[username] = [{"score": score, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]

# Function to view user's score history
def view_scores(username):
    clear_console()
    display_header("Historique des Scores")
    if username in user_scores:  # Check if the user has scores stored
        for i, entry in enumerate(user_scores[username]):  # Display each score entry
            print(f"{i + 1}. Score: {entry['score']} - Date: {entry['date']}")
    else:
        display_message("Aucun historique trouvé.", "info")

# Main function to control the application flow
def main():
    clear_console()
    display_header("Application QCM")
    typewriter_effect("Bienvenue dans l'application QCM...", 0.07)
    
    username = input("Veuillez entrer votre nom: ").strip()  # Get the user's name
    while True:
        clear_console()
        display_header(f"Bienvenue, {username}")
        display_menu()
        try:
            choice = int(input("Votre choix: "))
            if choice == 1:
                take_quiz(username)  # Pass username to the quiz function
            elif choice == 2:
                view_scores(username)  # Show user's score history
            elif choice == 3:
                display_message("Merci d'avoir utilisé l'application ! À bientôt.", "success")
                break  # Exit the main loop
            else:
                display_message("Choix invalide. Essayez encore.", "warning")
        except ValueError:
            display_message("Entrée invalide. Veuillez entrer un nombre.", "error")
        input("\nAppuyez sur Entrée pour continuer...")  # Wait for user input to proceed


if __name__ == "__main__":
    main()  # Entry point for the program
