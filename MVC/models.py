import random
# from view import Tournament
from controller import DateTime

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -"


class Gestionnaire_Joueur:
    def __init__(self):
        self.IdExistant = []

    def add_id_player(self, idplayer):
        self.IdExistant.append(idplayer)
        # print(self.IdExistant)

    def check_id_unicity(self):
        # print(self.IdExistant)
        # print("PI")
        return self.IdExistant


# jj = Gestionnaire_Joueur()
# print(jj.check_id_unicity())
# print(jj.add_id_player("JHBi"))
# print(jj.check_id_unicity())
# print(jj.add_id_player("HV"))
# print(jj.check_id_unicity())


class Joueur:
    """Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    Création Ajout de joueur, fin d'ajout de joueur"""

    def __init__(self, idJoueur=None, nom=None, prenom=None, dateDeNaissance=None):
        # Ajouter validation données et contrôle unicité
        self.idJoueur = self.valid_id()  # ne fonctionne pas
        self.nom = self.valid_nom()
        self.prenom = self.valid_prenom()
        self.nom_complet = f"{self.prenom}{self.nom}"
        self.dateDeNaissance = dateDeNaissance
        self.score = 0

    def valid_id(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("test")
        IdJoueur = input("Entrer l'Identifiant National du joueur :")
        if (
            len(IdJoueur)
            == 7  # modifier la la condition pour IdJoueur / utiliser regex
            and (IdJoueur[0] and IdJoueur[1]) in alphabet
            and int(IdJoueur[2:]) in range(00000, 99999)
        ):
            # Controle unicité
            idExist = Gestionnaire_Joueur().check_id_unicity()
            if IdJoueur in idExist:
                print("Erreur : Cet id existe déjà")
            else:
                # IdExistant.append(IdJoueur)
                Gestionnaire_Joueur().add_id_player(IdJoueur)
                print("Saisi conforme")
            # print(IdExistant)
            return IdJoueur
        else:  # remplacer par un raise
            print("l'identifiant n'est pas au bon format")

    def valid_nom(self):
        nom = input("Entrer le nom de famille :")
        if nom in ALPHABET:
            print("Nom OK")
            return nom
        else:
            print("Le nom ne doit comporter que des caractères alphabétiques")

    def valid_prenom(self):
        prenom = input("Entrer le prénom :")
        if prenom in ALPHABET:
            print("Prénom OK")
            return prenom
        else:
            print("Le prénom ne doit comporter que des caractères alphabétiques")

    # après validation envoyer joueur dans Class Tournoi
    def update_score(self, game_result):  # game_result => tuple (id_joueur, point)
        # une fois le joueur identifié
        self.score += game_result[1]

    def profile_player(self):
        profile = {
            "id_nat": self.idJoueur,
            "nom complet": self.nom_complet,
            "date de naissance": self.dateDeNaissance,
            "score": self.score,
        }
        print(profile)


# J1 = Joueur()
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


class Tournoi:
    def __init__(self, name, place, description, nb_round):
        self.name = name
        self.place = place
        self.dateDeDebut = DateTime().get_day
        self.dateDeFin = ""
        self.nbTours = nb_round
        self.nTourActuel = len(self.list_round)
        self.list_round = []
        self.listeJoueursEnregistres = []
        self.description = description

    def aff_tableau(self, tableau):
        print(tableau)
        return tableau

    def players_list(self):
        self.listeJoueursEnregistres.append(Joueur().profile_player())

    # def add_description(self):
    #     self.description = Tournament().create_description(self)

    def classement(self, tableau):
        tableau.sort_values(by=["score"], ascending=False, inplace=True)
        print(tableau)

    # Remplacer par __str__ ?
    def informations_tournoi(self):  # , listeJoueursEnregistres):
        print(
            f"Tournoi {self.name} à {self.place}"
        )  # , commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}."

    def init_tours(self, nb_tours):  # Recupérer view/tournoi/number_of_round
        self.nbTours = nb_tours

    def sort_ranking(self, dic_joueur):
        dic_joueur2 = sorted(dic_joueur.items(), key=lambda x: x[1], reverse=True)
        print(dict(dic_joueur2))
        return dict(dic_joueur2)


# TT = Tournoi()
# dictionaire = {"AAA": 6, "BB": 6, "BZ": 5, "AB": 1}
# TT.classement(dictionaire)


class Tours:
    def __init__(self):
        self.id_match_joues = []

    def match_joues(
        self, paires=None
    ):  # à envoyer dans la méthode génération des paires
        """Génération des id_match : id_match == id_j1+id_j2 et id_j2+id_j1"""
        print(paires)
        if paires is not None:
            for paire in paires:
                paire.sort()
                self.id_match_joues.append("".join(map(str, paire)))
                paire.sort(reverse=True)
                self.id_match_joues.append("".join(map(str, paire)))
        test = list(set(self.id_match_joues))
        # print(test)
        return self.id_match_joues

    def test_tour(self):
        return self.id_match_joues


class Tour:
    def __init__(self, idTours, classement, liste_matchs_joues):
        self.idTours = idTours
        self.Nom = f"Round {idTours}"
        # self.dateHeureDeDebut = get_time_on()
        # self.dateHeureDeFin = get_time_off()
        self.listMatch = self.generation_des_paires(classement)
        self.classement = classement  # Dataframe

    def generation_des_paires(
        self, classement
    ):  # Classement trié par score descendant, type Dataframe
        print(type(classement))
        paires = []
        liste_joueur = list(classement.keys())
        id_match_joues = Tours().test_tour()
        print(f"ID_MATCH_{id_match_joues}")  # test
        while len(liste_joueur) > 1:
            data = liste_joueur[0]
            for i in range(1, len(liste_joueur)):
                test_id_match_valid = str(data) + str(liste_joueur[i])
                print(type(test_id_match_valid))
                print(test_id_match_valid)
                if (
                    liste_joueur[i] != data
                    and test_id_match_valid not in id_match_joues
                ):
                    paire = [data, liste_joueur[i]]
                    print(f"match : {paire[0]} VS {paire[1]}")
                    paires.append(paire)
                    liste_joueur.pop(i)
                    liste_joueur.pop(0)
                    print(liste_joueur)
                    break
                # prévoir si joueur à jouer tout le monde, créer une séelction d'un élément déjà joué
                else:
                    print("NOK")
            # print(dataframe_to_list)
        print(paires)
        resultat_func = Tours().match_joues(paires)
        print(resultat_func)
        print("Création des matchs terminées")
        return paires

        #     pass
        # (ex : round X)


# test
# colonne = ["IdJoueur", "score"]
# tableau = pd.DataFrame(columns=colonne)
# for i in range(1, 10):
#     tableau.loc[len(tableau)] = [i * 10, 5 * i]
# print(tableau)

# tr1 = Tour(None, None, tableau, None)


# TT = Tournoi()
# dictionaire = {"AAA": 6, "BB": 6, "BZ": 5, "AB": 1}
# test_tour = TT.sort_ranking(dictionaire)
# print(test_tour)
# tr1 = Tour(None, test_tour, None)


class Match:
    def __init__(self, paire):
        self.joueur1 = paire[0]
        self.joueur2 = paire[1]
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.couleurJ1 = ""
        self.couleurJ2 = ""

    def attribution_couleur(self, paire):
        random_color_choice = random.choice([True, False])
        if random_color_choice is True:
            couleurJ1 = "Blanc"
            couleurJ2 = "Noir"
        else:
            couleurJ2 = "Blanc"
            couleurJ1 = "Noir"
        return print(
            f"{self.joueur1} joue en {couleurJ1}, {self.joueur2} joue en {couleurJ2}"
        )

    def input_score(self, paire):  # à retourner dans les resultats de Tour
        print(
            "Entrer les points acquis par les 2 joueurs au terme de ce tour. Valeurs possibles : 0, 0.5, 1"
        )
        points_possibles = ["0", "0.5", "1"]
        scoreJ1 = input(f"Indiquer le score obtenu par {self.joueur1} :")
        if scoreJ1 in points_possibles:
            scoreJ2 = input(f"Indiquer le score obtenu par {self.joueur2} :")
            if scoreJ2 in points_possibles:
                print(
                    f"Le joueur {self.joueur1} a obtenu {scoreJ1} point, le joueur {self.joueur2} a obtenu {scoreJ2} point"
                )
                return ([paire[0], scoreJ1], [paire[1], scoreJ2])
            else:
                print("Vous avez entré une valeur incorrecte")
        else:
            print("Vous avez entré une valeur incorrecte")


# match1 = Match(["AAAAAA", "BBBBBB"])
# match1.attribution_couleur(["AAAAAA", "BBBBBB"])
# resultat_match = match1.attribution_point(["AAAAAA", "BBBBBB"])


# paire = [12, 67]
# match1 = Match(paire)
# match1.input_score(paire)
