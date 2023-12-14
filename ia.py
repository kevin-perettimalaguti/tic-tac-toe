import random

def ia(board, signe):
    # Vérifier si l'IA peut gagner
    for i in range(3):
        if board[i][0] == board[i][1] == signe and board[i][2] == ' ':
            return i * 3 + 2  # Gagner en remplissant la troisième colonne

        if board[i][1] == board[i][2] == signe and board[i][0] == ' ':
            return i * 3  # Gagner en remplissant la première colonne

        if board[i][0] == board[i][2] == signe and board[i][1] == ' ':
            return i * 3 + 1  # Gagner en remplissant la deuxième colonne

        if board[0][i] == board[1][i] == signe and board[2][i] == ' ':
            return 6 + i  # Gagner en remplissant la troisième ligne

        if board[1][i] == board[2][i] == signe and board[0][i] == ' ':
            return i  # Gagner en remplissant la première ligne

        if board[0][i] == board[2][i] == signe and board[1][i] == ' ':
            return 3 + i  # Gagner en remplissant la deuxième ligne

    # Vérifier si l'adversaire peut gagner et bloquer
    adversaire_signe = "O" if signe == "X" else "X"

    for i in range(3):
        if board[i][0] == board[i][1] == adversaire_signe and board[i][2] == ' ':
            return i * 3 + 2  # Bloquer en remplissant la troisième colonne

        if board[i][1] == board[i][2] == adversaire_signe and board[i][0] == ' ':
            return i * 3  # Bloquer en remplissant la première colonne

        if board[i][0] == board[i][2] == adversaire_signe and board[i][1] == ' ':
            return i * 3 + 1  # Bloquer en remplissant la deuxième colonne

        if board[0][i] == board[1][i] == adversaire_signe and board[2][i] == ' ':
            return 6 + i  # Bloquer en remplissant la troisième ligne

        if board[1][i] == board[2][i] == adversaire_signe and board[0][i] == ' ':
            return i  # Bloquer en remplissant la première ligne

        if board[0][i] == board[2][i] == adversaire_signe and board[1][i] == ' ':
            return 3 + i  # Bloquer en remplissant la deuxième ligne

    # Si aucune opportunité de gagner ou de bloquer, jouer au hasard
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if available_moves:
        move = random.choice(available_moves)
        return move[0] * 3 + move[1]
    else:
        return False
