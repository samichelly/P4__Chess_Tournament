class Tournament_Menu:
    def menu_tournament(self):
        while True:
            select = int(
                input(
                    "\n1) Consulter les rapports\n2) Ajouter de nouveau joueur\n"
                    "3) Créer un tournoi\n4) Charger un tournoi\n5) Quitter l'interface\nChoix : "
                )
            )
            if select in {1, 2, 3, 4, 5}:
                return select
            else:
                print("Entrée non valide")

    def launch_new_round(self):
        while True:
            new_round = str.upper(
                input("\nLancer un nouveau tour ? O-oui / N-non\nChoix : ")
            )
            if new_round == "O":
                return True
            elif new_round == "N":
                return False
            else:
                print("Entrée non valide")

    def display_final_ranking(self, table):  # get profil des joueurs
        print("\nClassement final :\n")
        print(table)


class Tournament_Reports:
    def select_report(self):
        return int(input(
            "\nGénérer un rapport :\n1) Liste de tous les joueurs\n2) Liste de tous les tournois\nChoix : "
        ))
    
    def tournament_details(self):
        return int(input(
            "\nAfficher les détails d'un tournoi :\n1) Liste joueurs\n2) Liste matchs et tours\n3) Quitter\nChoix : "
        ))


class Tournament_Creation:
    def __init__(self):
        self.name = self._name_tournament()
        self.place = self._place_tournament()
        self.number_round = self._number_of_round()
        self.description = self._description_tournament()

    def _name_tournament(self):
        while True:
            self.name = input("\nEntrez le nom du tournoi : ")
            if self.name != "":
                False
                return self.name
            else:
                print("Veuillez entrer un nom")

    def _place_tournament(self):
        self.place = input("Entrez le lieu : ")
        return self.place

    def _number_of_round(self):
        nb_round = input("Indiquez le nombre de tour qui compose le tournoi : ")
        if nb_round.isnumeric() is False:
            self.number_round = 4
            print(f"Entrée non valide. Tournoi de {self.number_round} tours")
        else:
            self.number_round = int(nb_round)
            print(f"le tournoi sera de {self.number_round} tour(s)")
        return self.number_round

    def _description_tournament(self):
        self.description = input("Entrez une description : ")
        return self.description

    def about_tournament(self):
        return {
            "name": self.name,
            "place": self.place,
            "date_top": "",
            "date_stop": "",
            "nb_round": self.number_round,
            "current_round": 0,
            "list_round": [],
            "registered_players": [],
            "id_match_played": [],
            "description": self.description,
        }
