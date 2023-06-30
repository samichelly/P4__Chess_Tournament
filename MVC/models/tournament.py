import pandas as pd
from get_datetime import get_day


class Tournament:
    def __init__(self, about_tournament):
        self.name = about_tournament['name']
        self.place = about_tournament['place']
        self.date_top = about_tournament['date_top']
        self.date_stop = about_tournament['date_stop']
        self.nb_round = about_tournament['nb_round']
        self.current_round = about_tournament['current_round']
        self.list_round = about_tournament['list_round']
        self.registered_players = about_tournament['registered_players']
        self.id_match_played = about_tournament['id_match_played']
        self.description = about_tournament['description']

    def __str__(self):
        if self.date_stop == "":
            return f"\nTournoi : {self.name} ({self.place}) du {self.date_top}"
        else:
            return f"\nTournoi : {self.name} ({self.place}) débuté le {self.date_top} et terminé le {self.date_stop}. Les résultats :\n{self.list_round}"

    def date_begin(self):
        self.date_top = get_day()
        return self.date_top

    def date_end(self):
        self.date_stop = get_day()
        # return self.date_top

    def get_current_round(self):
        self.current_round = len(self.list_round) + 1
        return self.current_round

    def update_last_round(self, result_round):
        self.list_round.append(result_round)
        # return self.list_round[-1]

    def get_players_list(self, player):
        self.registered_players.append(player)
        print(f"Joueurs enregistré(s) : {len(self.registered_players)}")
        return self.registered_players
    
    def sort_alphabetic(self, players):
        self.registered_players = sorted(players, key=lambda x: x.name)
        return self.registered_players

    def match_played(self, paires):
        """Génération des id_match : id_match == id_j1+id_j2 et id_j2+id_j1"""
        for paire in paires:
            paire.sort()
            self.id_match_played.append("".join(map(str, paire)))
            paire.sort(reverse=True)
            self.id_match_played.append("".join(map(str, paire)))
        return self.id_match_played

    def test_rematch(self):
        return self.id_match_played

    def update_score(self, game_result):  # game_result => tuple (id_joueur, point)
        for player in self.registered_players:
            for result in game_result:
                for id in result:
                    if player.idplayer == str(id[0]):
                        player.score += id[1]
                        print("score")
                        print(player.idplayer, player.score)
                        break

    def sort_ranking(self, players):
        self.registered_players = sorted(players, key=lambda x: x.score, reverse=True)
        return self.registered_players

    def final_ranking(self, players):
        head_table = ["Identifiant", "Nom Complet", "Points"]  # add player_rank
        ranking = pd.DataFrame(columns=head_table)
        # ranking.index = range(1, len(players))
        for player in players:
            profile_player = [player.idplayer, player.fullname, player.score]
            ranking.loc[len(ranking)] = profile_player
        ranking.sort_values(by=["Points"], ascending=False)
        # Ajouter le trie du classement par rang + index qui conmmence par 1
        return ranking

    # def save_tournament(self):
    #     return {
    #         "tournament_name": self.name,
    #         "tournament_place": self.place,
    #         "date_top": self.date_top,
    #         "date_stop": self.date_stop,
    #         "number_of_rounds": self.nbRound,
    #         "current_round": self.current_round,
    #         "rounds": self.list_round,
    #         "registered_players": self.registered_players,
    #         "description": self.description,
    #     }
