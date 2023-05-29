import random
import string
import re

# from view import Tournament
# from controller import DateTime


class Tournoi:
    def __init__(self, name, place, description, nb_round):
        self.name = name
        self.place = place
        # self.dateDeDebut = DateTime().get_day
        self.dateDeFin = ""
        self.nbTours = nb_round
        self.nTourActuel = len(self.list_round)
        self.list_round = []
        self.listeJoueursEnregistres = []
        self.id_match_joues = []  # issue de class Tours
        self.description = description

    # def aff_tableau(self, tableau):
    #     print(tableau)
    #     return tableau

    def players_list(self):
        self.listeJoueursEnregistres.append(Joueur().profile_player())

    # def add_description(self):
    #     self.description = Tournament().create_description(self)

    # def classement(self, tableau):
    #     tableau.sort_values(by=["score"], ascending=False, inplace=True)
    #     print(tableau)

    # Remplacer par __str__ ?
    # def informations_tournoi(self):  # , listeJoueursEnregistres):
    #     print(
    #         f"Tournoi {self.name} à {self.place}"
    # )  # , commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}."

    def sort_ranking(self, dic_joueur):
        dic_joueur2 = sorted(dic_joueur.items(), key=lambda x: x[1], reverse=True)
        print(dict(dic_joueur2))
        return dict(dic_joueur2)

    def match_joues(self, paires=None):  # issue de la Class Tours
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

    def test_tour(self):  # issue de la Class Tours
        return self.id_match_joues


# TT = Tournoi()
# dictionaire = {"AAA": 6, "BB": 6, "BZ": 5, "AB": 1}
# TT.classement(dictionaire)
