### CONTROLLER ###
from Tournament_view import Tournament_View
from Tournament import Tournament
from Player_view import Player_View
from Player import Player, Players_Manager
from Round import Round
from Match import Match

tournament_choice = Tournament_View()
tournament_def = Tournament(tournament_choice.about_tournament())

# condition, ajoutez un nouveau joueur ?
# si oui, relancer la boucle while
# sinon passer à la suite
adding_player = True
manager = Players_Manager()
while adding_player:
    add_player = input("Incrivez un nouveau joueur ? O-Oui / N-Non\nChoix : ")
    try:
        if add_player == "O":
            player = Player(Player_View(manager).create_profile_player())
            # player.profile_player()
            # print(f"player  {player}")
            # print(f"player_profile  {player.profile_player()}")
            players_list = manager.create_players_list(player.shorted_player_profile())
            print(f"player_list{players_list}")
        elif add_player == "N":
            adding_player = False
        else:
            raise ValueError("Entrée non valide")
    except ValueError as error:
        print("Erreur :", error)


# ajouter joueurs à tournoi
players_ = tournament_def.get_players_list(players_list)
print(tournament_def.date_begin())

# classer les joueurs
players_ranked = tournament_def.sort_ranking(players_)

# créer le premier tour
launch_round = tournament_choice.launch_new_round()
if launch_round is True:
    current_round = tournament_def.get_current_round()
    first_round = Round(current_round)
    first_round.time_begin()
    pairs_generated = first_round.pairs_generation(
        players_ranked, tournament_def.test_round()
    )
    print(pairs_generated)  #  intégrer une view avant les matchs ?
    tournament_def.match_played(pairs_generated)
    print("OKOK")

    # lancer les matchs
    for _ in pairs_generated:
        match = Match(_)
        match.attribution_couleur(_)
        result_game = match.input_score(_)
        result_round = [result_game]
    first_round.results_round(result_round)
    print(first_round.listMatch)
