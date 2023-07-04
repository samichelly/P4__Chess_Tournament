# PROJET_4__JEU_ECHEC
Projet 4 OC : Jeu d'échec
Version testé avec Python : 3.11.3


## Installation 
1 - Cloner ce repository avec la commande `git clone https://github.com/samichelly/PROJET_3__JEU_ECHEC.git`
2 - Mettre en place un environnement virtuel et l'activer
3 - Installer les packages nécessaire au bon fonctionnement de l'application avec la commande `pip install -r requirements.txt`
4 - Se placer dans le dossier MVC et lancer le programme avec la commande `python main.py`

## Fonctionnement
Au démarrage, le menu propose 4 actions :

#### 1 - Consulter les rapports
Ce choix permet d'afficher un rapport, il en est existe 2 principaux :
a) Consulter l'ensemble des joueurs enregistrés dans le fichier des joueurs nationaux
b) Consulter les tournois créés précédemment
Il est existe un niveau de détail supplémentaire pour choix b) étant donné qu'il également possible de consulter :
- les joueurs participants à un tournoi
- le détails des tours et matchs d'un tournoi

#### 2 - Ajouter un nouveau joueur
Ce choix permet de créer un nouveau joueur qui sera enregistré dans la base de donnée nationale sans l'assigner à un tournoi.
Un contrôle d'unicité est réalisé afin de ne pas créer de joueur en doublon.

#### 3 - Créer un tournoi
Ce choix permet de créer un nouveau tournoi.
Il est possible d'ajouter des joueurs depuis la base de donnée nationale.
Il également possible d'ajouter un joueur inexistant directement dans le tournoi.
Ce joueur sera également enregistré dans la base de donnée nationale sans action de l'utlisateur.

#### 4 - Charger un tournoi
Ce choix permet de recharger un tournoi non terminé afin de pouvoir le continuer.
Il suffit pout cela d'indiquer l'index du tournoi souhaité à charger.
