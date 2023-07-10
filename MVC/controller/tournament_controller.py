from view.tournament_view import (
    Tournament_Menu,
    Tournament_Creation,
    Tournament_Reports,
)
from view.create_player_view import Create_Player
from models.tournament import Tournament
from models.player import Player
from controller.player_controller import Players_Manager
from models.round import Round
from models.match import Match
from database.database import Database
from view.reports import Reports


class Tournament_Controller:
    def generate_reports(self, menu, database, reports):
        """generate reports about players, tournaments"""
        create_reports = Tournament_Reports()
        while True:
            choice_reports = create_reports.select_report()
            if choice_reports == 1:
                players_loaded = database.read_players_json()
                if players_loaded is not None:
                    reports.all_players_reports(players_loaded)
                break

            elif choice_reports == 2:
                tournament_loaded = database.read_tournament_json()
                if tournament_loaded is not None:
                    reports.tournaments_reports(tournament_loaded)
                    display_detail = create_reports.display_tournament_details()
                    if display_detail == "O":
                        select_tournament = create_reports.select_tournament_details()
                        choice_details = create_reports.tournament_details()
                        if choice_details in [
                            1,
                            2,
                        ]:  # 1 for players, 2 for rounds/matches
                            tournament_details = database.load_tournament_json(
                                tournament_loaded, select_tournament
                            )
                            reports.tournaments_reports_details(
                                tournament_details, choice_details
                            )
                        break

                    elif display_detail == "N":
                        break

                    else:
                        menu.invalid_value()

                break

    def add_player_to_db(self, menu, database):
        """add player to db"""
        while True:
            new_player = menu.add_new_player()
            if new_player == "O":
                manager = Players_Manager()
                players_loaded = database.read_players_json()
                if players_loaded is not None:
                    id_exists = manager.check_id_unicity(players_loaded)
                    player_creation = Create_Player(id_exists).create_profile_player()
                    if player_creation is not None:
                        player = Player(player_creation)
                        database.save_player(player, players_loaded)
                        return player
                else:
                    player = Player(
                        Create_Player(id_exists=None).create_profile_player()
                    )
                    database.save_player(player, players_loaded)
                    return player
            elif new_player == "N":
                break
            else:
                menu.invalid_value()

    def create_tournament(self, menu, database, reports):
        """create tournament to play it"""
        creation_tournament = Tournament_Creation()
        tournament_def = Tournament(creation_tournament.about_tournament())
        tournament_loaded = database.read_tournament_json()
        database.save_tournament(tournament_def, tournament_loaded)
        players_loaded = database.read_players_json()
        while True:
            add_player = creation_tournament.add_player_to_tournament()

            if add_player == "1":
                reports.all_players_reports(players_loaded)
                input_players_selection = (
                    creation_tournament.load_players_to_tournament()
                )
                players_selection = input_players_selection.split(" ")
                players = database.load_player(players_loaded, players_selection)
                for i in players:
                    player = Player(i)
                    tournament_def.get_players_list(player)

            elif add_player == "2":
                player = self.add_player_to_db()
                print(player)
                tournament_def.get_players_list(player)
            elif add_player == "3":
                test_players_in = tournament_def.get_players()
                if len(test_players_in) != 0:
                    return tournament_def
                creation_tournament.error_no_player()
                continue
            else:
                menu.invalid_value()
            tournament_loaded = database.read_tournament_json()
            database.save_tournament(tournament_def, tournament_loaded)

    def load_tournament(self, menu, database, reports):
        """load tournament to play it"""
        reading_tournament = database.read_tournament_json()
        if reading_tournament is not None:
            reports.tournaments_reports(reading_tournament)
            select_tournament = menu.select_tournament_to_load()
            tournament_loaded = database.load_tournament_json(
                reading_tournament, select_tournament
            )
            tournament_def = Tournament(tournament_loaded)
            tournament_def.display_ranking()
            return tournament_def
        else:
            return None

    def competition(self, tournament_def, menu, database):
        """play rounds and matches"""
        tournament_def.date_begin()
        while tournament_def.current_round < (tournament_def.nb_round):
            launch_new_round = menu.launch_new_round()
            if launch_new_round is True:
                # round
                players_list = tournament_def.get_players()
                new_round = Round(tournament_def.get_current_round())
                new_round.time_begin()
                print(new_round)
                if new_round.idround == 1:
                    players_list = tournament_def.shuffle_players()
                pairs_generated = new_round.pairs_generation(
                    players_list,
                    tournament_def.test_rematch(),
                )
                tournament_def.match_played(pairs_generated)
                new_round.clean_exempt_match(pairs_generated)

                # matches
                result_round = []
                for i in pairs_generated:
                    match = Match(i)
                    match.attribution_couleur()
                    result_game = match.input_score()
                    print(match)
                    new_round.get_match(match)
                    result_round.append(result_game)

                # update
                new_round.time_end()
                result_round = new_round.results_round(result_round)
                print(new_round)
                tournament_def.update_last_round(new_round)
                tournament_def.sort_score(players_list)
                del new_round
                tournament_def.update_score(result_round)
                tournament_def.display_ranking()
                if tournament_def.current_round == (tournament_def.nb_round - 1):
                    tournament_def.date_end()
                tournament_loaded = database.read_tournament_json()
                database.save_tournament(tournament_def, tournament_loaded)
            else:
                break

        if tournament_def.current_round == (tournament_def.nb_round):
            print("Tournoi terminé : Classement final")
            tournament_def.display_ranking()

    def menu_tournament(self):
        while True:
            menu = Tournament_Menu()
            database = Database()
            reports = Reports()
            menu_choice = menu.menu_tournament()
            if menu_choice == 1:
                self.generate_reports(menu, database, reports)
            elif menu_choice == 2:
                self.add_player_to_db(menu, database)
            elif menu_choice == 3:
                tournament_def = self.create_tournament(menu, database, reports)
                self.competition(tournament_def, menu, database)
            elif menu_choice == 4:
                tournament_def = self.load_tournament(menu, database, reports)
                if tournament_def is not None:
                    self.competition(tournament_def, menu, database)
