# Importation des modules pygame
import pygame, pygame_menu
import sys

# Définition de couleurs utilisées dans le jeu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLEU_CLAIR = (102, 255, 255)
PURPLE = (182, 48, 243)
GREY = (170, 166, 184)

pygame.init()

# Dimensions de la fenêtre
fenetre_largeur = 700
fenetre_hauteur = 480
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialisation du plateau du jeu
largeur_plateau = 950
hauteur_plateau = 650
taille_plateau = largeur_plateau * hauteur_plateau
une_case = (largeur_plateau // 3 * hauteur_plateau // 3)

# Fonction pour afficher le plateau de jeu
def afficher_plateau():
    fenetre.fill(WHITE)  # Le fond de l'écran de jeu en blanc

    # Ma Grille en 3x3
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(fenetre, BLACK, (i * une_case[0], j * une_case[1], une_case[0], une_case[1]), 2)
            if plateau[j][i] != ' ':
                font = pygame.font.Font(None, 36)
                texte = font.render(plateau[j][i], True, BLACK)
                fenetre.blit(texte, (i * une_case[0] + une_case[0] // 3, j * une_case[1] + une_case[1] // 3))

def verification_alignement_gagnant():
    # Vérification des lignes
    for ligne in plateau:
        if ligne.count('X') == 3:
            return 'X'
        elif ligne.count('O') == 3:
            return 'O'

    # Vérification des colonnes
    for i in range(3):
        if plateau[0][i] == plateau[1][i] == plateau[2][i] and plateau[0][i] != ' ':
            return plateau[0][i]

    # Vérification des diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] != ' ':
        return plateau[0][0]
    elif plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] != ' ':
        return plateau[0][2]

    return None

#///===FONCTIONS===\\\

# Crée une fonction pour initialiser le plateau de jeu
def initialiser_plateau():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

# Crée une fonction pour vérifier si le plateau est plein
def plateau_plein():
    for ligne in plateau:
        if ' ' in ligne:
            return False
    return True

#///===BOUCLE PRINCIPAL DU JEU===\\\

# Initialise le plateau de jeu
plateau = initialiser_plateau()

# Met en place la boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Affiche le plateau de jeu
    afficher_plateau()

    # Vérification de l'alignement gagnant
    gagnant = verification_alignement_gagnant()
    if gagnant:
        print(f'Le joueur {gagnant} a gagné!')
        pygame.quit()
        sys.exit()

    # Vérification si le plateau est plein
    if plateau_plein():
        print("Match nul!")
        pygame.quit()
        sys.exit()

    # Mise à jour de l'affichage
    pygame.display.flip()
