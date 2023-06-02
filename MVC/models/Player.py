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

    def create_players_list(self, player):
        self.players_list.append(player)
        print("qqqqqqqqq")
        print(self.players_list)
        return self.players_list


class Player:
    """Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    Création Ajout de joueur, fin d'ajout de joueur"""

    def __init__(self, player):
        # Ajouter validation données et contrôle unicité
        self.idJoueur = player[0]  # ne fonctionne pas
        self.name = player[1]  # self.valid_nom()
        # self.forename = player[2]  # self.valid_prenom()
        # self.fullname = f"{self.forename} {self.name}"
        # self.birthday = player[3]  # self.valid_birthday()

        self.score = 0

    def valid_id(self):
        pattern = r"^[A-z]{2}\d{5}$"
        idExist = Players_Manager().check_id_unicity()
        running = True
        while running:
            IdJoueur = str.upper(input("Identifiant Nat. du joueur :"))
            print(IdJoueur)
            try:
                if re.search(pattern, IdJoueur):
                    if IdJoueur in idExist:
                        raise ValueError("Identifiant déjà enregistré")
                    Players_Manager().add_id_player(IdJoueur)
                    print("Identifiant conforme")
                    running = False
                    return IdJoueur
                else:
                    raise ValueError("Identifiant incorrect")
            except ValueError as error:
                print("Erreur :", error)

        # print(Players_Manager().check_id_unicity())
        # Players_Manager().add_id_player("HB89756")
        # print(Players_Manager().check_id_unicity())

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

    def valid_prenom(self):
        pattern = r"^[A-z]+[ -][A-z]+$"
        pattern2 = r"^[A-z]+$"
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

    # après validation envoyer joueur dans Class Tournoi
    def update_score(self, game_result):  # game_result => tuple (id_joueur, point)
        self.score += game_result[1]

    def player_profile(self):
        return {
            "id_nat": self.idJoueur,
            # "nom complet": self.fullname
            # "date de naissance": self.birthday,
            # "score": self.score,
        }

    def shorted_player_profile(self):
        return (self.idJoueur, self.score)

    def set_score_to_zero(self):
        self.score = 0


# J1 = Joueur()
# print(J1.nom_complet)
# print(J1.score)
# J1.set_to_zero()
# print(J1.score)
# # print(f"print nom{J1.nom}")
# resultat = ("IDHHD", 3)
# J1.update_score(resultat)
# resultat2 = ("IDHHD", 3)
# J1.update_score(resultat2)
# print(J1.score)

