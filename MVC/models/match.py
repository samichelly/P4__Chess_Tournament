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
        return f"{self.player1}({self.color1}) : {self.scoreP1} pts\n{self.player2}({self.color2}) : {self.scoreP2} pts"

    def attribution_couleur(self, paire):
        random_color_choice = random.choice([True, False])
        if random_color_choice is True:
            self.color1 = "Noir"
            self.color2 = "Blanc"
        else:
            self.color1 = "Blanc"
            self.color2 = "Noir"

    def input_score(self, paire):
        running = True
        while running:
            print(
                f"\nGagnant ?\n1 {self.player1}({self.color1})\n2 {self.player2}({self.color2})\n3 égalité"
            )
            result = input("Résultat : ")
            if result not in ["1", "2", "3"]:
                print("Entrée incorrecte")
            if result == "1":
                self.scoreP1 = 1
                return ([paire[0], 1], [paire[1], 0])
            elif result == "2":
                self.scoreP2 = 1
                return ([paire[0], 0], [paire[1], 1])
            else:
                self.scoreP1 = 0.5
                self.scoreP2 = 0.5
                return ([paire[0], 0.5], [paire[1], 0.5])
