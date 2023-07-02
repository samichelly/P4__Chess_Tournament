import database


class Players_Manager:
    def __init__(self):
        self.idExist = ["FF78420"]
        self.players_list = []
        # self.id_db = self.check_id_db(id_to_check)

    def add_id_player(self, idplayer):
        self.idExist.append(idplayer)

    def check_id_unicity(self, players_loaded):
        test_id = []
        for i in players_loaded["playertable"]:
            test_id.extend(i.keys())
        return test_id
        # if id_to_check in test_id:
        #     return False


# id = "TF52895"
# test = Players_Manager().check_id_db(id)
# print("test")
# id = "TF52892"
# test = Players_Manager().check_id_db(id)
# # print(test)


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
