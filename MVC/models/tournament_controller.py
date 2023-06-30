from tournament_view import Tournament_Menu, Tournament_Creation, Tournament_Reports
from tournament import Tournament
from create_player_view import Create_Player_View
from player import Player, Players_Manager
from round import Round
from match import Match
import database
import reports


def generate_reports():
    while True:
        choice_reports = Tournament_Reports().select_report()
        if choice_reports == 1:
            players_loaded = database.read_players_json("player")
            reports.players_reports(players_loaded)

        elif choice_reports == 2:
            tournament_loaded = database.read_tournament_json("tournament")
            reports.tournaments_reports(tournament_loaded)
            diplay_tournament_details = str.upper(
                input("Afficher des détails sur un tournoi\nO-Oui\nN-Non\nChoix : ")
            )
            if diplay_tournament_details == "O":
                select_tournament = input("Indiquer l'index du tournoi à afficher : ")
                choice_details = Tournament_Reports().tournament_details()
                if choice_details in [1, 2]:
                    tournament_details = database.load_tournament_json(
                        tournament_loaded, select_tournament
                    )
                    reports.tournaments_reports_details(
                        tournament_details, choice_details
                    )

                elif choice_details == "2":
                    tournament_loaded = database.read_tournament_json("tournament")
                    reports.tournaments_reports(tournament_loaded)

            if diplay_tournament_details == "N":
                break
        else:
            print("Erreur de sélection")


def add_player_to_db():
    while True:
        new_player = str.upper(
            input("\nIncrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
        )
        if new_player == "O":
            players_loaded = database.read_players_json("player")
            # print(players_loaded)
            # print("playersloaded")
            player = Player(Create_Player_View(manager=None).create_profile_player())
            database.save_player(player, players_loaded, "player")
        elif new_player == "N":
            break
        else:
            print("Erreur : Entrée non valide")


def create_tournament():
    tournament_def = Tournament(Tournament_Creation().about_tournament())
    tournament_loaded = database.read_tournament_json("tournament")
    database.save_tournament(tournament_def, tournament_loaded, "tournament")
    players_loaded = database.read_players_json("player")
    manager = Players_Manager()
    while True:
        add_player = str.upper(
            input(
                "\n1) Charger des joueurs\n2) Incrire un nouveau joueur\n3) Commencer le tournoi\n4) Quitter\nChoix : "
            )
        )

        if add_player == "1":
            reports.players_reports(players_loaded)
            input_players_selection = input(
                "\nIndiquer les Index séparés par une virgule et un espace : "
            )
            players_selection = input_players_selection.split(", ")
            players = database.load_player(players_loaded, players_selection)
            for i in players:
                player = Player(i)
                tournament_def.get_players_list(player)

        elif add_player == "2":
            while True:
                player = Player(
                    Create_Player_View(manager=None).create_profile_player()
                )
                database.save_player(player, players_loaded, "player")
                print(player)
                tournament_def.get_players_list(player)
                add_new_player = str.upper(
                    input("Ajouter un nouveau joueur :\nO-Oui\nN-Non\nChoix : ")
                )
                if add_new_player == "O":
                    pass
                elif add_new_player == "N":
                    break
                else:
                    print("Erreur : Entrée non valide")
        elif add_player == "3":
            return tournament_def
        elif add_player == "4":
            False
        else:
            print("Erreur : Entrée non valide")
        tournament_loaded = database.read_tournament_json("tournament")
        database.save_tournament(tournament_def, tournament_loaded, "tournament")


def load_tournament():
    reading_tournament = database.read_players_json("tournament")
    reports.tournaments_reports(reading_tournament)
    select_tournament = input(
        "\nIndiquer les Index séparés par une virgule et un espace : "
    )
    tournament_loaded = database.load_tournament_json(
        reading_tournament, select_tournament
    )
    print("chargement réussi")
    # Afficher un recap des informations précédentes
    return Tournament(tournament_loaded)


def competition(tournament_def):
    players_list = tournament_def.registered_players
    tournament_def.date_begin()
    while tournament_def.current_round < (tournament_def.nb_round - 1):
        launch_new_round = Tournament_Menu().launch_new_round()
        if launch_new_round is True:
            new_round = Round(tournament_def.get_current_round())
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
            tournament_loaded = database.read_tournament_json("tournament")
            database.save_tournament(tournament_def, tournament_loaded, "tournament")

            # lancer les matchs
            result_round = []
            for i in pairs_generated:
                match = Match(i)
                match.attribution_couleur(i)
                result_game = match.input_score(i)  #

                print(match)

                result_round.append(result_game)  #

            new_round.time_end()

            result_round = new_round.results_round(result_round)  #

            print(new_round)
            print(result_round)

            #########

            tournament_def.update_last_round(new_round)
            del new_round

            #########

            # print(update_tournament)
            # print(tournament_def.list_round)

            tournament_def.update_score(result_round)  #

            tournament_loaded = database.read_tournament_json("tournament")
            database.save_tournament(tournament_def, tournament_loaded, "tournament")

        else:
            tournament_loaded = database.read_tournament_json("tournament")
            database.save_tournament(tournament_def, tournament_loaded, "tournament")
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


def menu_tournament():
    while True:
        menu = Tournament_Menu().menu_tournament()
        if menu == 1:
            generate_reports()
        elif menu == 2:
            add_player_to_db()
        elif menu == 3:
            tournament_def = create_tournament()
            competition(tournament_def)
        elif menu == 4:
            tournament_def = load_tournament()
            competition(tournament_def)
        elif menu == 5:
            break
        else:
            print("Error selection")


menu_tournament()
