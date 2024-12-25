import json

with open("Questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

# Afficher les questions
for question in questions:
    print(f"Question: {question['qst']}")
    for idx, response in enumerate(question["arrayResponse"]):
        print(f"{idx+1}: {response}")
    print(f"Réponse correcte: {question['arrayResponse'][question['correctResponse']]}")
    print(f"Catégorie: {question['categorie']}\n")
