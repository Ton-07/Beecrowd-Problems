N = int(input())
linhas = N
colunas = N
matriz = []
soma_linhas = 0
soma_colunas = 0
soma_diagonalp = 0
soma_diagonals = 0
eh_magico = True
valores_diferente = True
valores_cubo = []
#fazemos um for para criar a matriz
for _ in range(N):
    linha = input().split()
    matriz.append(linha)
#um quadrado mágico não pode ter todos os seus valores iguais. Por conta disso, precisamos
#fazer um for para verificar se todos os números da matriz são iguais
for d in range(len(matriz) - 1):
    if matriz[d] == matriz[d + 1]:
        valores_diferente = False
    else:
        valores_diferente = True

#com a matriz criada devemos fazer um for para obtermos a soma das diagonais, colunas e linhas
for i in range(len(matriz)):
    for j in range(len(matriz)):
        soma_linhas += int(matriz[i][j])
        soma_colunas += int(matriz[j][i])
    soma_diagonalp += int(matriz[i][i])
    soma_diagonals += int(matriz[i][len(matriz) - 1 - i])
    valores_cubo.append(soma_linhas)
    valores_cubo.append(soma_colunas)
    soma_linhas = 0
    soma_colunas = 0
valores_cubo.append(soma_diagonalp)
valores_cubo.append((soma_diagonals))

#vamos fazer um último for para verificar se todos os valores dentro de "valores_cubo" são
#iguais
for f in range(len(valores_cubo) - 1):
    if valores_cubo[f] != valores_cubo[f + 1]:
        eh_magico = False
        break
if eh_magico and valores_diferente:
    print(valores_cubo[0])
else:
    print('0')