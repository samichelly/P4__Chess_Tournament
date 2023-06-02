import random, re
import pandas as pd

"""
# Création Id aléatoire
liste_id_existant = [] # liste des identifiants existants
#liste_id_existant.append()
def id_aleatoire():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_id = random.randint(10000, 99999)
    char_id = ''.join(random.choice(alphabet) for _ in range(2))
    identifiant = char_id + str(number_id)
    # gérer l'unicité de l'id
    liste_id_existant.append(identifiant)
    return identifiant

#vérifier que l'id n'est pas doublon / et bon format

def match_J1_vs_J2(self, vainqueur, egalite):                   #à sortir de la classe
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
        # print(f"scoreJ1 : {self[0]} - {scoreJ1}   scoreJ2 : {self[1]} - {scoreJ2}")
        # print(vainqueur)
        # print(egalite)
        return vainqueur, egalite

"""
"""
class Joueur:                   #Ajouter un gestionnaire de joueur afin de récupérer chacun des joueurs ou bien transmettre chaque joueur à tournoi
    def __init__(self, IdJoueur, nomDeFamille, prenom, dateDeNaissance):
        # Ajouter validation données et contrôle unicité
         self.IdJoueur = IdJoueur
         self.nomDeFamille = nomDeFamille
         self.prenom = prenom
         self.dateDeNaissance = dateDeNaissance
    
    def input_joueur(self, IdJoueur, nomDeFamille, prenom, dateDeNaissance):
        self.IdJoueur = input("Entrer l'Identtifiant National du joueur :")
        self.nomDeFamille = input("Entrer le nom de famille du joueur :")
        self.prenom = input("Entrer le prénom du joueur :")
        self.dateDeNaissance = input("Entrer la date de naissance du joueur :")
  
J1 = Joueur("77777", "", "", "")
"""
dictionnaire = {"joueur1": 6, "joueur2": 1}


class Tournoi:
    def __init__(
        self,
        nom,
        lieu,
        dateDeDebut,
        dateDeFin,
        nbTours,
        nTourActuel,
        listeTour,
        dictionnaire,
        listeJoueursEnregistres,
        description,
    ):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nbTours = nbTours
        self.nTourActuel = nTourActuel
        self.listeTour = listeTour  # get objets class tour
        self.listeJoueursEnregistres = (
            listeJoueursEnregistres  # get objets class joueurs
        )
        self.description = description
        self.dictionnaire = dictionnaire
        colonne_tableau = ["idNatEchec", "nomDeFamille", "prenom", "score"]
        tableau = pd.DataFrame(columns=colonne_tableau)

    # créer tableau
    def listedesjoueurs(self, idNatEchec, nomDeFamille, prenom, tableau):
        score = 0.0
        tableau.loc[len(tableau)] = [idNatEchec, nomDeFamille, prenom, score]
        return tableau

    def classement(self, tableau):
        # pass
        tableau.sort_values(by=["score"], ascending=False, inplace=True)
        print(tableau)

    # Remplacer par __str__ ?
    def informations_tournoi(
        self, nom, lieu, dateDeDebut, dateDeFin, nbTours, nTourActuel
    ):  # , listeJoueursEnregistres):
        print(
            f"Tournoi {nom} à {lieu}, commence le {dateDeDebut} et se termine {dateDeFin}. Le tournoi est composé de {nbTours}. Tour actuel {nTourActuel}."
        )

    # def etablir_classement(self, nbTours, nTourActuel):  #ajouter joueur sous forme de dictionnaire
    #     if nbTours == nTourActuel:
    #         print("Le vainqueur est ")

    def getListJoueur(self):  # , listeJoueursEnregistres):
        # print(f"Liste des participants : \n{self}")
        return self

    def init_tours(self):
        # def nbToursTournoi(self, nbTours):
        pass

    def attribution_points(self, tableau):
        # pass
        # attribution des points dans tableau
        # trier pour obtenir un classement ordonné
        print(self[0])
        print(self[1])
        for _ in self[0]:
            # print(_)
            tableau.loc[[_], ["score"]] += 1

        for _ in self[1]:
            # print(_)
            tableau.loc[[_], ["score"]] += 0.5
        # print(tableau)
        return tableau


Tournoi.classement
