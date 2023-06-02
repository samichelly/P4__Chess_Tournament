import random

# from Round import Round


class Match:
    def __init__(self, paire):
        self.player1 = paire[0]
        self.player2 = paire[1]
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.color1 = ""
        self.color2 = ""

    def attribution_couleur(self, paire):
        random_color_choice = random.choice([True, False])
        if random_color_choice is True:
            self.color1 = "Noir"
            self.color2 = "Blanc"
        else:
            self.color1 = "Blanc"
            self.color2 = "Noir"
        print(f"{self.player1} est {self.color1}, {self.player2} est {self.color2}")

    def input_score(self, paire):  # à retourner dans les resultats de Tour
        running = True
        while running:
            print(f"\nGagnant ?\n1 {self.player1}\n2 {self.player2}\n3 égalité")
            result = input("Résultat : ")
            try:
                if result not in ["1", "2", "3"]:
                    raise ValueError("Entrée incorrecte")
                if result == "1":
                    return ([paire[0], 1], [paire[1], 0])
                elif result == "2":
                    return ([paire[0], 0], [paire[1], 1])
                else:
                    return ([paire[0], 0.5], [paire[1], 0.5])
                # else:

            except ValueError as error:
                print("Erreur :", error)


# m = Match(["FFFF", "KKK"])
# m.attribution_couleur(["FFFF", "KKK"])
# test = m.input_score(["FFFF", "KKK"])
# print(test)


# match1 = Match(["AAAAAA", "BBBBBB"])
# match1.attribution_couleur(["AAAAAA", "BBBBBB"])
# resultat_match = match1.attribution_point(["AAAAAA", "BBBBBB"])


# paire = [12, 67]
# match1 = Match(paire)
# match1.input_score(paire)
