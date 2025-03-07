def transforma(lista):
    return [int(num) for num in lista]

n = int(input())
contagem = 0
padrao = [1, 2, 3, 4, 5, 6, 7, 8, 9]
instancia = 1

for _ in range(n):
    matriz = []
    for _ in range(9):
        linha = input().split()
        transformada = transforma(linha)
        matriz.append(transformada)
    
    for j in range(9):
        coluna = []
        for h in range(9):
            coluna.append(matriz[j][h])
        coluna.sort()
        if coluna == padrao:
            contagem += 1
    
    for j in range(9):
        linha = []
        for h in range(9):
            linha.append(matriz[h][j])
        linha.sort()
        if linha == padrao:
            contagem += 1
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrade = []
            for k in range(3):
                for m in range(3):
                    subgrade.append(matriz[i+k][j+m])
            subgrade.sort()
            if subgrade == padrao:
                contagem += 1
    
    print('Instancia {}'.format(instancia))
    if contagem == 27:
        print('SIM')
    else:
        print('NAO')
    print()
    instancia += 1
    contagem = 0
