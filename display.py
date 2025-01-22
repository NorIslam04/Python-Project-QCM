import os
import sys
import time

def display_menu():
    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Répondre à un QCM")
    print("2. Voir l'historique des scores")
    print("3. Voir mes réponses détaillées")  # Nouvelle option
    print("4. changer de compte")
    print("5. Quitter")
    print("-" * 20)

# Function to display categories
def display_categories():
    categories = [
        "1. basics",
        "2. data_structures",
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


def display_header(title):
    print("=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

# Function to display messages with different colors and types
def display_message(message, type):
    types = {
        "info": "\033[94m[INFO]\033[0m",
        "success": "\033[92m[SUCCESS]\033[0m",
        "error": "\033[91m[ERROR]\033[0m",
        "warning": "\033[93m[WARNING]\033[0m",
    }
    print(f"\n{types.get(type, '[INFO]')} {message}")

# Function to simulate a typewriter effect
def typewriter_effect(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Utilities for display
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')