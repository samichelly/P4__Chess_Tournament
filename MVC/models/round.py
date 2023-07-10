from controller.get_datetime import Timing


class Round:
    def __init__(self, idround):
        self.idround = idround
        self.name = f"Round {idround}"
        self.time_top = self.time_begin()
        self.time_stop = ""
        self.matches_round = []
        self.obj_matches = []

    def __str__(self):
        if self.time_stop == "":
            return f"\n{self.name}"
        else:
            return (
                f"\n{self.name} débuté à {self.time_top} et terminé à {self.time_stop}"
            )

    def pairs_generation(self, players_sorted, id_match_played):
        """if players_sorted is odd number, create exempt player to complete matchmaking
        id_match_played is result of tournament method match_played
        create match between closest 2 players not id_match_played
        if impossible create match between closest players
        """
        players_list = [i.idplayer for i in players_sorted]
        test_pair = len(players_list) % 2
        if test_pair > 0:
            players_list.insert(1, "EXEMPT")
        while len(players_list) > 1:
            for i in range(1, len(players_list)):
                test_id_match = str(players_list[0]) + str(players_list[i])

                if test_id_match not in id_match_played:
                    paire = [players_list[0], players_list[i]]
                    self.matches_round.append(paire)
                    print(f"match : {paire[0]} VS {paire[1]}")
                    players_list.pop(i)
                    players_list.pop(0)
                    break

                elif players_list[i] == players_list[-1]:
                    paire = [players_list[0], players_list[1]]
                    self.matches_round.append(paire)
                    print(f"match : {paire[0]} VS {paire[1]}")
                    players_list.pop(1)
                    players_list.pop(0)
                    break

                else:
                    continue

        return self.matches_round

    def clean_exempt_match(self, list_match):
        """erase EXEMPT match to don't play it"""
        for i in list_match:
            test = str(i).find("EXEMPT")
            if test != -1:
                list_match.remove(i)
        self.matches_round = list_match
        return self.matches_round

    def results_round(self, result_matches):
        """get tuple ([player, score], [player, score])"""
        self.matches_round = result_matches
        return self.matches_round

    def get_match(self, match):
        """get object match"""
        self.obj_matches.append(match)

    def time_begin(self):
        time = Timing()
        self.time_top = time.get_time()

    def time_end(self):
        time = Timing()
        self.time_stop = time.get_time()
