class Plateau:
    def __init__(self):
        self.grille = [['' for _ in range(10)] for _ in range(10)]

    def placer_navire(self, navire, positions):
        for position in positions:
            x, y = position
            self.grille[x][y] = navire
            navire.ajouter_position(position)

    def afficher(self):
        for ligne in self.grille:
            print(' '.join(['.' if case == '' else 'N' for case in ligne]))