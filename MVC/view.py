import pandas as pd

# import models


### VUE ###


# class Joueur:
#     def input_identity_player(self):
#         IdJoueur = input("Entrer l'Identifiant National du joueur :")
#         # Envoyer vers le controlleur pour vérification  / self.valid_id(self.IdJoueur)
#         nomDeFamille = input("Entrer le nom de famille du joueur :")
#         # Envoyer vers le controlleur pour vérification
#         prenom = input("Entrer le prénom du joueur :")
#         # Envoyer vers le controlleur pour vérification
#         dateDeNaissance = input("Entrer la date de naissance du joueur :")
#         # Envoyer vers le controlleur pour vérification
#         # Si tous les inputs OK print
#         print("Création du joueur réussie")


class Tournament:
    def select_tournament(self):
        print("\n1 créer un nouveau tournoi\n2 charger un tournoi")
        return int(input("Choix :"))

    def number_of_round(self):
        nb_round = input("Indiquez le nombre de tour qui compose le tournoi :")
        if nb_round.isnumeric() is False:
            print("Erreur de saisi. Le tournoi sera de 4 tours par défaut")
            return 4
        else:
            print(f"le tournoi sera de {nb_round} tour(s)")
            return nb_round
        # Envoyer vers le controlleur pour vérification

    def about_tournament(self):
        tournament_info = [input("\nEntrez le nom du tournoi : ")]
        tournament_info.append(input("Entrez le lieu : "))
        tournament_info.append(input("Entrez une description : "))
        return tournament_info

    def display_final_ranking(self, dic_joueur):  # get profil des joueurs
        print("\nClassement final :\n")
        # table_head =
        # final_ranking = pd.DataFrame(columns=)

        # create dataframe

    def launch_new_round(self):
        new_round = input("Lancez un nouveau tour ?\n 1 - oui\n 2 - non")
        if new_round == "1":
            # lancer nouveau tour
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
        print("Matchs du tour : ")
