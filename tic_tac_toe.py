# Initialise le plateau de jeu
    # 1. Crée une variable pour représenter le plateau de jeu.
    # 2. Choisis la taille du plateau (par exemple, 3x3) et initialise-le avec des valeurs par défaut.
    # 3. Assure-toi que chaque case du plateau est vide au début du jeu.

#///===FONCTIONS===\\\
    
    # Crée une fonction pour afficher le plateau de jeu
        # 1. Définis une fonction qui affiche le plateau de jeu.
        # 2. Utilise une boucle pour parcourir chaque ligne du plateau.
        # 3. À l'intérieur de la boucle, utilise une autre boucle pour parcourir chaque case de la ligne.
        # 4. Affiche le contenu de chaque case (X, O ou vide) avec des séparateurs.
        
    # Crée une fonction pour vérifier s'il y a un alignement gagnant
        # 1. Crée une fonction qui prend le plateau en entrée et vérifie s'il y a un alignement gagnant.
        # 2. Définis les conditions nécessaires pour qu'il y ait un alignement (horizontal, vertical, diagonal).
        # 3. Renvoie le symbole du joueur gagnant s'il y en a un, sinon renvoie un symbole indiquant l'absence de gagnant.

    # Crée une fonction pour vérifier si le plateau est plein
        # 1. Crée une fonction qui prend le plateau en entrée et vérifie si toutes les cases sont remplies.
        # 2. Renvoie une valeur indiquant si le plateau est plein ou non.


#///===BOUCLE PRINCIPAL DU JEU===\\\
    # Met en place la boucle principale du jeu
    # À chaque tour, affiche le plateau, prend l'entrée du joueur, met à jour le plateau
    
# Vérifie s'il y a un gagnant ou si le plateau est plein


#importation des modules pygame
import pygame, pygame_menu

# Définition de couleurs utilisées dans le jeu
BLACK= (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE= (0, 0, 255)
BLEU_CLAIR = (102, 255, 255)
PURPLE = (182, 48, 243)
GREY = (170, 166, 184)

pygame.init()

# Dimensions de la fenêtre
fenetre_largeur = 700
fenetre_hauteur = 480
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
pygame.display.set_caption("Tic-Tac-Toe")

#Initialisation du plateau du jeu
largeur_plateau = 950
hauteur_plateau = 650
taille_plateau = largeur_plateau * hauteur_plateau
une_case = (largeur_plateau // 3 * hauteur_plateau // 3)

# Fonction pour afficher le plateau de jeu
def afficher_plateau():
    fenetre.fill(WHITE) # Le fond de l'écran de jeu en blanc
    
    # Ma Grille en 3x3
    plateau = [['X', 'O', 'X'],
               ['O', ' ', 'O'],
               ['X', 'O', 'X']]
    
    # Taille et position des cases
    case_largeur, case_hauteur = une_case
    x, y = 50, 50
    
    # Boucle pour parcourir chaque ligne du plateau
    for ligne in plateau:
        # Boucle pour parcourir chaque case de la ligne
        for cases in ligne:
            pygame.draw.rect(fenetre, BLACK, (x, y, case_largeur, case_hauteur), 2)
            if cases != ' ':
                font = pygame.font.Font(None, 36)
                texte = font.render(cases, True, BLACK)
                fenetre.blit(texte, (x + case_largeur // 3, y + case_hauteur // 3))
            
            x += case_largeur
        x = 50
        y += case_hauteur
        
def verification_alignement_gagnant(jeu):
    global taille_plateau
    global une_case
    
    for v in taille_plateau:
        if v in taille_plateau.count('X'):
            return True
        
        if v in taille_plateau.count('O'):
            return True
        
        
    
    















# Initialisation du menu principal
menu = pygame_menu.Menu('Bienvenue', 700, 480, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Jouer au Pendu')
menu.add.button('Quitter', pygame_menu.events.EXIT)

# Lancement du menu
menu.mainloop(fenetre)

# Fermeture de Pygame
pygame.quit()




