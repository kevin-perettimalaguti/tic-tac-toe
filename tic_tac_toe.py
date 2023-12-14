import pygame
import sys
import pygame_menu
from ia import ia

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
BLEU_CLAIR = (102, 255, 255)
VIOLET = (182, 48, 243)
GRIS = (170, 166, 184)

# Initialisation de pygame
pygame.init()
pygame.font.init()

# Police
fonte_perdu = pygame.font.SysFont('arial', 45)

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

# Fonction pour afficher le plateau de jeu
def afficher_plateau():
    fenetre.fill(BLANC)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(fenetre, NOIR, (i * une_case[0], j * une_case[1], une_case[0], une_case[1]), 2)
            if plateau[j][i] != ' ':
                font = pygame.font.Font(None, 36)
                texte = font.render(plateau[j][i], True, NOIR)
                fenetre.blit(texte, (i * une_case[0] + une_case[0] // 3, j * une_case[1] + une_case[1] // 3))

# Fonction pour vérifier un alignement gagnant
def verification_alignement_gagnant():
    for ligne in plateau:
        if ligne.count('X') == 3:
            return 'X'
        elif ligne.count('O') == 3:
            return 'O'

    for i in range(3):
        if plateau[0][i] == plateau[1][i] == plateau[2][i] and plateau[0][i] != ' ':
            return plateau[0][i]

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

# Fonction pour l'écran de fin de jeu
def fin_de_jeu(partie_gagnee=True):
    pygame.time.delay(1000)
    fenetre.fill(GRIS)

    if partie_gagnee:
        gagnant = verification_alignement_gagnant()
        if gagnant:
            label = fonte_perdu.render(f"Le joueur {gagnant} est gagnant", True, VERT)
        else:
            label = fonte_perdu.render("Match Nul !", True, ROUGE)
    else:
        label = fonte_perdu.render("Match Nul !", True, ROUGE)

    fenetre.blit(label, (fenetre_largeur // 2 - label.get_width() // 2, 65))
    pygame.display.update()

# Initialisation du menu principal
menu = pygame_menu.Menu('Jouons au Morpion', 450, 350, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button("Jouer en duel", lambda: jouer_au_morpion_sans_ia())
menu.add.button("Jouer avec l'IA", lambda: jouer_au_morpion_avec_ia())
menu.add.button('Quitter', pygame_menu.events.EXIT)

# Fonction principale du gameplay en boucle (pour jouer en duel)
def jouer_au_morpion_sans_ia():
    global plateau
    tour = ''
    en_jeu = True

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos

                for i in range(3):
                    for j in range(3):
                        case_x = i * une_case[0]
                        case_y = j * une_case[1]

                        if case_x <= mouseX < case_x + une_case[0] and case_y <= mouseY < case_y + une_case[1]:
                            plateau[j][i] = tour
                            tour = 'O' if tour == 'X' else 'X' if tour == 'O' else 'O'
                            afficher_plateau()
                            gagnant = verification_alignement_gagnant()
                            if gagnant:
                                fin_de_jeu(partie_gagnee=True)
                                pygame.display.flip()
                                pygame.time.delay(2000)
                                pygame.quit()
                                sys.exit()
                            if plateau_plein() and not gagnant:
                                fin_de_jeu(partie_gagnee=False)
                                pygame.display.flip()
                                pygame.time.delay(2000)
                                pygame.quit()
                                sys.exit()

                            pygame.display.flip()
                            
                            
                            
# Fonction principale du gameplay en boucle (pour jouer avec l'IA)
def jouer_au_morpion_avec_ia():
    global plateau
    tour = 'X'  # Initialiser le premier tour avec le joueur X
    en_jeu = True

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos

                for i in range(3):
                    for j in range(3):
                        case_x = i * une_case[0]
                        case_y = j * une_case[1]

                        if case_x <= mouseX < case_x + une_case[0] and case_y <= mouseY < case_y + une_case[1]:
                            if plateau[j][i] == ' ' and tour == 'X':
                                plateau[j][i] = tour
                                afficher_plateau()
                                gagnant = verification_alignement_gagnant()
                                if gagnant:
                                    fin_de_jeu(partie_gagnee=True)
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()
                                if plateau_plein() and not gagnant:
                                    fin_de_jeu(partie_gagnee=False)
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()

                                pygame.display.flip()

                                # Passer au tour suivant
                                tour = 'O'

                            # Vérifier si le jeu est toujours en cours avant que l'IA ne joue
                            if en_jeu:
                                # L'IA joue son coup
                                coup_ia = ia(plateau, 'O')
                                if coup_ia is not False:
                                    ligne, colonne = divmod(coup_ia, 3)
                                    if plateau[colonne][ligne] == ' ':
                                        plateau[colonne][ligne] = 'O'
                                        afficher_plateau()
                                        gagnant = verification_alignement_gagnant()
                                        if gagnant:
                                            fin_de_jeu(partie_gagnee=True)
                                            pygame.display.flip()
                                            pygame.time.delay(2000)
                                            pygame.quit()
                                            sys.exit()
                                        if plateau_plein() and not gagnant:
                                            fin_de_jeu(partie_gagnee=False)
                                            pygame.display.flip()
                                            pygame.time.delay(2000)
                                            pygame.quit()
                                            sys.exit()

                                pygame.display.flip()

                                # Passer au tour suivant
                                tour = 'X'

    pygame.quit()





# Initialiser le plateau avant le lancement du jeu
initialiser_plateau()

# Lancement du menu
menu.mainloop(fenetre)





