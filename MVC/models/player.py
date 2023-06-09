import re

# from view import Tournament
# from controller import DateTime


class Players_Manager:
    def __init__(self):
        self.idExist = []
        self.players_list = []

    def add_id_player(self, idplayer):
        self.idExist.append(idplayer)

    def check_id_unicity(self):
        print(self.idExist)
        return self.idExist


class Player:
    """Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    Création Ajout de joueur, fin d'ajout de joueur"""

    def __init__(self, player):
        # Ajouter validation données et contrôle unicité
        self.idJoueur = player[0]  # ne fonctionne pas
        # self.name = player[1]  # self.valid_nom()
        # self.forename = player[2]  # self.valid_prenom()
        # self.fullname = f"{self.forename} {self.name}"
        # self.birthday = player[3]  # self.valid_birthday()
        self.score = 0

    def player_profile(self):
        return {
            "id_nat": self.idJoueur,
            # "nom complet": self.fullname
            # "date de naissance": self.birthday,
            # "score": self.score,
        }

    def set_score_to_zero(self):
        self.score = 0
