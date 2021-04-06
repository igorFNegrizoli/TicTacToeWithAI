from ticTacToe import *

escolha = ""
while(escolha not in ["1","2"]):
    print("Contra qual I.A. deseja jogar?")
    print("1 - Minimax")
    print("2 - Busca em profundidade")
    escolha = input()
    if escolha == "1":
        from minimax import *
    elif escolha == "2":
        from depthSearch import *
    else:
        print("Entrada invalida")
        print()


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