from plateau import Plateau
from navire import Navire

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.plateau = Plateau()
        self.navires = []

    def ajouter_navire(self, taille, positions):
        navire = Navire(taille)
        self.plateau.placer_navire(navire, positions)
        self.navires.append(navire)

    def afficher_plateau(self):
        self.plateau.afficher()