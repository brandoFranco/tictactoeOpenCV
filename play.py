def won(tabuleiro):
    if -1 not in tabuleiro:
        return 1
    else:
        if (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 0) or (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == 1):
            return 1
        elif (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 0) or (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == 1):
            return 1
        elif (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 0) or (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == 1):
            return 1
        elif (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 0) or (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == 1):
            return 1
        elif (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 0) or (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == 1):
            return 1
        elif (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 0) or (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == 1):
            return 1
        elif (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 0) or (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == 1):
            return 1
        elif (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 0) or (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == 1):
            return 1
        else:
            return 0


def move(tabuleiro, posicao, peca):
    if tabuleiro[posicao] == -1:
        tabuleiro[posicao] = peca

'''tabuleiro = [-1,-1,-1,-1,-1,-1,-1,-1,-1]

print(tabuleiro)

from random import randint

while won(tabuleiro) != 1:
    posicao = randint(0, 8)

    x = move(tabuleiro, posicao, 0)
    while x != 1:
        posicao = randint(0, 8)
        x = move(tabuleiro, posicao, 0)
    posicao = randint(0, 8)

    x = move(tabuleiro, posicao, 1)
    while x != 1:
        posicao = randint(0, 8)
        x = move(tabuleiro, posicao, 1)
    print(tabuleiro)'''
