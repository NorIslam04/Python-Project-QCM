import os
import json
import csv
from datetime import datetime

class Historique:
     
     DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
     #initialiser les attributs de l'historique
     def __init__(self, username: str, categorie: str, time_taken: float, responses: list):
       
        self.username = username
        self.date = datetime.now().strftime(self.DATE_FORMAT)
        self.categorie = categorie
        self.time_taken = time_taken
        self.responses = responses
        correct_responses = (1 for r in self.responses if r.get("correct", False))#compter les bonnes réponses
        self.score = sum(correct_responses)

      #convertir les données de l'historique en dictionnaire  
     def to_dict(self) -> dict:
        return {
            "name_player": self.username,
            "date": self.date,
            "categorie": self.categorie,
            "score": self.score,
            "time_taken": self.time_taken,
        }
# ..................................Fonction pour sauvegarder  l'historique dans un fichier CSV...............................................
     def save_to_csv(self, filename: str = "resultats.csv") -> None:
        # Créer un fichier CSV et ajouter les données de l'historique
        data = {
            "nom": self.username,
            "score": f"{self.score}",
            "categorie": self.categorie,
            "date": self.date,
            "temps": f"{self.time_taken:.1f}s"
        }#créer un dictionnaire avec les données de l'historique
        
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:#si le fichier n'existe pas, on ajoute l'entête
                writer.writeheader()
            writer.writerow(data)#ajouter les données de l'historique dans le fichier CSV
        print("Historique sauvegardé avec succès dans le fichier CSV.")
    
# ..................................Fonction pour sauvegarder  l'historique dans un fichier JSON...............................................
     def save_to_json(self, filename: str = "historique.json") -> None:
       
        try:
            if os.path.exists(filename):#si le fichier existe, on le charge
                with open(filename, 'r', encoding='utf-8') as file:
                    historique = json.load(file)
            else:#si le fichier n'existe pas, on crée un nouveau fichier
                historique = []
            
            historique.append(self.to_dict())#ajouter les données de l'historique dans la liste historique
            
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(historique, file, indent=4, ensure_ascii=False)
        except Exception as e:#si une erreur survient lors de la sauvegarde
            print(f"Erreur lors de la sauvegarde dans le JSON: {e}")
        else:
            print("Historique sauvegardé avec succès dans le fichier JSON.")

     