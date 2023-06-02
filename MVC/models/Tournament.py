from Player import Player
from get_datetime import get_day

# from view import Tournament
# from controller import DateTime


class Tournament:
    def __init__(self, about_tournament):
        self.name = about_tournament[0]
        self.place = about_tournament[1]
        self.date_top = ""
        self.date_stop = ""
        self.nbTours = about_tournament[2]
        self.current_round = ""
        self.list_round = []
        self.registered_players = []
        self.id_match_joues = ["KH22332KH22333"]  # issue de class Tours
        self.description = about_tournament[3]

    def test_func(self):
        return self.name

    def date_begin(self):
        self.date_top = get_day()
        return self.date_top
    
    def date_end(self):
        self.date_stop = get_day()
        # return self.date_top
    
    def get_current_round(self):
        self.current_round = len(self.list_round)
        return self.current_round



    def get_players_list(self, players_list):
        self.registered_players = players_list
        print(self.registered_players)
        print("ggggg")
        return self.registered_players

    # def classement(self, tableau):
    #     tableau.sort_values(by=["score"], ascending=False, inplace=True)
    #     print(tableau)

    # Remplacer par __str__ ?
    # def informations_tournoi(self):  # , listeJoueursEnregistres):
    #     print(
    #         f"Tournoi {self.name} à {self.place}"
    # )  # , commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}."

    def sort_ranking(self, tuple_players):
        return sorted(tuple_players, key=lambda x: x[1], reverse=True)
        # print(dict(dic_players2))
        # return dict(dic_players2)

    def match_played(self, paires):  # issue de la Class Tours
        """Génération des id_match : id_match == id_j1+id_j2 et id_j2+id_j1"""
        # print(paires)
        for paire in paires:
            paire.sort()
            self.id_match_joues.append("".join(map(str, paire)))
            paire.sort(reverse=True)
            self.id_match_joues.append("".join(map(str, paire)))
        test = list(set(self.id_match_joues))
        # print(test)
        return self.id_match_joues

    def test_round(self):  # issue de la Class Tours
        return self.id_match_joues


# TT = Tournament(None, None, None, None)
# TT.players_list()
# dictionaire = {"AAA": 6, "BB": 6, "BZ": 5, "AB": 1}
# TT.classement(dictionaire)
