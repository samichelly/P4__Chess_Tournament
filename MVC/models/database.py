import json
import jsonpickle
import os
import player
import tournament
import round
import match

path = "C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/test.json"

# print(os.getcwd())
# si chemin n'existe pas
# if not os.path.exists(f"output/{categorie}"):
#         os.makedirs(f"output/{categorie}")


def save_data(data_models, table):
    print("fnonc")
    data_to_save = {table: data_models}
    print(table)
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "w",
    ) as file:
        json_objet = jsonpickle.encode(data_to_save, indent=4)
        print(json_objet)
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
        print("aaaaaaaaa")
        json_objet = jsonpickle.encode(players_loaded, indent=4)
        file.write(json_objet)


def load_tournament(table):
    print("Enregistrement en cours")
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        json_str = infile.read()
        json_objet = jsonpickle.decode(json_str)
    print("mmmmmmm")
    print(type(json_objet))
    print(json_objet)
    tournoi = {
        "name": json_objet["tournament"].name,
        "place": json_objet["tournament"].place,
        "date_top": json_objet["tournament"].date_top,
        "date_stop": json_objet["tournament"].date_stop,
        "nb_round": json_objet["tournament"].nb_round,
        "current_round": json_objet["tournament"].current_round,
        "list_round": json_objet["tournament"].list_round,
        "registered_players": json_objet["tournament"].registered_players,
        "id_match_played": json_objet["tournament"].id_match_played,
        "description": json_objet["tournament"].description,
    }
    print(tournoi)
    print("testççççççççç")
    return tournoi


def load_players(table):
    print("Chargement en cours")
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        json_str = infile.read()
        try:
            json_objet = jsonpickle.decode(json_str)
            print("affichage player")
            print(json_objet)
            print("testttt")
            return json_objet
        except Exception:
            print("Aucun joueur enregistré en base de donnée")
            return None


def load_player(players_loaded, select_players):
    players_selected = []
    for i, player_ in enumerate(players_loaded["playertable"], start=1):
        # print(player_)
        # print(i)
        if str(i) in select_players:
            print(i)
            # print(select_player)
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


# select_player = [3, 6]
# players_loaded = load_players("player")
# load_player(players_loaded, select_player)

    # for i, player_ in enumerate(players_loaded["playertable"], start=1):
    #     print("i")
    #     print(i)
    #     print(player_)
    #     if str(i) in select_players:
    #         players_selected.append(player_.values())
    #         print("test")
    #         # test = player_.values()
    #         # print(test['fullname'])
    #         print("players_selected")
    #         print(players_selected)

    # return players_selected



# for i in players_loaded["playertable"]:
#     player_data = next(iter(i))
#     player_list = [
#         i[player_data].idplayer,
#         i[player_data].name,
#         i[player_data].forename,
#         i[player_data].fullname,
#         i[player_data].birthday,
#         i[player_data].score,
#         i[player_data].rank,
#     ]


"""
def update_data(data_models, table, attribute_to_update):
    print("ipdate")
    # print(json_objet)
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        print("fnonc")
        # json_str = infile.read()
        # json_splited = json_str.split("}{")
        # print("jjjj")
        # for i in json_splited:
        #     print(i)
        #     print("json spliteeee")
        # print(json_str)
        json_objet = json.load(infile)
        json_objet[attribute_to_update] = data_models
        print("mmmmmmm")
    print(type(json_objet))
    print(json_objet)
    print(json_objet.registered_players)
    print("testççççççççç")
"""

# if not os.path.exists(f"output/{categorie}"):
#     os.makedirs(f"output/{categorie}")
