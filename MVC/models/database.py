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
    table = {table: data_models}
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "w",
    ) as file:
        json_objet = jsonpickle.encode(table, indent=4)
        file.write(json_objet)


def save_player(player_to_save, players_loaded, table):
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "w",
    ) as file:
        if players_loaded is None:
            players_loaded = {"playertable": [{player_to_save.idplayer: player_to_save}]}

        else:
            players_loaded["playertable"].append({player_to_save.idplayer: player_to_save})
            players_loaded["playertable"] = sorted(players_loaded["playertable"], key=lambda x: x[next(iter(x))].name)
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
        # print("jjjj")
        # print(json_str)
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
    print("Enregistrement en cours")
    with open(
        f"C:/Users/samic/Documents/OpenClassRooms/PROJET_3/MVC/database/{table}.json",
        "r",
    ) as infile:
        json_str = infile.read()
        print(json_str)
        print("json_str")
        try:
            print("dans le try")
            json_objet = jsonpickle.decode(json_str)
            print("dans le try")
            print(json_objet.keys())
            print("json_obbbbjt")
            # player = {
            #     "ggggggg": {
            #         "idplayer": json_objet.idplayer,
            #         "name": json_objet.name,
            #         "forename": json_objet.forename,
            #         "fullname": json_objet.fullname,
            #         "birthday": json_objet.birthday,
            #         "score": json_objet.score,
            #         "rank": json_objet.rank,
            #     }
            # }
            print("affichage player")
            print(json_objet)
            return json_objet
        except Exception:
            # json_objet = jsonpickle.decode(json_str)
            print("tableau vide")
            return None
    # }
    # print(tournoi)
    # print("testççççççççç")
    # # print(json_objet['name'])
    # return tournoi


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
