import csv


class Historique:
    def init(self, name: str, date: str, score: int,categorie: str):
        self.name = name
        self.date = date
        self.score = score
        self.categorie = categorie


def ajouter_historique( nom: str, date: str, score: int,categorie: str) -> None:
    # Append the new history entry to the CSV file
    try:
        with open("resultats.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["nom","categorie", "score", "date"])
            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"nom": nom,"categorie":categorie, "score": score, "date": date})
    except Exception as e:
        print(f"Erreur lors de l'ajout dans le fichier CSV : {e}")
