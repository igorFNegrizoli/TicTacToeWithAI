from ticTacToe import *
from math import inf

def melhorJogada(tabuleiro):
    melhorScore = -inf
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = "X"
                score = depthSearch(tabuleiro, True)
                tabuleiro[i][j] = " "
                if score > melhorScore:
                    melhorScore = score
                    coord = [i,j]
    tabuleiro[coord[0]][coord[1]] = "X"
    return tabuleiro

def calculaScore(tabuleiro, vencedor):
    #score = R * 2^(5-i) * 3^(5-d)
    pontos = {"X":7, "O":-2, "Empate":0}
    i2 = d = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                i2 += 1
            if tabuleiro[i][j] == vencedor:
                d += 1
    return (pontos[vencedor] * pow(2,5-i2) * pow(3,5-d))
            

def depthSearch(tabuleiro, vez):
    #vez == True -> IA
    #vez == False -> jogador
    
    vencedor = winner(tabuleiro)
    if vencedor != "-":
        return calculaScore(tabuleiro, vencedor)

    tempResultado = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] != " ":
                continue

            if vez:
                quemJoga = "X"
            else:
                quemJoga = "O"

            tabuleiro[i][j] = quemJoga
            tempResultado += depthSearch(tabuleiro, not vez)
            tabuleiro[i][j] = " "

    return tempResultado
