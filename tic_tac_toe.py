# Importation des modules pygame
import pygame
import sys
import pygame_menu

#///================ESTHETIQUE DU JEU======================\\\
    
    # Définition de couleurs utilisées dans le jeu
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
BLEU_CLAIR = (102, 255, 255)
VIOLET = (182, 48, 243)
GRIS = (170, 166, 184)

pygame.init()

    # Dimensions de la fenêtre
fenetre_largeur = 450
fenetre_hauteur = 350
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
pygame.display.set_caption("Tic-Tac-Toe")

    # Initialisation du plateau du jeu
largeur_plateau = 450
hauteur_plateau = 350
une_case = (largeur_plateau // 3, hauteur_plateau // 3)

    # Déclaration globale du plateau
plateau = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

#///================FONCTIONS NECESSAIRE POUR LE JEU======================\\\
    
    # Fonction pour afficher le plateau de jeu
def afficher_plateau():
    fenetre.fill(BLANC)  # Le fond de l'écran de jeu en blanc

    # Ma Grille en 3x3
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(fenetre, NOIR, (i * une_case[0], j * une_case[1], une_case[0], une_case[1]), 2)
            if plateau[j][i] != ' ':
                font = pygame.font.Font(None, 36)
                texte = font.render(plateau[j][i], True, NOIR)
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

    # Fonction pour initialiser le plateau de jeu
def initialiser_plateau():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    
    # Fonction pour vérifier si le plateau est plein
def plateau_plein():
    for ligne in plateau:
        if ' ' in ligne:
            return False
    return True

#///================MENU======================\\\
    
    # Initialisation du menu principal
menu = pygame_menu.Menu('Welcome', 450, 350, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Jouer', lambda: jouer_au_morpion())
menu.add.button('Quitter', pygame_menu.events.EXIT)

#///================FONCTION DU GAMEPLAY EN BOUCLE======================\\\
    
def jouer_au_morpion():
    global plateau  # Utilise la variable globale au lieu de la déclarer localement
    tour = 'X'  # Initialise le premier tour avec le joueur 'X'
    en_jeu = True   

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_jeu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtient les coordonnées de la case cliquée
                mouseX, mouseY = event.pos
                colonne = mouseX // une_case[0]
                ligne = mouseY // une_case[1]

                # Vérifie si la case est vide avant de placer le symbole
                if plateau[ligne][colonne] == ' ':
                    plateau[ligne][colonne] = tour

                    # Change le joueur à chaque tour
                    tour = 'O' if tour == 'X' else 'X'

                    afficher_plateau()

                    # Vérifie l'alignement gagnant
                    gagnant = verification_alignement_gagnant()
                    if gagnant:
                        print(f'Le joueur {gagnant} a gagné!')
                        pygame.quit()
                        sys.exit()

                    # Vérifie si le plateau est plein
                    if plateau_plein():
                        print("Match nul!")
                        pygame.quit()
                        sys.exit()

                    # Mise à jour de l'affichage
                    pygame.display.flip()

    # Fermeture de pygame
    pygame.quit()

# Lancement du menu
menu.mainloop(fenetre)
