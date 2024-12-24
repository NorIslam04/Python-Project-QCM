import csv

def ajouter_dans_fichier_csv(fichier: str, elements: list[dict]) -> None:
    try:
        with open(fichier, mode="a", newline="", encoding="utf-8") as file:
            # Créer un écrivain pour le CSV
            if elements:
                writer = csv.DictWriter(file, fieldnames=elements[0].keys())
                
                # Vérifier si le fichier est vide pour ajouter l'en-tête
                file.seek(0, 2)  # Positionner à la fin de fichier (2) pour append
                if file.tell() == 0:  # Si le fichier est vide
                    writer.writeheader()  # Ajouter l'en-tête
                # Ajouter les nouvelles lignes
                writer.writerows(elements)
        print(f"{len(elements)} éléments ont été ajoutés au fichier {fichier}.")
    except Exception as e:
        print(f"Erreur lors de l'ajout dans le fichier : {e}")


# Nouveaux éléments à ajouter
nouvelles_donnees = [
    {"nom": "Charlie", "score": 20, "date": "2024-12-17"},
    {"nom": "Diana", "score": 19, "date": "2024-12-18"}
]

# Ajouter les nouvelles données
ajouter_dans_fichier_csv("resultats.csv", nouvelles_donnees)
