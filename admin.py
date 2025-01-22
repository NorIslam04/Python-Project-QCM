import json
import os
from display import clear_console, display_header, display_message, display_categories

def admin_menu():
    print("\nADMIN MENU")
    print("-" * 20)
    print("1. Répondre à un QCM")
    print("2. Voir l'historique des scores")
    print("3. Voir mes réponses détaillées")
    print("4. Gérer les questions")
    print("5. Quitter")
    print("-" * 20)

def question_management_menu():
    print("\nGESTION DES QUESTIONS")
    print("-" * 20)
    print("1. Ajouter une question")
    print("2. Modifier une question")
    print("3. Supprimer une question")
    print("4. Retour")
    print("-" * 20)

def get_category_choice():
    clear_console()
    display_header("Choisissez une catégorie")
    display_categories()
    categories = ["basics", "data_structures", "control_flow", "file_handling", 
                 "functions", "oop", "exceptions", "modules_libraries"]
    
    while True:
        try:
            choice = int(input("Votre choix (1-8): "))
            if 1 <= choice <= 8:
                return categories[choice - 1]
            display_message("Veuillez entrer un nombre entre 1 et 8.", "warning")
        except ValueError:
            display_message("Entrée invalide.", "error")

def load_questions(category):
    filepath = os.path.join("QST", f"{category}.json")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_questions(category, questions):
    filepath = os.path.join("QST", f"{category}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)

def add_question(category):
    question = {
        "qst": input("Question: "),
        "arrayResponse": [
            input(f"Réponse {i+1}: ") for i in range(4)
        ],
        "correctResponse": None
    }
    
    while True:
        try:
            correct = int(input("Numéro de la bonne réponse (1-4): ")) - 1
            if 0 <= correct <= 3:
                question["correctResponse"] = correct
                break
            display_message("Veuillez entrer un nombre entre 1 et 4.", "warning")
        except ValueError:
            display_message("Entrée invalide.", "error")
    
    questions = load_questions(category)
    questions.append(question)
    save_questions(category, questions)
    display_message("Question ajoutée avec succès!", "success")

def update_question(category):
    questions = load_questions(category)
    if not questions:
        display_message("Aucune question trouvée.", "warning")
        return
    
    print("\nQuestions disponibles:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['qst']}")
    
    try:
        idx = int(input("\nChoisir le numéro de la question à modifier: ")) - 1
        if 0 <= idx < len(questions):
            questions[idx]["qst"] = input("Nouvelle question: ")
            for i in range(4):
                questions[idx]["arrayResponse"][i] = input(f"Nouvelle réponse {i+1}: ")
            while True:
                try:
                    correct = int(input("Numéro de la bonne réponse (1-4): ")) - 1
                    if 0 <= correct <= 3:
                        questions[idx]["correctResponse"] = correct
                        break
                except ValueError:
                    display_message("Entrée invalide.", "error")
            save_questions(category, questions)
            display_message("Question modifiée avec succès!", "success")
        else:
            display_message("Numéro de question invalide.", "error")
    except ValueError:
        display_message("Entrée invalide.", "error")

def delete_question(category):
    questions = load_questions(category)
    if not questions:
        display_message("Aucune question trouvée.", "warning")
        return
    
    print("\nQuestions disponibles:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q['qst']}")
    
    try:
        idx = int(input("\nChoisir le numéro de la question à supprimer: ")) - 1
        if 0 <= idx < len(questions):
            questions.pop(idx)
            save_questions(category, questions)
            display_message("Question supprimée avec succès!", "success")
        else:
            display_message("Numéro de question invalide.", "error")
    except ValueError:
        display_message("Entrée invalide.", "error")

def manage_questions():
    while True:
        clear_console()
        display_header("Gestion des Questions")
        question_management_menu()
        try:
            choice = int(input("Votre choix: "))
            if choice == 4:
                break
            if 1 <= choice <= 3:
                category = get_category_choice()
                if choice == 1:
                    add_question(category)
                elif choice == 2:
                    update_question(category)
                else:
                    delete_question(category)
            else:
                display_message("Choix invalide.", "warning")
        except ValueError:
            display_message("Entrée invalide.", "error")
        input("\nAppuyez sur Entrée pour continuer...")

def verify_admin():
    password = input("Mot de passe admin: ")
    return password == "admin123"