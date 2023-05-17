import random
"""
class Joueur:
    def __init__(self, IdJoueur, nomDeFamille, prenom, dateDeNaissance):    # score_cumule=0
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
# print(J1._IdJoueur)
    # ajouter les property

    #Regarder comment ne pas modifier les attributs à l'extérieur. + attribut de classe
"""

"""
class Tournoi:
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
        # print(self)
        self.sort_values(by=['score'], ascending = False, inplace = True)
        print(self)
        # print(f"classement trié : \n {self}")
        #trier pour obtenir un classement ordonné


class Tours:
    def __init__(self, idTours, Nom, dateHeureDeDebut,	dateHeureDeFin,	listMatch, listeParticipants):
        self.idTours = idTours
        self.Nom = Nom
        self.dateHeureDeDebut = dateHeureDeDebut
        self.dateHeureDeFin = dateHeureDeFin
        self.listMatch = listMatch

    # def liste_des_joueurs(self, listeParticipants):
    #     pass
    def generation_des_paires(self, tableau = []):
        # pour chaque ligne du tableau, je veux constituer un tuple de 2 listes ([id, score], [id, score]) = match
        # print(f"ggg: {self}")
        print(self)
        paire_compil = []
        #if tableau vide, je fais autre chose
        if tableau == []:
            self.sample(frac=1, axis = 0)     #Le mélange ne fonctionne pas
            print(self)
            # random.shuffle(self)   #Faire un shuffle sur la colonne IdJoueur
            # print(f"Vainqueurs : {resultat}")
        # else:
            # print("idTours2")
        for i in range(0, len(self), 2):
            paire = [self['IdJoueur'].values[i], self['IdJoueur'].values[i+1]]
            paire_compil.append(paire)
        return paire_compil
        #     pass
        #(ex : round X)

"""
class Match:
    def __init__(self,paire):
        self.joueur1 = paire[0]
        self.joueur2 = paire[1]
        self.scoreJ1 = 0
        self.scoreJ2 = 0
        self.couleurJ1 = ""
        self.couleurJ2 = ""
        
    def attribution_point(self, paire):
        scoreJ1 = input(f"Indiquer le score obtenu par {paire[0]} :")
        scoreJ2 = input(f"Indiquer le score obtenu par {paire[1]} :")
        print(f"Le joueur {paire[0]} a obtenu {scoreJ1} point, le joueur {paire[1]} a obtenu {scoreJ2} point")
        return ([paire[0], scoreJ1], [paire[1], scoreJ2])
    
    def attribution_couleur(self, paire):     #Supprimer les [] pour couleurJ1
        couleur = "Blanc", "Noir"
        couleurJ1 = random.sample(couleur, 1)
        if couleurJ1 == ["Blanc"]:
            couleurJ2 = "Noir"
        else:
            couleurJ2 = "Blanc"
        return print(f"{paire[0]} joue en {couleurJ1}, {paire[1]} joue en {couleurJ2}")


match1 = Match(['AAAAAA', 'BBBBBB'])
match1.attribution_couleur(['AAAAAA', 'BBBBBB'])
resultat_match = match1.attribution_point(['AAAAAA', 'BBBBBB'])