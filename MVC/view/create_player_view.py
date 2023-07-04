import re


class Create_Player_View:
    """create player parameters to input in Player Class"""
    def __init__(self, id_exists):
        self.idplayer = self._valid_id(id_exists)
        if self.idplayer is False:
            return None
        self.name = self._valid_name("Nom")
        self.forename = self._valid_name("Prénom")
        self.birthday = self._valid_birthday()
        self.score = 0
        self.rank = 0

    def _valid_id(self, id_exists):
        pattern = r"^[A-Za-z]{2}\d{5}$"
        while True:
            id_player = str.upper(input("\nIdentifiant Nat. du joueur : "))
            if re.search(pattern, id_player):
                try:
                    if id_player not in id_exists:
                        return id_player
                except TypeError:
                    return id_player
                else:
                    print("Identifiant déjà existant")
                    choice = str.upper(
                        input("Quitter l'ajout du joueur ?\nO-oui\nN-Non\nChoix : ")
                    )
                    if choice == "O":
                        return False
            else:
                print("Erreur : Identifiant incorrect")

    def _valid_name(self, nom):
        pattern = r"(^[A-Za-z]+[ -][A-Za-z]+$)|(^[A-Za-z]+$)"
        while True:
            name = str.upper(input(f"{nom} : "))
            if re.search(pattern, name):
                return name
            else:
                print("Erreur : Entrée non conforme")

    def _valid_birthday(self):
        pattern = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        while True:
            birthday = str.upper(input("Date de naissance (JJ/MM/AAAA) : "))
            if re.search(pattern, birthday):
                return birthday
            else:
                print("Erreur : Entrée non conforme")

    def create_profile_player(self):
        if self.idplayer is False:
            return None
        return {
            "idplayer": self.idplayer,
            "name": self.name,
            "forename": self.forename,
            "birthday": self.birthday,
            "score": self.score,
            "rank": self.rank,
        }
