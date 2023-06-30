from tournament_view import Tournament_Menu, Tournament_Creation, Tournament_Reports
from tournament import Tournament
from create_player_view import Create_Player_View
from player import Player, Players_Manager
from round import Round
from match import Match
import database
import reports


def menu_tournament():  # prévoir de faire un quit tournament
    while True:
        tournament_menu = Tournament_Menu()

        if tournament_menu.menu == 1:
            print("consulter les rapports")
            choice_reports = Tournament_Reports().select_rapport()
            if choice_reports == "1":  # rapports tous joueurs
                players_loaded = database.load_players("player")
                reports.players_reports(players_loaded)

            elif choice_reports == "2":
                tournament_loaded = database.load_tournament("tournament")
                reports.tournaments_reports(tournament_loaded)

        elif tournament_menu.menu == 2:
            while True:
                new_player = str.upper(
                    input("\nIncrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
                )
                if new_player == "O":
                    players_loaded = database.load_players("player")
                    print(players_loaded)
                    print("playersloaded")
                    player = Player(
                        Create_Player_View(manager=None).create_profile_player()
                    )
                    database.save_player(player, players_loaded, "player")
                elif new_player == "N":
                    False
                else:
                    print("Erreur : Entrée non valide")

        elif tournament_menu.menu == 3:
            tournament_def = Tournament(Tournament_Creation().about_tournament())
            tournament_loaded = database.load_tournament("tournament")
            database.save_tournament(tournament_def, tournament_loaded, "tournament")
            players_loaded = database.load_players("player")
            manager = Players_Manager()
            while True:
                add_player = str.upper(
                    input(
                        "\n1) Charger des joueurs\n2) Incrire un nouveau joueur\n3) Quitter\nChoix : "
                    )
                )

                if add_player == "1":
                    reports.players_reports(players_loaded)
                    input_text = input(
                        "\nIndiquer les Index séparés par une virgule et un espace : "
                    )
                    players_selection = input_text.split(", ")
                    players = database.load_player(players_loaded, players_selection)
                    for i in players:
                        player = Player(i)
                        players_list = tournament_def.get_players_list(player)

                elif add_player == "2":
                    while True:
                        player = Player(
                            Create_Player_View(manager=None).create_profile_player()
                        )
                        database.save_player(player, players_loaded, "player")
                        print(player)
                        players_list = tournament_def.get_players_list(player)
                        add_new_player = str.upper(
                            input(
                                "Ajouter un nouveau joueur :\nO-Oui\nN-Non\nChoix :  "
                            )
                        )
                        if add_new_player == "O":
                            pass
                        elif add_new_player == "N":
                            break
                        else:
                            print("Erreur : Entrée non valide")
                elif add_player == "3":
                    break
                else:
                    print("Erreur : Entrée non valide")
                tournament_loaded = database.load_tournament("tournament")
                database.save_tournament(
                    tournament_def, tournament_loaded, "tournament"
                )

        elif tournament_menu.menu == 4:
            print("chargement")
            table = "tournament"
            tournoi_charge = database.load_tournament(table)
            tournament_def = Tournament(tournoi_charge)
            players_list = tournoi_charge["registered_players"]

        elif tournament_menu.menu == 5:
            break

        else:
            print("Error selection")

        ### TOURNOI EN JEU ###
        if tournament_menu.menu in [3, 4]:
            while tournament_def.current_round < tournament_def.nb_round:
                tournament_def.date_begin()
                launch_new_round = tournament_menu.launch_new_round()
                if launch_new_round is True:
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
                    tournament_loaded = database.load_tournament("tournament")
                    database.save_tournament(
                        tournament_def, tournament_loaded, "tournament"
                    )

                    # lancer les matchs
                    result_round = []
                    for i in pairs_generated:
                        match = Match(i)
                        match.attribution_couleur(i)
                        result_game = match.input_score(i)
                        print(match)
                        result_round.append(result_game)
                    new_round.time_end()
                    # print("tesssst")
                    result_round = new_round.results_round(result_round)
                    new_round.time_end()
                    print(new_round)
                    print(result_round)
                    update_tournament = tournament_def.update_last_round(result_round)
                    del new_round
                    print(update_tournament)
                    print(tournament_def.list_round)
                    tournament_def.update_score(result_round)
                    tournament_loaded = database.load_tournament("tournament")
                    database.save_tournament(
                        tournament_def, tournament_loaded, "tournament"
                    )

                else:
                    tournament_loaded = database.load_tournament("tournament")
                    database.save_tournament(
                        tournament_def, tournament_loaded, "tournament"
                    )
                    break
                    # faire autre actions

            #     if         #actions à faire suite au tournoi
            #         print("fin du tournoi ou autres actions (comme sauve)")
            #         tournament_def.date_end()
            #         sorted_players = tournament_def.sort_ranking(players_list)
            #         ranking = tournament_def.final_ranking(sorted_players)
            #         tournament_menu.display_final_ranking(ranking)
            #         database.save_tournament(tournament_def, "tournament")
            #         for i in players_list:
            #             i.set_score_to_score()
            # print("fini")


menu_tournament()
