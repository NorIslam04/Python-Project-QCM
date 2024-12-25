import json

# Nouvelles questions à ajouter
nouvelles_questions = [
    {
        "qst": "Que retourne la fonction len(['a', 'b', 'c']) ?",
        "arrayResponse": ["3", "2", "1", "Erreur"],
        "correctResponse": 0,
        "categorie": "structures_de_donnees"
    },
    {
        "qst": "Comment déclarer une fonction en Python ?",
        "arrayResponse": ["function nom():", "def nom():", "declare nom():", "func nom():"],
        "correctResponse": 1,
        "categorie": "bases"
    }
]

# Lire les questions existantes (si le fichier existe)
try:
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
except FileNotFoundError:
    # Si le fichier n'existe pas, on part d'une liste vide
    questions = []

# Ajouter les nouvelles questions
questions.extend(nouvelles_questions)

# Réécrire toutes les questions dans le fichier JSON
with open("questions.json", "w", encoding="utf-8") as file:
    json.dump(questions, file, indent=4, ensure_ascii=False)

print("Les nouvelles questions ont été ajoutées à questions.json")
