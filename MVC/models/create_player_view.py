import re


class Create_Player_View:
    def __init__(self, manager):
        if manager is None:
            self.idplayer = self._valid_id_without_manager()
        else:
            self.idplayer = self._valid_id(manager)
        self.name = self._valid_name()
        self.forename = self._valid_forename()
        self.birthday = self._valid_birthday()
        self.score = 0
        self.rank = 0

    def _valid_id(self, manager):
        pattern = r"^[A-Za-z]{2}\d{5}$"
        while True:
            id_player = str.upper(input("\nIdentifiant Nat. du joueur : "))
            if re.search(pattern, id_player):
                if id_player in manager.check_id_unicity():
                    print("Identifiant déjà enregistré")
                    # récupérer le joueurs depuis le JSON, à faire dans le controleur
                else:
                    manager.add_id_player(id_player)
                    False
                    return id_player
            else:
                print("Erreur : Identifiant incorrect")

    def _valid_id_without_manager(self):
        pattern = r"^[A-Za-z]{2}\d{5}$"
        while True:
            id_player = str.upper(input("\nIdentifiant Nat. du joueur : "))
            if re.search(pattern, id_player):
                False
                return id_player
            else:
                print("Erreur : Identifiant incorrect")

    def _valid_name(self):
        pattern = r"(^[A-Za-z]+[ -][A-Za-z]+$)|(^[A-Za-z]+$)"
        while True:
            name = str.upper(input("Nom : "))
            if re.search(pattern, name):
                False
                return name
            else:
                print("Erreur : Entrée non conforme")

    def _valid_forename(self):
        pattern = r"(^[A-Za-z]+[ -][A-Za-z]+$)|(^[A-Za-z]+$)"
        while True:
            surname = str.upper(input("Prénom : "))
            if re.search(pattern, surname):
                False
                return surname
            else:
                print("Erreur : Entrée non conforme")

    def _valid_birthday(self):
        pattern = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        while True:
            birthday = str.upper(input("Date de naissance (JJ/MM/AAAA) : "))
            if re.search(pattern, birthday):
                False
                return birthday
            else:
                print("Erreur : Entrée non conforme")

    def create_profile_player(self):
        return {
            "idplayer": self.idplayer,
            "name": self.name,
            "forename": self.forename,
            "birthday": self.birthday,
            "score": self.score,
            "rank": self.rank,
        }
