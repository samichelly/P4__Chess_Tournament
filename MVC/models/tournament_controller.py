from tournament_view import Tournament_Menu, Tournament_Creation, Tournament_Reports
from tournament import Tournament
from create_player_view import Create_Player_View
from player import Player, Players_Manager
from round import Round
from match import Match
import database


def menu_tournament():
    while True:
        tournament_menu = Tournament_Menu()

        if tournament_menu.menu == "1":
            # génération des rapports
            pass

        elif tournament_menu.menu == "2":
            # création de nouveau joueur (hors tournoi)
            while True:
                new_player = str.upper(
                    input("\nIncrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
                )
                if new_player == "O":
                    players_loaded = database.load_players("player")
                    if players_loaded is not None:
                        for i in players_loaded.values():
                            for j in i:
                                print(j)
                                print("joueur affiché")
                    else:
                        pass
                    print(players_loaded)
                    print("playersloaded")
                    # print(len(players_loaded))
                    player = Player(
                        Create_Player_View(manager=None).create_profile_player()
                    )
                    database.save_player(player, players_loaded, "player")
                elif new_player == "N":
                    False
                    tournament_menu = Tournament_Menu()
                else:
                    print("Erreur : Entrée non valide")

        elif tournament_menu.menu == "3":
            tournament_def = Tournament(Tournament_Creation().about_tournament())
            print(tournament_def.__dict__)
            print(tournament_def.name)
            database.save_data(tournament_def, "tournament")
            adding_player = True
            manager = Players_Manager()
            while adding_player:
                add_player = str.upper(
                    input("\nIncrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
                )
                if add_player == "O":
                    player = Player(Create_Player_View(manager).create_profile_player())
                    print(player)
                    players_list = tournament_def.get_players_list(player)
                    # print(f"player_list{players_list}")
                elif add_player == "N":
                    adding_player = False
                else:
                    print("Erreur : Entrée non valide")
            database.save_data(tournament_def, "tournament")

        elif tournament_menu.menu == "4":
            print("chargement")
            table = "tournament"
            tournoi_charge = database.load_tournament(table)
            tournament_def = Tournament(tournoi_charge)
            players_list = tournoi_charge["registered_players"]

        else:
            print("Error selection")

        if tournament_menu.menu in ["3", "4"]:
            launch_round = True
            tournament_def.date_begin()
            while tournament_def.current_round < tournament_def.nb_round:
                if launch_round:
                    launch_new_round = tournament_menu.launch_new_round()
                    if launch_new_round is False:
                        break
                    # tournament_def.sort_ranking(players_list)
                    current_round = tournament_def.get_current_round() + 1
                    new_round = Round(current_round)
                    print(new_round)
                    pairs_generated = new_round.pairs_generation(
                        tournament_def.sort_ranking(players_list),
                        tournament_def.test_rematch(),
                    )
                    print(pairs_generated)  #  intégrer une view avant les matchs ?
                    tournament_def.match_played(pairs_generated)
                    print("rrr")
                    print(tournament_def.id_match_played)
                    new_round.clean_exempt_match(pairs_generated)
                    database.save_data(tournament_def, "tournament")

                    # lancer les matchs
                    result_round = []
                    for i in pairs_generated:
                        match = Match(i)
                        match.attribution_couleur(i)
                        result_game = match.input_score(i)
                        print(match)
                        database.save_data(match, "match")
                        result_round.append(result_game)
                    new_round.time_end()
                    # print("tesssst")
                    result_round = new_round.results_round(result_round)
                    new_round.time_end()
                    print(new_round)
                    print(result_round)
                    update_tournament = tournament_def.update_last_round(result_round)
                    database.save_data(new_round, "round")
                    del new_round
                    print(update_tournament)
                    print(tournament_def.list_round)
                    tournament_def.update_score(result_round)
                    database.save_data(tournament_def, "tournament")
                else:
                    print("fin du tournoi ou autres actions")
                    tournament_def.date_end()
                    sorted_players = tournament_def.sort_ranking(players_list)
                    ranking = tournament_def.final_ranking(sorted_players)
                    tournament_menu.display_final_ranking(ranking)
                    database.save_data(tournament_def, "tournament")
                    for i in players_list:
                        i.set_score_to_score()
            print("fini")


menu_tournament()
