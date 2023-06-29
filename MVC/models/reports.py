from prettytable import PrettyTable


def players_reports(players_loaded):
    reports_players = PrettyTable()
    reports_players.field_names = [
        "idplayer",
        "name",
        "forename",
        "fullname",
        "birthday",
        "score",
        "rank",
    ]
    for i in players_loaded["playertable"]:
        player_data = next(iter(i))
        player_list = [
            i[player_data].idplayer,
            i[player_data].name,
            i[player_data].forename,
            i[player_data].fullname,
            i[player_data].birthday,
            i[player_data].score,
            i[player_data].rank,
        ]
        reports_players.add_row(player_list)
    reports_players.add_autoindex()
    print(reports_players)


def tournaments_reports(tournaments_loaded):
    reports_tournaments = PrettyTable()
    reports_tournaments.field_names = ["name", "date top", "date stop"]
    for i in tournaments_loaded["tournament"]:      #à corriger
        # player_data = next(iter(i))
        # player_list = [
        #     i[player_data].idplayer,
        #     i[player_data].name,
        #     i[player_data].forename,
        #     i[player_data].fullname,
        #     i[player_data].birthday,
        #     i[player_data].score,
        #     i[player_data].rank,
        # ]
        reports_tournaments.add_row(player_list)
    print(reports_tournaments)
