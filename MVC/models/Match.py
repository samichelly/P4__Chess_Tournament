import random

# from Round import Round


class Match:
    def __init__(self, paire):
        self.player1 = paire[0]
        self.player2 = paire[1]
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.couleurJ1 = ""
        self.couleurJ2 = ""

    def attribution_couleur(self, paire):
        random_color_choice = random.choice([True, False])
        if random_color_choice is True:
            color1 = "Blanc"
            color2 = "Noir"
        else:
            color2 = "Blanc"
            color1 = "Noir"
        print(f"{self.player1} est {color1}, {self.player2} est {color2}")

    def input_score(self, paire):  # à retourner dans les resultats de Tour
        running = True
        while running:
            print(f"\n1- {self.player1} gagne\n2- {self.player2} gagne\n3- égalité\n")
            result = input("Résultat : ")
            try:
                if result in ["1", "2", "3"]:
                    if result == "1":
                        return ([paire[0], 1], [paire[1], 0])
                    elif result == "2":
                        return ([paire[0], 0], [paire[1], 1])
                    else:
                        return ([paire[0], 0.5], [paire[1], 0.5])
                else:
                    raise ValueError("\nEntrée incorrecte\n")
            except ValueError as error:
                print("Erreur :", error)


m = Match(["FFFF", "KKK"])
m.attribution_couleur(["FFFF", "KKK"])
test = m.input_score(["FFFF", "KKK"])
print(test)


# match1 = Match(["AAAAAA", "BBBBBB"])
# match1.attribution_couleur(["AAAAAA", "BBBBBB"])
# resultat_match = match1.attribution_point(["AAAAAA", "BBBBBB"])


# paire = [12, 67]
# match1 = Match(paire)
# match1.input_score(paire)
