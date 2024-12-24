import csv

def lire_fichier_csv(fichier: str) -> list[dict]:
    donnees = []
    try:
        with open(fichier, mode="r", encoding="utf-8") as file:
            lecteur = csv.DictReader(file)  # Crée un lecteur pour le CSV
            for ligne in lecteur:
                donnees.append(ligne)  # Ajoute chaque ligne sous forme de dictionnaire
        print(f"Les données ont été lues avec succès depuis {fichier}.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier} est introuvable.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    return donnees


# Lire les données du fichier CSV
chemin_fichier = "resultats.csv"
resultats = lire_fichier_csv(chemin_fichier)

# Afficher les résultats
for resultat in resultats:
    print(resultat)

