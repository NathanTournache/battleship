from joueur import Joueur

def main():
    joueur1 = Joueur("Joueur 1")
    joueur2 = Joueur("Ordinateur")

    # Exemple de placement de navires pour le joueur 1
    joueur1.ajouter_navire(5, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    joueur1.ajouter_navire(4, [(2, 0), (2, 1), (2, 2), (2, 3)])
    joueur1.ajouter_navire(3, [(4, 0), (4, 1), (4, 2)])
    joueur1.ajouter_navire(3, [(6, 0), (6, 1), (6, 2)])
    joueur1.ajouter_navire(2, [(8, 0), (8, 1)])
    joueur1.ajouter_navire(2, [(9, 0), (9, 1)])

    # Afficher le plateau du joueur 1
    joueur1.afficher_plateau()

if __name__ == "__main__":
    main()