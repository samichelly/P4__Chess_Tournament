from Tournament import Tournament
from get_datetime import get_time


class Round:
    def __init__(self, idround):
        self.idround = idround
        self.name = f"Round {idround}"
        self.time_top = ""
        self.time_stop = ""
        self.listMatch = []

    def pairs_generation(
        self, players_ranked, id_match_played
    ):  # Classement trié par score
        players_list = []
        for i in players_ranked:
            print(i.idJoueur)       #à supprimer
            players_list.append(i.idJoueur)
        print(f"ID_MATCH_EXIST{id_match_played}")  # test
        while len(players_list) > 1:
            for i in range(1, len(players_list)):
                test_id_match = str(players_list[0]) + str(players_list[i])
                print(test_id_match)
                if test_id_match not in id_match_played:
                    paire = [players_list[0], players_list[i]]
                    print(f"match : {paire[0]} VS {paire[1]}")
                    self.listMatch.append(paire)
                    players_list.pop(i)
                    players_list.pop(0)
                    print(players_list)
                    break  # voir pour suppression
                # prévoir si joueur à jouer tout le monde, créer une sélection d'un élément déjà joué
                else:
                    print("NOK")
        print(self.listMatch)
        print("Création des matchs terminées")
        return self.listMatch

        #     pass
        # (ex : round X)

    def results_round(self, result_matchs):
        self.listMatch = result_matchs
        print("llllll")
        print(self.listMatch)
        return self.listMatch

    def time_begin(self):
        self.time_top = get_time()
        return self.time_top

    def time_end(self):
        self.time_stop = get_time()
        # return self.date_top


