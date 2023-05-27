### CONTROLLER ###
from datetime import date
from datetime import datetime
from view import Tournament as Trn
from models import Tournoi


class DateTime:
    def get_day(self):
        return date.today().strftime("%d/%m/%Y")

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")


choice = Trn().select_tournament()
if choice == 1:
    tournament_info = Trn().about_tournament()
    nb_round = Trn().number_of_round()
    print(tournament_info)
    tournoi = Tournoi()
    print(tournoi)
    # tournoi.__init__(
    #     tournament_info[0], tournament_info[1], tournament_info[2], nb_round
    # )
    # tournoi.informations_tournoi()

elif choice == 2:
    print("Chargement tournoi")
else:
    print("Error")
