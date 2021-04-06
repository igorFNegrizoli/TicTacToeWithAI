from math import inf
from ticTacToe import *

def melhorJogada(tabuleiro):
    melhorScore = -inf
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = ia
                score = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = " "
                if score > melhorScore:
                    melhorScore = score
                    coord = [i,j]
    tabuleiro[coord[0]][coord[1]] = ia
    return tabuleiro

def minimax(tabuleiro, prof, turno):
    pontos = {"X":1, "O":-1, "Empate":0}
    vencedor = winner(tabuleiro)
    if vencedor != "-":
        return pontos[vencedor]

    if turno:
        return maximiza(tabuleiro, prof)
    else:
        return minimiza(tabuleiro, prof)

def minimiza(tabuleiro, prof):
    melhorScore = inf
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = jogador
                score = minimax(tabuleiro, prof+1, True)
                tabuleiro[i][j] = " "
                melhorScore = min([score, melhorScore])
    return melhorScore

def maximiza(tabuleiro, prof):
    melhorScore = -inf
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = ia
                score = minimax(tabuleiro, prof+1, False)
                tabuleiro[i][j] = " "
                melhorScore = max([score, melhorScore])
    return melhorScore
