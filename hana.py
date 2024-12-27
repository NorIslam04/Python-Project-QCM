import os
import json
import csv
from datetime import datetime

class Historique:
     
     DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
#........................................initialiser les attributs de l'historique à 0...............................................
     def __init__(self, username: str) :
        self.username = username
        self.date = datetime.now().strftime(self.DATE_FORMAT)
        self.scores = {
             "basics": 0,
             "datastructure": 0,
             "control_flow": 0,
             "functions": 0,
             "file_handling": 0,
             "oop": 0,
             "exceptions": 0,
             "modules_libraries": 0,
         }
        
#...........................................mettre à jour le score pour une catégorie donnée.........................................   
    
     def mettre_a_jour_scores(self, user_scores: dict):
         #Met à jour les scores de toutes les catégories automatiquement
         for categorie, score in user_scores.items():
             if categorie in self.scores:
                 self.scores[categorie] = score


#..........................................calculer le score d'une catégorie en fonction des bonnes réponses............................
    
     def calculer_score_categorie(self, bonnes_reponses: int, total_questions: int):
         POINT = 1  # Chaque question vaut 1 point
         if total_questions == 0:
             return 0
         return f"{bonnes_reponses * POINT}/5"
     

#.......................................calcule la somme des scores de toutes les catégories (somme total)..............................
     def somme(self) -> int: 
         return sum(self.scores.values())


#.......................................convertir les données de l'historique en dictionnaire...........................................  
     def to_dict(self) -> dict:
        return {
             "name_player": self.username,
             "date": self.date,
             "scores": self.scores,
             "total_score": self.somme(),
        }

# ..................................Fonction pour afficher l'historique........................................................................
     def afficher_historique(self) -> str:
        
         historique = f"Historique de {self.username} - {self.date}\n"
         historique += "Scores par catégorie :\n"
         for categorie, score in self.scores.items():
             historique += f"  {categorie}: {score}\n"
         historique += f"Score total : {self.somme()}\n"
         return historique  
    
# ..................................Fonction pour sauvegarder  l'historique dans un fichier CSV...............................................
     def save_to_csv(self, filename: str = "resultats.csv") -> None:
        # Créer un fichier CSV et ajouter les données de l'historique
      
         file_exists = os.path.isfile(filename)
         with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
             fieldnames = ["name_player", "date", "scores", "total_score"]
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

             if not file_exists:
                 writer.writeheader()

             writer.writerow(self.to_dict())
             print("Historique enregistré avec succès dans le fichier CSV")

   