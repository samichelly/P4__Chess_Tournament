import pandas as pd
from datetime import date
from pprint import pprint

class joueur:
    def __init__(self, idNatEchec, nomDeFamille, prenom, dateDeNaissance, classement):    # score_cumule=0
         self.idNatEchec = idNatEchec
         self.nomDeFamille = nomDeFamille
         self.prenom = prenom
         self.dateDeNaissance = dateDeNaissance
         self.classement = classement
    
    def listedesjoueurs(self, idNatEchec, nomDeFamille, prenom):
        print(idNatEchec, nomDeFamille, prenom)
        return idNatEchec
    # def score_Joueurs(self, ):

class tournoi:
    def __init__(self, nom, lieu, dateDeDebut, dateDeFin, nbTours, nTourActuel, listeTour, listeJoueursEnregistres, description):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nbTours = nbTours
        self.nTourActuel = nTourActuel
        # self.listeTour = listeTour
        # self.listeJoueursEnregistres = listeJoueursEnregistres
        # self.description = description
    
    def informations_tournoi(self, nom, lieu, dateDeDebut, dateDeFin, nbTours, nTourActuel, listeJoueursEnregistres):
        print(f"Tournoi {nom} à {lieu}, commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}.")
    # def etablir_classement(self, nbTours, nTourActuel):  #ajouter joueur sous forme de dictionnaire
    #     if nbTours == nTourActuel:
    #         print("Le vainqueur est ")
    
    def getListJoueur(self, listeJoueursEnregistres):
        print(f"Liste des participants : {listeJoueursEnregistres}")
        return listeJoueursEnregistres

    def commencer_tour(self):
    # def nbToursTournoi(self, nbTours):
        pass
    

class tours:
    def __init__(self, idTours, Nom, dateHeureDeDebut,	dateHeureDeFin,	listMatch):
        self.idTours = idTours
        self.Nom = Nom
        self.dateHeureDeDebut = dateHeureDeDebut
        self.dateHeureDeFin = dateHeureDeFin
        self.listMatch = listMatch

    def liste_des_joueurs(self, listeParticipants):
        pass
    def generation_des_paires():
        pass
		
        #(ex : round X)


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
        




# for i in range(1, 8):
#     joueurs = [joueur.listedesjoueurs(i, i , "AAAAAAA", "AAAAAAA")]

joueurs = [joueur.listedesjoueurs(i, i , "AAAAAAA", "AAAAAAA") for i in range(1, 8)]
nombre_tour = input("Entrez le nombre de tours souhaitez pour ce tournoi :")
tournoi.informations_tournoi("Premier Tournoi", "Marseille", date.today(), "samedi", nombre_tour, 2, 6, joueurs)

# Listes_Joueurs_tournoi = joueur.listedesjoueurs()
Listes_Joueurs = tournoi.getListJoueur(joueurs, joueurs)


# test_joueur = joueur("AAAAAAA", "AAAAAAA", "AAAAAAA", "AAAAAAA")
# col = ("col1", "col2", "col3", "col4")
# test_jou = pd.DataFrame(columns=test_joueur)
# print(test_jou)


# joueur1 = joueur("AAAAAAA", "AAAAAAA", "AAAAAAA", "AAAAAAA")
# joueur2 = joueur("AAABBBB", "AAABBBB", "AAABBBB", "AAABBBB")
# nombre_tour = input("Entrez le nombre de tours souhaitez pour ce tournoi :")
# tournoi.informations_tournoi("Premier Tournoi", "Marseille", date.today(), "samedi", nombre_tour, 2, 6)


# test_paire = [joueur1, joueur2]
# match1 = match(test_paire)
# match1.opposition(test_paire)

# print(joueur1.prenom)
# print(joueur2)
