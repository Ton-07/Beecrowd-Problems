def ler_parede():
    parede = []
    parede.append([int(input())])
    for i in range(2, 9, 2):
        parede.append([0] * i)
        parede.append([0] * (i + 1))
        valores_linha = input().split()
        k = 0
        for j in range(0, i + 1, 2):
            parede[i][j] = int(valores_linha[k])
            k += 1
    return parede

def preencher_parede(parede):
    for j in range(1, 8, 2):
        parede[8][j] = (parede[6][j-1] - parede[8][j-1] - parede[8][j+1]) // 2
    
    for linha in range(7, 0, -2):
        for coluna in range(0, linha + 1):
            parede[linha][coluna] = parede[linha + 1][coluna] + parede[linha + 1][coluna + 1]
        for coluna in range(1, linha, 2):
            parede[linha - 1][coluna] = parede[linha][coluna] + parede[linha][coluna + 1]

def mostrar_parede(parede):
    for linha in range(9):
        for coluna in range(0, linha):
            print(parede[linha][coluna], "", end="")
        print(parede[linha][linha])

num_casos = int(input())

for _ in range(num_casos):
    parede = ler_parede()
    preencher_parede(parede)
    mostrar_parede(parede)
