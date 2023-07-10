import jsonpickle


class Database:
    def save_tournament(self, tournament_to_save, tournament_loaded):
        """save tournament_to_save
        1) create tournament_loaded if is empty. it's list of tournamnent
        2) if tournament_to_save exist in tournament_loaded, overwrite it
        else append tournament_to_save to tournament_loaded
        """
        with open("database/tournament.json", "w") as file:
            if tournament_loaded is None:
                tournament_loaded = {
                    "tournament_table": [{tournament_to_save.name: tournament_to_save}]
                }

            else:
                tournament_saved = False
                for i, tournament_ in enumerate(tournament_loaded["tournament_table"]):
                    if str(tuple(tournament_.keys())[0]) == str(
                        tournament_to_save.name
                    ):
                        tournament_loaded["tournament_table"][i] = {
                            tournament_to_save.name: tournament_to_save
                        }
                        tournament_saved = True
                if tournament_saved is False:
                    tournament_loaded["tournament_table"].append(
                        {tournament_to_save.name: tournament_to_save}
                    )
                tournament_loaded["tournament_table"] = sorted(
                    tournament_loaded["tournament_table"],
                    key=lambda x: x[next(iter(x))].name,
                )

            json_objet = jsonpickle.encode(tournament_loaded, indent=4)
            file.write(json_objet)
            print("\nSauvegarde réussie\n")

    def save_player(self, player_to_save, players_loaded):
        """save player_to_save
        1) create players_loaded if is empty. it's list of players
        2) if player_to_save exist in players_loaded, overwrite it
        else append player_to_save to players_loaded
        """
        with open("database/player.json", "w") as file:
            if players_loaded is None:
                players_loaded = {
                    "playertable": [{player_to_save.idplayer: player_to_save}]
                }

            else:
                players_loaded["playertable"].append(
                    {player_to_save.idplayer: player_to_save}
                )
                players_loaded["playertable"] = sorted(
                    players_loaded["playertable"], key=lambda x: x[next(iter(x))].name
                )
            json_objet = jsonpickle.encode(players_loaded, indent=4)
            file.write(json_objet)
            print("\nSauvegarde réussie\n")

    def read_tournament_json(self):
        with open("database/tournament.json", "r") as file:
            json_str = file.read()
            try:
                json_objet = jsonpickle.decode(json_str)
                return json_objet
            except Exception:
                print("Aucun tournoi enregistré en base de donnée")
                return None

    def read_players_json(self):
        with open("database/player.json", "r") as file:
            json_str = file.read()
            try:
                json_objet = jsonpickle.decode(json_str)
                return json_objet
            except Exception:
                print("Aucun joueur enregistré en base de donnée")
                return None

    def load_tournament_json(self, tournament_loaded, select_tournament):
        """return load tournament if it is select_tournament"""
        for i, tournament_ in enumerate(tournament_loaded["tournament_table"], start=1):
            if str(i) in select_tournament:
                tournament_data = next(iter(tournament_))
                tournament_loading = {
                    "name": tournament_[tournament_data].name,
                    "place": tournament_[tournament_data].place,
                    "date_top": tournament_[tournament_data].date_top,
                    "date_stop": tournament_[tournament_data].date_stop,
                    "nb_round": tournament_[tournament_data].nb_round,
                    "current_round": tournament_[tournament_data].current_round,
                    "list_round": tournament_[tournament_data].list_round,
                    "registered_players": tournament_[
                        tournament_data
                    ].registered_players,
                    "id_match_played": tournament_[tournament_data].id_match_played,
                    "description": tournament_[tournament_data].description,
                }
        return tournament_loading

    def load_player(self, players_loaded, select_players):
        """return load player if it is select_player"""
        players_selected = []
        for i, player_ in enumerate(players_loaded["playertable"], start=1):
            if str(i) in select_players:
                player_data = next(iter(player_))
                player_loading = {
                    "idplayer": player_[player_data].idplayer,
                    "name": player_[player_data].name,
                    "forename": player_[player_data].forename,
                    "birthday": player_[player_data].birthday,
                    "score": player_[player_data].score,
                    "rank": player_[player_data].rank,
                }
                players_selected.append(player_loading)
        return players_selected
