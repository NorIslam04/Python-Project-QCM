import threading


def chronometrer_questions(duree_max: int, fonction: callable, *args, **kwargs) -> None:

    def wrapper():
        wrapper.result = fonction(*args, **kwargs)
    
    # Initialiser un thread pour la fonction cible
    wrapper.result = None
    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout=duree_max)
    
    # Vérifier si le temps est écoulé
    if thread.is_alive():
        print(f"Temps écoulé ! Vous aviez {duree_max} secondes pour répondre.")
        thread._stop()
        #next_question()
    else:
        return wrapper.result

import time

def poser_question():
    """Simule une question demandant une réponse."""
    reponse = input("Quel est le type de données en Python pour représenter du texte ?\n")
    return reponse.lower() == "str"

# Utilisation de la fonction avec une limite de temps de 5 secondes
resultat = chronometrer_questions(5, poser_question)
if resultat is not None:
    print("Bonne réponse !" if resultat else "Mauvaise réponse.")
