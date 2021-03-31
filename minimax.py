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

def minimax(tabuleiro, prof, maximizacao):
    pontos = {"X":10, "O":-10, "Empate":0}
    vencedor = winner(tabuleiro)
    if vencedor != "-":
        return pontos[vencedor]

    if maximizacao:
        melhorScore = -inf
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = ia
                    score = minimax(tabuleiro, prof+1, False)
                    tabuleiro[i][j] = " "
                    melhorScore = max([score, melhorScore])
        return melhorScore
    else:
        melhorScore = inf
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro[i])):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = jogador
                    score = minimax(tabuleiro, prof+1, True)
                    tabuleiro[i][j] = " "
                    melhorScore = min([score, melhorScore])
        return melhorScore

##
#Main
##

while winner(tabuleiro) == "-":
    printTabuleiro(tabuleiro)
    if vez == "ia":
        print("Pensando...")
        print()
        tabuleiro = melhorJogada(tabuleiro)
        vez = "jogador"
    else:
        coord = [-1, -1]
        while True:
            coord[0] = int(input("jogada (linha): "))
            coord[1] = int(input("jogada (coluna): "))
            print()
            if ((coord[0] < 3) and (coord[1] < 3) and (coord[0] >= 0) and (coord[1] >= 0)) and (tabuleiro[coord[0]][coord[1]] == " "):
                break
            print("A posição desejada é inválida!!!")
            print("Escolha uma posição não preenchida e entre 0 e 2")
            printTabuleiro(tabuleiro)
        tabuleiro[coord[0]][coord[1]] = jogador
        vez = "ia"
        

printTabuleiro(tabuleiro)
print(winner(tabuleiro))
