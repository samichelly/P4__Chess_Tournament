class Player:
    def __init__(self, about_player):
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
        """set score to 0 (not used)"""
        self.score = 0
