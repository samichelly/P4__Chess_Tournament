import re

from Player import Players_Manager


class Player_View:
    def __init__(self, manager):
        self.id_player = self.valid_id(manager)
        self.name = self.valid_name()
        # self.forename = self.valid_forename()
        # self.birthday = self.valid_birthday()

    def valid_id(self, manager):
        pattern = r"^[A-Za-z]{2}\d{5}$"
        id_exist = manager.check_id_unicity()
        running = True
        while running:
            id_player = str.upper(input("Identifiant Nat. du joueur :"))
            print(id_player)
            try:
                if re.search(pattern, id_player):
                    if id_player in id_exist:
                        raise ValueError("Identifiant déjà enregistré")
                    manager.add_id_player(id_player)
                    print(manager.check_id_unicity())
                    print("Identifiant conforme")
                    running = False
                    return id_player
                else:
                    raise ValueError("Identifiant incorrect")
            except ValueError as error:
                print("Erreur :", error)

    def valid_name(self):
        pattern = r"^[A-Za-z]+[ -][A-Za-z]+$"
        pattern2 = r"^[A-Za-z]+$"
        running = True
        while running:
            name = str.upper(input("Nom :"))
            try:
                if re.search(pattern, name) or re.search(pattern2, name):
                    print("Entrée conforme")
                    running = False
                    return name
                else:
                    raise ValueError("Entrée non conforme")
            except ValueError as error:
                print("Erreur :", error)

    def valid_forename(self):
        pattern = r"^[A-Za-z]+[ -][A-Za-z]+$"
        pattern2 = r"^[A-Za-z]+$"
        running = True
        while running:
            surname = str.upper(input("Prénom :"))
            try:
                if re.search(pattern, surname) or re.search(pattern2, surname):
                    print("Entrée conforme")
                    running = False
                    return surname
                else:
                    raise ValueError("Entrée non conforme")
            except ValueError as error:
                print("Erreur :", error)

    def valid_birthday(self):
        pattern = r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        running = True
        while running:
            birthday = str.upper(input("Date de naissance (JJ/MM/AAAA) :"))
            try:
                if re.search(pattern, birthday):
                    print("Entrée conforme")
                    running = False
                    return birthday
                else:
                    raise ValueError("Entrée non conforme")
            except ValueError as error:
                print("Erreur :", error)

    def create_profile_player(self):
        return [self.id_player, self.name]#, self.forename, self.birthday]

