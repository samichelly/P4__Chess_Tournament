import re

# from view import Tournament
# from controller import DateTime


class Gestionnaire_Joueur:
    def __init__(self):
        self.IdExist = []

    def add_id_player(self, idplayer):
        self.IdExist.append(idplayer)
        print(self.IdExist)

    def check_id_unicity(self):
        return self.IdExist


# faire à nouveau les tests sur Gestionnaire_Joueur


class Joueur:
    """Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    Création Ajout de joueur, fin d'ajout de joueur"""

    def __init__(self, idJoueur=None, nom=None, prenom=None, dateDeNaissance=None):
        # Ajouter validation données et contrôle unicité
        self.idJoueur = self.valid_id()  # ne fonctionne pas
        self.nom = self.valid_nom()
        self.prenom = self.valid_prenom()
        self.nom_complet = f"{self.prenom} {self.nom}"
        self.dateDeNaissance = self.valid_birthday()
        self.score = 10

    def valid_id(self):
        pattern = r"^[A-z]{2}\d{5}$"
        idExist = Gestionnaire_Joueur().check_id_unicity()
        running = True
        while running:
            IdJoueur = str.upper(input("Identifiant Nat. du joueur :"))
            print(IdJoueur)
            try:
                if re.search(pattern, IdJoueur):
                    if IdJoueur in idExist:
                        raise ValueError("Identifiant déjà enregistré")
                    Gestionnaire_Joueur().add_id_player(IdJoueur)
                    print("Identifiant conforme")
                    running = False
                    return IdJoueur
                else:
                    raise ValueError("Identifiant incorrect")
            except ValueError as error:
                print("Erreur :", error)

        # print(Gestionnaire_Joueur().check_id_unicity())
        # Gestionnaire_Joueur().add_id_player("HB89756")
        # print(Gestionnaire_Joueur().check_id_unicity())

    def valid_nom(self):
        pattern = r"^[A-z]+[ -][A-z]+$"
        pattern2 = r"^[A-z]+$"
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

    def profile_player(self):
        profile = {
            "id_nat": self.idJoueur,
            "nom complet": self.nom_complet,
            "date de naissance": self.dateDeNaissance,
            "score": self.score,
        }
        print(profile)

    def set_to_zero(self):
        self.score = 0


J1 = Joueur()
print(J1.nom_complet)
print(J1.score)
J1.set_to_zero()
print(J1.score)
# # print(f"print nom{J1.nom}")
# resultat = ("IDHHD", 3)
# J1.update_score(resultat)
# resultat2 = ("IDHHD", 3)
# J1.update_score(resultat2)
# print(J1.score)


# J1 = Joueur("77777", "UUU", "HHH", "")
# print(J1.nom_tt("UUU", "HHH"))
# print(J1._IdJoueur)
# ajouter les property
