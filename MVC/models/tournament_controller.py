### CONTROLLER ###
from Tournament_view import Tournament_View
from Tournament import Tournament
from Player_view import Player_View
from Player import Player, Players_Manager
from Round import Round
from Match import Match

tournament_choice = Tournament_View()
tournament_def = Tournament(tournament_choice.about_tournament())

adding_player = True
manager = Players_Manager()
while adding_player:
    add_player = str.upper(
        input("Incrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
    )
    try:
        if add_player == "O":
            player = Player(Player_View(manager).create_profile_player())
            players_list = tournament_def.get_players_list(player)
            print(f"player_list{players_list}")
        elif add_player == "N":
            adding_player = False
        else:
            raise ValueError("Entrée non valide")
    except ValueError as error:
        print("Erreur :", error)

# ajouter joueurs à tournoi
# players_ = tournament_def.get_players_list(players_list)
print(tournament_def.date_begin())

launch_round = True
count = 0
while count < 3:
    if launch_round:
        launch_new_round = tournament_choice.launch_new_round()
        if launch_new_round is False:
            break
        count += 1
        tournament_def.sort_ranking(players_list)
        current_round = tournament_def.get_current_round()
        first_round = Round(current_round)
        first_round.time_begin()
        print("classement")
        print(tournament_def.registered_players)
        print(tournament_def.registered_players)
        pairs_generated = first_round.pairs_generation(
            tournament_def.sort_ranking(players_list), tournament_def.test_round()
        )
        print(pairs_generated)  #  intégrer une view avant les matchs ?
        tournament_def.match_played(pairs_generated)
        print("OKOK")

        # lancer les matchs
        result_round = []
        for i in pairs_generated:
            match = Match(i)
            match.attribution_couleur(i)
            result_game = match.input_score(i)
            result_round.append(result_game)
        first_round.time_end()
        print("tesssst")
        result_round = first_round.results_round(result_round)
        print(result_round)
        update_tournament = tournament_def.update_last_round(result_round)
        print(update_tournament)
        print(tournament_def.list_round)
        tournament_def.update_score(result_round)

    else:
        print("fin du tournoi ou autres actions")


print(tournament_def)
# remonter les scores dans round correctement (pour le moment print None)
# attribuer les points à chaque joueurs
# maj classement
# lancer un nouveau tour
