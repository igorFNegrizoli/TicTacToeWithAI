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
        return "Empate"

    return "-"

def printTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(*i, sep = "|")
    print()

tabuleiro = [[" "," "," "],[" "," "," "],[" "," "," "]]
ia = "X"
jogador = "O"
vez = "ia"