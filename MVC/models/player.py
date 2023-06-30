class Players_Manager:
    def __init__(self):
        self.idExist = ["FF78420"]
        self.players_list = []

    def add_id_player(self, idplayer):
        self.idExist.append(idplayer)

    def check_id_unicity(self):
        # print(self.idExist)
        return self.idExist


class Player:
    """Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    Création Ajout de joueur, fin d'ajout de joueur"""

    def __init__(self, about_player):
        # Ajouter validation données et contrôle unicité
        self.idplayer = about_player["idplayer"]
        self.name = about_player["name"]
        self.forename = about_player["forename"]
        self.fullname = f"{about_player['forename']} {about_player['name']}"
        self.birthday = about_player["birthday"]
        self.score = about_player["score"]
        self.rank = about_player["rank"]

    def __str__(self):
        return (
            f"Profil crée : {self.fullname} ({self.idplayer}), né(e) le {self.birthday}"
        )

    def set_score_to_zero(self):
        self.score = 0
