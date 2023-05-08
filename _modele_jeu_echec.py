import pandas as pd
from datetime import date
import random, re


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
        score = 0.0
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
        # print(f"Liste des participants : \n{self}")
        return self

    def init_tours(self):
    # def nbToursTournoi(self, nbTours):
        pass

    def attribution_points(self, tableau):
        # pass
        #attribution des points dans tableau
        #trier pour obtenir un classement ordonné
        print(self[0])
        print(self[1])
        for _ in self[0]:
            # print(_)
            tableau.loc[[_], ['score']] += 1

        for _ in self[1]:
            # print(_)
            tableau.loc[[_], ['score']] += 0.5
        # print(tableau)
        return tableau
    
    def classement(self):
        # pass
        print(self)
        self.sort_values(by=['score'], ascending = False, inplace = True)
        print(self)
        # print(f"classement trié : \n {self}")
        #trier pour obtenir un classement ordonné
    

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
        # print(f"ggg: {self}")
        paire_compil = []
        if idTours in [0, 1]:
            # self.sample(frac=1)
            # print(self)
            # random.shuffle(self)   #Faire un shuffle sur la colonne idNatEchec
            for i in range(0, len(self), 2):
                paire = [self['idNatEchec'].values[i], self['idNatEchec'].values[i+1]]
                paire_compil.append(paire)
            # print(f"paire_compil : {paire_compil}")
            #     resultat = match_J1_vs_J2(paire)
            # print(f"Vainqueurs : {resultat}")
        else:
            for i in range(0, len(self), 2):
                paire = [self['idNatEchec'].values[i], self['idNatEchec'].values[i+1]]
                paire_compil.append(paire)
        return paire_compil
        #     pass

        #(ex : round X)

vainqueur = []
egalite = []
class match:
    def __init__(self,paire):
        self.paire = paire
    
    def attribution_point_match(self, point):
        pass
    
    def match_J1_vs_J2(self, vainqueur, egalite):                       #gérer le problème de scoreJ2
        # print(f"self_match : {self}")
        scoreJ1 = scoreJ2 = 0.0
        opposition_match = ([self[0], scoreJ1], [self[1], scoreJ2])
        # générateur de score aléatoire
        score_possible = 0.0, 0.5, 1.0
        scoreJ1 = random.sample(score_possible, 1)
        # print(f"score : {self[0]} - {scoreJ1}")
        if scoreJ1 == [0.0]:
            scoreJ2 = 1.0
            vainqueur.append(self[1])
        elif scoreJ1 == [0.5]:
            scoreJ2 = 0.5
            egalite.extend(self)
        else:
            scoreJ2 = 0.0
            vainqueur.append(self[0])
        print(f"scoreJ1 : {self[0]} - {scoreJ1}   scoreJ2 : {self[1]} - {scoreJ2}")
        print(vainqueur)
        print(egalite)
        return vainqueur, egalite


   

liste_colonne = ["idNatEchec", "nomDeFamille", "prenom", "score"]
tableau = pd.DataFrame(columns=liste_colonne)
for i in range(6):
    identifiant = id_aleatoire()
    joueur.listedesjoueurs(i, identifiant , f"AAAAAAA{i}", f"BBB{i}", tableau)
tableau = tableau.set_index(tableau['idNatEchec'])
# tableau.drop('idNatEchec', columns='idNatEchec')       #supprimer colonne "idNatEchec"
# print(tableau)

# print(tableau)
# nombre_tour = input("Entrez le nombre de tours souhaitez pour ce tournoi :")
nombre_tour = 3
# tournoi.informations_tournoi("Premier Tournoi", "Marseille", date.today(), "samedi", nombre_tour, 2, 6)
Listes_Joueurs = tournoi.getListJoueur(tableau)#, joueurs)

for _ in range(nombre_tour):
    paire_compile = tours.generation_des_paires(Listes_Joueurs, 0)
    # print(f"paire {paire_compile}")
    vainqueur = []
    egalite = []
    for i in paire_compile:
        # print(f"i :{i}")
        # resultat = []
        resultat = match.match_J1_vs_J2(i, vainqueur, egalite)
        # print(type(resultat))
        #[match.match_J1_vs_J2(i)]
    print(f"resultat : {resultat}")
    tableau_maj = tournoi.attribution_points(resultat, tableau)
    # print(tableau_maj)
    ranking = tournoi.classement(tableau_maj)
    # print(ranking)