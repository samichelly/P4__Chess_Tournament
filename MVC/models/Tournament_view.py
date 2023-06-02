class Tournament_View:
    def __init__(self):
        self.tournament = self.select_tournament()
        self.name = self.name_tournament()
        self.place = self.place_tournament()
        self.number_round = self.number_of_round()
        self.description = self.description_tournament()

    def select_tournament(self):
        running = True
        while running:
            select = input("1 créer un tournoi\n2 charger un tournoi\nChoix :")
            if select == "1":  # possible erreur
                # creer un tournoi
                running = False
                # self.dict_tournament['select_type'] = select
                # return select
            elif select == "2":  # possible erreur
                # charger un tournoi
                running = False
                # self.dict_tournament['select_type'] = select
                # return select
            else:
                print("Entrée non valide")

    def name_tournament(self):
        self.name = input("\nEntrez le nom du tournoi : ")
        return self.name

    def place_tournament(self):
        self.place = input("Entrez le lieu : ")
        return self.place

    def number_of_round(self):
        nb_round = input("Indiquez le nombre de tour qui compose le tournoi :")
        if nb_round.isnumeric() is False:
            print("Erreur de saisi. Le tournoi sera de 4 tours par défaut")
            self.number_round = 4
        else:
            print(f"le tournoi sera de {nb_round} tour(s)")
            self.number_round = nb_round
        return self.number_round

        # Envoyer vers le controlleur pour vérification

    def description_tournament(self):
        self.description = input("Entrez une description : ")
        return self.description

    def display_final_ranking(self, dic_joueur):  # get profil des joueurs
        print("\nClassement final :\n")
        # table_head =
        # final_ranking = pd.DataFrame(columns=)

        # create dataframe

    def launch_new_round(self):
        running = True
        while running:
            new_round = str.upper(
                input("Lancez un nouveau tour ?\n O -oui\n N -non\nChoix : ")
            )
            if new_round == "O":  # possible erreur
                running = False
                return True
            elif new_round == "N":  # possible erreur
                running = False
                return False
            else:
                print("Entrée non valide")

    def about_tournament(self):
        return [self.name, self.place, self.number_round, self.description]


# tt = Tournament_View()
# print(tt.about_tournament())
