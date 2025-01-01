from typing import List

class Question:
    def __init__(self, id: int, qst: str, arrayResponse: List[str], correctResponse: int, categorie: str):
        """
        Initialise une question.

        :param id: Identifiant de la question
        :param qst: Texte de la question
        :param arrayResponse: Liste des options de réponse
        :param correctResponse: Index de la réponse correcte
        :param categorie: Catégorie de la question
        """
        self.id = id
        self.qst = qst
        self.arrayResponse = arrayResponse
        self.correctResponse = correctResponse
        self.categorie = categorie

    def verifier_reponse(self, reponse: int) -> bool:
        """
    

        :param reponse: Index de la réponse donnée par le joueur
        :return: True si la réponse est correcte, False sinon
        """
        return self.correctResponse == reponse

    def afficher_question(self) -> str:
        """
        Retourne la question et les options sous forme de chaîne.

        
        """
        options = "\n".join(f"{i + 1}. {option}" for i, option in enumerate(self.arrayResponse))
        return f"Question: {self.qst}\nOptions:\n{options}"

def charger_questions_depuis_fichier(fichier: str) -> List[Question]:
    """
    Charge des questions depuis un fichier structuré.

    Le fichier doit contenir des lignes avec le format suivant :
    id|texte_question|reponse1,reponse2,reponse3|index_correct|categorie

    :param fichier: Chemin du fichier contenant les questions
    :return: Liste d'objets Question
    """
    questions = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                
                # strip():Lit chaque ligne et supprime les espaces superflus en début et fin  
                elements = ligne.strip().split('|')
                if len(elements) == 5:
                    id = int(elements[0])
                    texte_question = elements[1]
                    arrayResponse = elements[2].split(',')
                    correctResponse = int(elements[3])
                    categorie = elements[4]
                    # Création d'une instance Question et ajout à la liste
                    questions.append(
                        Question(id, texte_question, arrayResponse, correctResponse, categorie)
                    )
    except FileNotFoundError:
        print(f"Erreur : fichier '{fichier}' introuvable.")
    except Exception as e:
        print(f"Erreur lors du chargement des questions : {e}")
    return questions

def filtrer_questions(questions: List[Question], categorie: str) -> List[Question]:
    """
    Retourne les questions d'une catégorie spécifique.

    
    :return: Liste des questions filtrées
    """
    return [q for q in questions if q.categorie == categorie]
