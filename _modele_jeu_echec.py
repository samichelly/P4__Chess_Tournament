import pandas as pd
from datetime import date
import random


# Création Id aléatoire
liste_id_existant = [] # liste des identifiants existants
#liste_id_existant.append()
def id_aleatoire():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_id = random.randint(100000, 999999)
    char_id = ''.join(random.choice(alphabet) for _ in range(2))
    identifiant = char_id + str(number_id)
    # gérer l'unicité de l'id
    liste_id_existant.append(identifiant)
    return identifiant


class joueur:
    def __init__(self, idNatEchec, nomDeFamille, prenom, dateDeNaissance, score, tableau):    # score_cumule=0
         self.idNatEchec = idNatEchec
         self.nomDeFamille = nomDeFamille
         self.prenom = prenom
         self.dateDeNaissance = dateDeNaissance
         self.score = score
         self.tableau = tableau
    
    def listedesjoueurs(self, idNatEchec, nomDeFamille, prenom, tableau):
        score = 0
        tableau.loc[len(tableau)] = [idNatEchec, nomDeFamille, prenom, score]
        return tableau
    # def score_Joueurs(self, ):

class tournoi:
    def __init__(self, nom, lieu, dateDeDebut, dateDeFin, nbTours, nTourActuel, listeTour, listeJoueursEnregistres, description, tableau):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nbTours = nbTours
        self.nTourActuel = nTourActuel
        self.tableau = tableau
        # self.listeTour = listeTour
        # self.listeJoueursEnregistres = listeJoueursEnregistres
        # self.description = description
    
    def informations_tournoi(self, nom, lieu, dateDeDebut, dateDeFin, nbTours, nTourActuel):#, listeJoueursEnregistres):
        print(f"Tournoi {nom} à {lieu}, commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}.")
    # def etablir_classement(self, nbTours, nTourActuel):  #ajouter joueur sous forme de dictionnaire
    #     if nbTours == nTourActuel:
    #         print("Le vainqueur est ")
    
    def getListJoueur(self):#, listeJoueursEnregistres):
        print(f"Liste des participants : \n{self}")
        return self

    def init_tours(self):
    # def nbToursTournoi(self, nbTours):
        pass

    def attribution_points(self, tableau):
        # pass
        #attribution des points dans tableau
        #trier pour obtenir un classement ordonné
        for _ in self[0]:
            print(_)
            tableau.loc[[_], ['score']] = 1
        print(tableau)
        # print(tableau)
        # gagnant = resultat[0]
        # egalite = resultat[1]
        # print(f"gagnants {gagnant}")
        # print(f"egalite {egalite}")
        # pass
    

class tours:
    def __init__(self, idTours, Nom, dateHeureDeDebut,	dateHeureDeFin,	listMatch, listeParticipants):
        self.idTours = idTours
        self.Nom = Nom
        self.dateHeureDeDebut = dateHeureDeDebut
        self.dateHeureDeFin = dateHeureDeFin
        self.listMatch = listMatch

    # def liste_des_joueurs(self, listeParticipants):
    #     pass
    def generation_des_paires(self, idTours):
        # pour chaque ligne du tableau, je veux constituer un tuple de 2 listes ([id, score], [id, score]) = match
        # for i in range(1, len(self), 2):
        #     opposition_match = [self['idNatEchec'].values[i], self['idNatEchec'].values[i+1]]
        #     print(opposition_match)
        paire_compil = []
        if idTours == 0:
            # random.shuffle(self)   #Faire un shuffle sur la colonne idNatEchec
            for i in range(0, len(self), 2):
                paire = [self['idNatEchec'].values[i], self['idNatEchec'].values[i+1]]
                paire_compil.append(paire)
            print(f"paire_compil : {paire_compil}")
            #     resultat = match_J1_vs_J2(paire)
            # print(f"Vainqueurs : {resultat}")
        else:
            print("OK")
        return paire_compil
        #     pass
        # print(listeParticipants)

        #(ex : round X)

vainqueur = []
egalite = []
class match:
    def __init__(self,paire):
        self.paire = paire
    
    def attribution_point_match(self, point):
        pass
    
    # def opposition(self, paire):
    #     J1 = paire[0]
    #     J2 = paire[1]
    #     match_J1_vs_J2(J1, J2)

    def match_J1_vs_J2(self):
        # print(f"self_match : {self}")
        scoreJ1 = scoreJ2 = 0
        opposition_match = ([self[0], scoreJ1], [self[1], scoreJ2])
        # print(f"opposition_match : {opposition_match}")
        scoreJ1 = 1
        # générateur de score aléatoire
        if scoreJ1 == 1:
            # print("J1 a gagné")
            vainqueur.append(self[0])
        elif scoreJ1 == scoreJ2:
            print("J1 et J2 ont fait match nul")
            egalite.append(self[0])
            egalite.append(self[1])
        else:
            print("J2 a gagné")
            vainqueur.append(self[1])
        # print(vainqueur)
        return vainqueur, egalite



        

liste_colonne = ["idNatEchec", "nomDeFamille", "prenom", "score"]
tableau = pd.DataFrame(columns=liste_colonne)
for i in range(1, 9):
    identifiant = id_aleatoire()
    joueur.listedesjoueurs(i, identifiant , "AAAAAAA", "AAAAAAA", tableau)
tableau = tableau.set_index(tableau['idNatEchec'])
print(tableau.index)

print(tableau)
# nombre_tour = input("Entrez le nombre de tours souhaitez pour ce tournoi :")
nombre_tour = 4
tournoi.informations_tournoi("Premier Tournoi", "Marseille", date.today(), "samedi", nombre_tour, 2, 6)
Listes_Joueurs = tournoi.getListJoueur(tableau)#, joueurs)
paire_compile = tours.generation_des_paires(Listes_Joueurs, 0)
# print(f"paire {paire_compile}")
for i in paire_compile:
    print(f"i :{i}")
    resultat = match.match_J1_vs_J2(i)
    # print(f"resultat : {resultat}")
tournoi.attribution_points(resultat, tableau)

    


