from prettytable import PrettyTable


def players_reports(players_loaded):
    reports_players = PrettyTable()
    reports_players.field_names = [
        "IDENTIFIANT",
        "NOM",
        "PRENOM",
        "NOM COMPLET",
        "DATE DE NAISSANCE",
    ]
    for i in players_loaded["playertable"]:
        player_data = next(iter(i))
        player_list = [
            i[player_data].idplayer,
            i[player_data].name,
            i[player_data].forename,
            i[player_data].fullname,
            i[player_data].birthday,
        ]
        reports_players.add_row(player_list)
    reports_players.add_autoindex()
    print(reports_players)


def tournaments_reports(tournaments_loaded):
    reports_tournaments = PrettyTable()
    reports_tournaments.field_names = ["TOURNOI (nom)", "date debut", "date fin"]
    for i in tournaments_loaded["tournament_table"]:
        tournament_data = next(iter(i))
        tournament_list = [
            i[tournament_data].name,
            i[tournament_data].date_top,
            i[tournament_data].date_stop,
        ]
        reports_tournaments.add_row(tournament_list)
    reports_tournaments.add_autoindex()
    print(reports_tournaments)


def tournaments_reports_details(tournament_loaded, choice_details):
    reports_details_tournament = PrettyTable()
    if choice_details == 1:
        reports_details_tournament.field_names = [
            "Identifiant",
            "Nom",
            "Prénom",
            "Nom complet",
            "Date de naissance",
            "Score",
            "Rang",
        ]
        for i in tournament_loaded["registered_players"]:
            players_list = [
                i.idplayer,
                i.name,
                i.forename,
                i.fullname,
                i.birthday,
                i.score,
                i.rank,
            ]
            reports_details_tournament.add_row(players_list)
    else:
        reports_details_tournament.field_names = [
            "Tour",
            "Début du tour",
            "Fin du tour",
            "Liste des matchs",
        ]
        for i in tournament_loaded["list_round"]:
            print("nuage")
            print(i)
            rounds_list = [
                i.name,
                i.time_top,
                i.time_stop,
                i.matchs_round,
            ]
            reports_details_tournament.add_row(rounds_list)

    reports_details_tournament.add_autoindex()
    print(reports_details_tournament)

    # name = tournaments_loaded["name"]
    # date_top = tournaments_loaded["date_top"]
    # date_stop = tournaments_loaded["date_stop"]  # à corriger
    # colonne = [name, date_top, date_stop]
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
