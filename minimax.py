from math import inf
def winner(tabuleiro):
    winner = " "

    for i in tabuleiro:
        if i.count(i[0]) == len(i) and i[0] != " ":
            return i[0]
            
    transposta = [list(i) for i in zip(*tabuleiro)]
    for i in transposta:
        if i.count(i[0]) == len(i) and i[0] != " ":
            return i[0]

    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]) and tabuleiro[1][1] != " ":
        return tabuleiro[1][1]
    
    if (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]) and tabuleiro[1][1] != " ":
        return tabuleiro[1][1]

    espacosOcupados = 0
    for i in tabuleiro:
        for j in i:
            if j != " ":
                espacosOcupados += 1
    
    if espacosOcupados == 9:
        return " "

    return "-"

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
    pontos = {"X":10, "O":-10, " ":0}
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

def printTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)
    print()

tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
ia = "X"
jogador = "O"
vez = "ia"

while winner(tabuleiro) == "-":
    printTabuleiro(tabuleiro)
    if vez == "ia":
        tabuleiro = melhorJogada(tabuleiro)
        vez = "jogador"
    else:
        coord = [-1, -1]
        coord[0] = int(input("jogada (linha): "))
        coord[1] = int(input("jogada (coluna): "))
        tabuleiro[coord[0]][coord[1]] = jogador
        vez = "ia"

printTabuleiro(tabuleiro)
print(winner(tabuleiro))