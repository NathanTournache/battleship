class Navire:
    def __init__(self, taille):
        self.taille = taille
        self.positions = []
        self.touche = 0

    def ajouter_position(self, position):
        self.positions.append(position)

    def est_touche(self):
        self.touche += 1

    def est_coule(self):
        return self.touche == self.taille