caso_testes = int(input())
soma_colunas = 0
soma_linhas = 0
soma_diagonalp = 0
soma_diagonals = 0
eh_magico = True
valores_somas = []
matriz = []
for _ in range(caso_testes):
    linhas = input().split()
    matriz.append(linhas)
# com a matriz criada fazemos um for para somar as colunas, outro para as linhas e um último para as diagonais

# for para as colunas
for a in range(len(matriz)):
    for b in range(len(matriz)):
        soma_colunas += int(matriz[b][a])
    valores_somas.append(soma_colunas)
    soma_colunas = 0

# for para fazer a soma das linhas
for c in range(len(matriz)):
    for d in range(len(matriz)):
        soma_linhas += int(matriz[c][d])
    valores_somas.append(soma_linhas)
    soma_linhas = 0

# for para somar as diagonais principais
for e in range(len(matriz)):
    soma_diagonalp += int(matriz[e][e])
    soma_diagonals += int(matriz[e][len(matriz) - 1 - e])

valores_somas.append(soma_diagonalp)
valores_somas.append(soma_diagonals)

for f in range(len(valores_somas) - 1):
    if valores_somas[f] != valores_somas[f + 1]:
        eh_magico = False
        break
if eh_magico:
    print('{:.0f}'.format(valores_somas[0]))
else:
    print('-1')