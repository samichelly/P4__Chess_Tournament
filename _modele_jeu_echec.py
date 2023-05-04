class joueur:
    def __init__(self, idNatEchec, nomDeFamille, prenom, dateDeNaissance):
         self.idNatEchec = idNatEchec
         self.nomDeFamille = nomDeFamille
         self.prenom = prenom
         self.dateDeNaissance = dateDeNaissance
        #  self.score_total = score_total

def match_J1_vs_J2(J1, J2):
    resultat_J1 = resultat_J2 = 0
    # générateur de score aléatoire
    resultat_J1 = 0
    resultat_J2 = 0
    if resultat_J1 == 1:
        print("J1 a gagné")
    elif resultat_J1 == resultat_J2:
        print("J1 et J2 ont fait match nul")
    else:
        print("J2 a gagné")
    return resultat_J1, resultat_J2

class match:
    def __init__(self,paire):
        self.paire = paire

    def opposition(self, paire):
        J1 = paire[0]
        J2 = paire[1]
        match_J1_vs_J2(J1, J2)
        
        

joueur1 = joueur("AAAAAAA", "AAAAAAA", "AAAAAAA", "AAAAAAA")
joueur2 = joueur("AAABBBB", "AAABBBB", "AAABBBB", "AAABBBB")

test_paire = [joueur1, joueur2]
match1 = match(test_paire)
match1.opposition(test_paire)

# print(joueur1.prenom)
# print(joueur2)

# class tournoi:
#     def __init__(self) -> None:


# class tours:
#     def __init__(self, 	idTours,	Nom,	dateHeureDeDebut,	dateHeureDeFin,	listMatch) -> None:
# 		#(ex : round X)







