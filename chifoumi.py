# Importer la bibliothèque random
import random

# Définir une fonction pour obtenir un choix aléatoire
def get_random_choice():
    choices = ["pierre", "feuille", "ciseaux"]
    return random.choice(choices)

# Définir une fonction pour jouer au jeu de Pierre-Feuille-Ciseaux
def play_rock_paper_scissors():
    while True:
        # Obtenir le choix aléatoire de l'ordinateur
        computer_choice = get_random_choice()

        # Demander à l'utilisateur de faire un choix
        user_choice = input("Entrez votre choix (pierre, feuille ou ciseaux) : ").lower()

        # Vérifier qui a gagné
        if user_choice == computer_choice:
            print("Égalité !")
        elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
             (user_choice == "feuille" and computer_choice == "pierre") or \
             (user_choice == "ciseaux" and computer_choice == "feuille"):
            print("Vous avez gagné !")
        else:
            print("L'ordinateur a gagné !")

        # Demander à l'utilisateur s'il veut rejouer
        replay = input("Voulez-vous rejouer ? (oui/non) : ").lower()
        if replay != "oui":
            print("Merci d'avoir joué !")
            break

# Jouer au jeu de Pierre-Feuille-Ciseaux
play_rock_paper_scissors()