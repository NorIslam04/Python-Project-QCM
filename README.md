# Python-Project-QCM

## Description
Ce projet est une application de questionnaire à choix multiples (QCM) en Python. Les utilisateurs peuvent répondre à des questions, voir leur historique de scores et consulter leurs réponses détaillées.

## Fonctionnalités et Accès

### Répondre à un QCM
1. Lancez l'application et entrez votre nom.
2. Sélectionnez l'option "1. Répondre à un QCM" dans le menu principal.
3. Choisissez une catégorie de questions (1-8).
4. Répondez aux questions dans le temps imparti.

### Voir l'historique des scores
1. Sélectionnez l'option "2. Voir l'historique des scores" dans le menu principal.
2. Votre historique de scores sera affiché.

### Voir les réponses détaillées
1. Sélectionnez l'option "3. Voir mes réponses détaillées" dans le menu principal.
2. Vos réponses détaillées pour chaque QCM seront affichées.

## Fichiers Importants
- `QCM.py`: Point d'entrée principal de l'application.
- `display.py`: Contient les fonctions d'affichage pour le menu, les catégories et les messages.
- `hana.py`: Gère l'ajout de l'historique et l'affichage des réponses détaillées.
- `ramy.py`: Gère l'affichage des scores et la sauvegarde des réponses des utilisateurs.
- `QST/`: Contient les fichiers JSON avec les questions pour chaque catégorie.

## Utilisation

### Prérequis
- Python 3.x doit être installé sur votre machine.

### Installation
1. Clonez le dépôt:
   ```sh
   git clone https://github.com/NorIslam04/Python-Project-QCM/
   cd Python-Project-QCM
   
2. Execution:
   ```sh
   python QCM.py
