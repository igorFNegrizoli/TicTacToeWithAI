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

def depthSearch(tabuleiro, vez):
    pontos = {"X":7, "O":-2, "Empate":2}
    #vez == True -> IA
    #vez == False -> jogador
    
    vencedor = winner(tabuleiro)
    if vencedor != "-":
        return pontos[vencedor]

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