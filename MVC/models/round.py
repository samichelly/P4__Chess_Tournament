from get_datetime import get_time


class Round:
    def __init__(self, idround):
        self.idround = idround
        self.name = f"Round {idround}"
        self.time_top = self.time_begin()
        self.time_stop = ""
        self.matchs_round = []

    def __str__(self):
        if self.time_stop == "":
            return f"\n{self.name}"
        else:
            return f"{self.name} débuté à {self.time_top} et terminé à {self.time_stop}. \nRésultats :\n{self.matchs_round}"

    # ajouter un player fictif si nombre de joueur impair
    def pairs_generation(
        self, players_ranked, id_match_played
    ):  # Classement trié par score / player_ranked = obj player
        players_list = [i.idplayer for i in players_ranked]
        test_pair = len(players_list) % 2
        if test_pair > 0:
            players_list.insert(1, "EXEMPT")
        while len(players_list) > 1:
            for i in range(1, len(players_list)):
                test_id_match = str(players_list[0]) + str(players_list[i])

                if test_id_match not in id_match_played:
                    paire = [players_list[0], players_list[i]]
                    self.matchs_round.append(paire)
                    print(f"match : {paire[0]} VS {paire[1]}")
                    players_list.pop(i)
                    players_list.pop(0)
                    break

                elif players_list[i] == players_list[-1]:
                    paire = [players_list[0], players_list[1]]
                    self.matchs_round.append(paire)
                    print(f"match : {paire[0]} VS {paire[1]}")
                    players_list.pop(1)
                    players_list.pop(0)
                    break

                else:
                    None

        print(players_list)
        print(self.matchs_round)
        print("Création des matchs terminées")
        return self.matchs_round

    def clean_exempt_match(self, list_match):
        for i in list_match:
            test = str(i).find("EXEMPT")
            if test != -1:
                list_match.remove(i)
        self.matchs_round = list_match
        return self.matchs_round

    def results_round(self, result_matchs):
        self.matchs_round = result_matchs
        return self.matchs_round

    def time_begin(self):
        self.time_top = get_time()
        return self.time_top

    def time_end(self):
        self.time_stop = get_time()
        # return self.date_top

    # def save_round(self):
    #     return {
    #         "idround": self.idround,
    #         "round": self.name,
    #         "time_top": self.time_top,
    #         "time_stop": self.time_stop,
    #         "matchs": self.matchs_round,
    #     }
