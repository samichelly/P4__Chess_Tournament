# import models
from datetime import date
from datetime import datetime

### VUE ###


class Joueur:
    def input_identity_player(self):
        IdJoueur = input("Entrer l'Identifiant National du joueur :")
        # Envoyer vers le controlleur pour vérification  / self.valid_id(self.IdJoueur)
        nomDeFamille = input("Entrer le nom de famille du joueur :")
        # Envoyer vers le controlleur pour vérification
        prenom = input("Entrer le prénom du joueur :")
        # Envoyer vers le controlleur pour vérification
        dateDeNaissance = input("Entrer la date de naissance du joueur :")
        # Envoyer vers le controlleur pour vérification
        # Si tous les inputs OK print
        print("Création du joueur réussie")


class Tournoi:
    # def create_tournament(self):
    #     choice = input("'1' pour créer un nouveau tournoi :\n '2' pour charger un tournoi")
    #     if choice == 1:
    #         #créer un tournoi
    #     elif choice == 2:
    #         #charger un tournoi
    #     else:
    #         # error

    def number_of_round(self):
        print("Indiquez le nombre de tour qui compose le tournoi :")
        nb_round = int(
            input("Entrez une valeur pour modifier le paramètre par défaut : ")
        )
        if nb_round is False:
            print("Erreur de saisi. Le tournoi sera de 4 tours par défaut")
            return 4
        else:
            print("le tournoi sera de {nb_round} tour(s)")
            return nb_round
        # Envoyer vers le controlleur pour vérification

    def about_tournament():
        tournament_name = input("Entrez le nom du tournoi : ")
        return tournament_name
        tournament_place = input("Entrez le lieu : ")
        return tournament_place

    def display_resultat(self, dic_joueur):  # get profil des joueurs
        print("\nClassement final :\n")
        # create dataframe

    def create_description(self):
        input = "Ajouter une description : "
        return input

    def launch_new_round(self):
        # lancer un nouveau tour
        pass


class Match:
    def game(self):
        # pour chaque paire
        print("Le match : paire[0] VS paire[1]")

    def input_score(self, paire):  # Définir score possible 0, 0.5, 1
        print(
            "Entrer les points acquis par les 2 joueurs au terme de ce tour. Valeurs possibles : 0, 0.5, 1"
        )
        scoreJ1 = input(f"Indiquer le score obtenu par {self.paire[0]} :")
        # Envoyer vers le controlleur pour vérification
        scoreJ2 = input(f"Indiquer le score obtenu par {self.paire[0]} :")
        # Envoyer vers le controlleur pour vérification
        print(
            f"Le joueur {self.paire[0]} a obtenu {scoreJ1} point, le joueur {self.paire[0]} a obtenu {scoreJ2} point"
        )


class Tour:
    def match_list(self):
        print("Matchs du Tour X : ")


class DateTime:
    def get_day(self):
        return date.today().strftime("%d/%m/%Y")

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")


