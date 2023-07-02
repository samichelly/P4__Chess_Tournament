import jsonpickle
import os

path = "C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/test.json"

# print(os.getcwd())
# si chemin n'existe pas
# if not os.path.exists(f"output/{categorie}"):
#         os.makedirs(f"output/{categorie}")


def save_tournament(tournament_to_save, tournament_loaded, table):
    print("\nEnregistrement en cours\n")
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "w",
    ) as file:
        if tournament_loaded is None:
            tournament_loaded = {
                "tournament_table": [{tournament_to_save.name: tournament_to_save}]
            }

        else:
            tournament_saved = False
            for i, tournament_ in enumerate(tournament_loaded["tournament_table"]):
                if str(tuple(tournament_.keys())[0]) == str(tournament_to_save.name):
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


def save_player(player_to_save, players_loaded, table):
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "w",
    ) as file:
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


def read_tournament_json(table):
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        json_str = infile.read()
        try:
            json_objet = jsonpickle.decode(json_str)
            return json_objet
        except Exception:
            print("Aucun joueur enregistré en base de donnée")
            return None


def read_players_json(table):
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        json_str = infile.read()
        try:
            json_objet = jsonpickle.decode(json_str)
            return json_objet
        except Exception:
            print("Aucun joueur enregistré en base de donnée")
            return None


def load_tournament_json(tournament_loaded, select_tournament):
    print("Chargement en cours")
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
                "registered_players": tournament_[tournament_data].registered_players,
                "id_match_played": tournament_[tournament_data].id_match_played,
                "description": tournament_[tournament_data].description,
            }
    print(tournament_loading)
    print("testççççççççç")
    return tournament_loading


def load_player(players_loaded, select_players):
    players_selected = []
    for i, player_ in enumerate(players_loaded["playertable"], start=1):
        if str(i) in select_players:
            # print(i)
            player_data = next(iter(player_))
            player_loading = {
                "idplayer": player_[player_data].idplayer,
                "name": player_[player_data].name,
                "forename": player_[player_data].forename,
                "birthday": player_[player_data].birthday,
                "score": player_[player_data].score,
                "rank": player_[player_data].rank,
            }
            print(player_loading)
            players_selected.append(player_loading)
    print(players_selected)
    return players_selected
