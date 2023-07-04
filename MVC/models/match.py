import random


class Match:
    def __init__(self, paire):
        self.player1 = paire[0]
        self.player2 = paire[1]
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.color1 = ""
        self.color2 = ""

    def __str__(self):
        return f"\n{self.player1} : {self.scoreP1} pts\n{self.player2} : {self.scoreP2} pts"

    def attribution_couleur(self):
        """attribute color for each player"""
        random_color_choice = random.choice([True, False])
        if random_color_choice is True:
            self.color1 = "Noir"
            self.color2 = "Blanc"
        else:
            self.color1 = "Blanc"
            self.color2 = "Noir"

    def input_score(self):
        """input result
        and returntuple ([self.player1, self.score1], [self.player2, self.score2])"""
        while True:
            print(
                f"\nGagnant ?\n1) {self.player1}({self.color1})\n2) {self.player2}({self.color2})\n3) égalité"
            )
            result = input("Résultat : ")
            if result not in ["1", "2", "3"]:
                print("Entrée incorrecte")
            if result == "1":
                self.scoreP1 = 1
                return ([self.player1, 1], [self.player2, 0])
            elif result == "2":
                self.scoreP2 = 1
                return ([self.player1, 0], [self.player2, 1])
            elif result == "3":
                self.scoreP1 = 0.5
                self.scoreP2 = 0.5
                return ([self.player1, 0.5], [self.player2, 0.5])
            else:
                continue
