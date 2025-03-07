# o problema nos fala que um caractere ‘.’ indica que aquele quadrado do território é ocupada por água
# da mesma forma. Além disso, espaços fora da área do mapa são ocupado por água.
def eh_agua(i,j):
    """essa função receberá os indices i e j do for e retornará
    True caso a posição i ou j estiverem fora dos limites do mapa
    ou, dentro do mapa, ela verifica se é água
    i: representa o índice i do for(que nesse caso seria a cordenada da linha)
    j: representa o índice j do for(que nesse caso seria a cordenada da coluna"""
    #condicional para ver se a posição está fora do mapa
    if i < 0 or i >= M or j < 0 or j >= N:
        return True
    #verifica se é água
    return matriz[i][j] == '.'

M,N = input().split()
M = int(M)
N = int(N)
n_costa = 0
matriz = []
for _ in range(M):
    linhas = input()
    matriz.append(linhas)
#fazer um for para verificar se a posição desejada é = # e a posição seguinte da linha ou coluna = "."
for i in range(len(matriz)):
    for j in range(len(matriz)):
#caso a posição da matriz[i][j] = '#' o programá irá verificar se as posições ao redor dela
#é água. Se apenas uma dessas posições for água somaremos um a "n_costa"
        if matriz[i][j] == '#':
            if eh_agua(i - 1, j) or eh_agua(i+1, j) or eh_agua(i, j-1) or eh_agua(i, j+1):
                n_costa += 1
print(n_costa)