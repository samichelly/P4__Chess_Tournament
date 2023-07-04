from prettytable import PrettyTable


def all_players_reports(players_loaded):
    """report of all players added in national file"""
    reports_players = PrettyTable()
    reports_players.title = "Listes des joueurs nationaux"
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
    """report short informations about all tournament"""
    reports_tournaments = PrettyTable()
    reports_tournaments.title = "Listes des tournois"
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
    """report full informations about one tournament
    informations about players or rounds and matches"""
    reports_details_tournament = PrettyTable()
    if choice_details == 1:
        reports_details_tournament.title = "Listes des joueurs du tournois"
        reports_details_tournament.field_names = [
            "Identifiant",
            "Nom",
            "Prénom",
            "Nom complet",
            "Date de naissance",
            "Score",
        ]
        for i in tournament_loaded["registered_players"]:
            players_list = [
                i.idplayer,
                i.name,
                i.forename,
                i.fullname,
                i.birthday,
                i.score,
            ]
            reports_details_tournament.add_row(players_list)
        reports_details_tournament.sortby = "Score"
        reports_details_tournament.reversesort = True
    else:
        reports_details_tournament.title = "Listes des tours/matchs du tournois"
        reports_details_tournament.field_names = [
            "Tour",
            "Début du tour",
            "Fin du tour",
            "Joueur 1",
            "Score J1",
            "VS",
            "Score J2",
            "Joueur 2",
        ]
        for i in tournament_loaded["list_round"]:
            for j in i.obj_matches:
                match_resulat = [
                    j.player1,
                    j.scoreP1,
                    j.scoreP2,
                    j.player2,
                ]
                rounds_list = [
                    i.name,
                    i.time_top,
                    i.time_stop,
                    match_resulat[0],
                    match_resulat[1],
                    "VS",
                    match_resulat[2],
                    match_resulat[3],
                ]

                reports_details_tournament.add_row(rounds_list)
        reports_details_tournament.add_autoindex()
    print(reports_details_tournament)
