from random import shuffle
from prettytable import PrettyTable
from controller.get_datetime import Timing


class Tournament:
    def __init__(self, about_tournament):
        self.name = about_tournament["name"]
        self.place = about_tournament["place"]
        self.date_top = about_tournament["date_top"]
        self.date_stop = about_tournament["date_stop"]
        self.nb_round = about_tournament["nb_round"]
        self.current_round = about_tournament["current_round"]
        self.list_round = about_tournament["list_round"]
        self.registered_players = about_tournament["registered_players"]
        self.id_match_played = about_tournament["id_match_played"]
        self.description = about_tournament["description"]

    def __str__(self):
        if self.date_stop == "":
            return f"\nTournoi : {self.name} ({self.place}) du {self.date_top}"
        else:
            return f"\nTournoi : {self.name} ({self.place}) débuté le {self.date_top} et terminé le {self.date_stop}."

    def date_begin(self):
        date = Timing()
        self.date_top = date.get_day()

    def date_end(self):
        date = Timing()
        self.date_stop = date.get_day()

    def get_players_list(self, player):
        """add player to tournament"""
        self.registered_players.append(player)
        return self.registered_players

    def shuffle_players(self):
        """shuffle players for first round"""
        shuffle(self.registered_players)
        return self.registered_players

    def get_players(self):
        return self.registered_players

    def get_current_round(self):
        """return the current round"""
        self.current_round = len(self.list_round) + 1
        return self.current_round

    def update_last_round(self, result_round):
        """update match results of complete round"""
        self.list_round.append(result_round)

    def match_played(self, paires):
        """generate id_match to avoid rematch: id_match == id_p1+id_p2 et id_p2+id_p1"""
        for paire in paires:
            paire.sort()
            self.id_match_played.append("".join(map(str, paire)))
            paire.sort(reverse=True)
            self.id_match_played.append("".join(map(str, paire)))
        return self.id_match_played

    def test_rematch(self):
        return self.id_match_played

    def update_score(self, game_result):
        """game_result => tuple (id_joueur, point)
        update score for each player
        """
        for player in self.registered_players:
            for result in game_result:
                for id in result:
                    if player.idplayer == str(id[0]):
                        player.score += id[1]
                        break

    def sort_score(self, players):
        """sort by score"""
        self.registered_players = sorted(players, key=lambda x: x.score, reverse=True)
        return self.registered_players

    def display_ranking(self):
        ranking = PrettyTable()
        ranking.title = "Classement"
        ranking.field_names = [
            "Identifiant",
            "Nom",
            "Prénom",
            "Nom complet",
            "Date de naissance",
            "Score",
        ]
        for i in self.registered_players:
            players_list = [
                i.idplayer,
                i.name,
                i.forename,
                i.fullname,
                i.birthday,
                i.score,
            ]
            ranking.add_row(players_list)
        ranking.sortby = "Score"
        ranking.reversesort = True
        print(ranking)
