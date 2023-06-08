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

    def update_last_round(self, result_round):
        self.list_round.append(result_round)
        print("gccz")
        return self.list_round[-1]

    def date_begin(self):
        self.date_top = get_day()
        return self.date_top

    def date_end(self):
        self.date_stop = get_day()
        # return self.date_top

    def get_current_round(self):
        self.current_round = len(self.list_round)
        return self.current_round

    def get_players_list(self, player):
        self.registered_players.append(player)
        print(self.registered_players)
        print(player)
        return self.registered_players

    def update_score(self, game_result):  # game_result => tuple (id_joueur, point)
        for player in self.registered_players:
            for result in game_result:
                for id in result:
                    # print(result)
                    # print(id)
                    # print(f"player_name {player.idJoueur}")
                    # print(f"result indiv {id[0]}")
                    if player.idJoueur == str(id[0]):
                        player.score += id[1]
                        print("score")
                        print(player.idJoueur, player.score)
                        break

    # def classement(self, tableau):
    #     tableau.sort_values(by=["score"], ascending=False, inplace=True)
    #     print(tableau)

    # Remplacer par __str__ ?
    # def informations_tournoi(self):  # , listeJoueursEnregistres):
    #     print(
    #         f"Tournoi {self.name} à {self.place}"
    # )  # , commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}."

    def sort_ranking(self, players):
        # tuple_players = []
        self.registered_players = sorted(players, key=lambda x: x.score, reverse=True)
        print(self.registered_players)
        return self.registered_players

    def match_played(self, paires):
        """Génération des id_match : id_match == id_j1+id_j2 et id_j2+id_j1"""
        for paire in paires:
            paire.sort()
            self.id_match_joues.append("".join(map(str, paire)))
            paire.sort(reverse=True)
            self.id_match_joues.append("".join(map(str, paire)))
        return self.id_match_joues

    def test_round(self):  # issue de la Class Tours
        return self.id_match_joues
