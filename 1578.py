def max_larg_col(m, mat):
    """
    Recebe a dimensão e a matriz de strings,
    e retorna uma lista com a largura máxima
    de strings em cada coluna.
    m: int;
    mat: matriz de strings.
    Retorna uma lista de int.
    """
    larg = [0] * m

    for j in range(m):
        for i in range(m):
            len_numero = len(mat[i][j])
            if len_numero > larg[j]:
                larg[j] = len_numero
    return larg

# n_calculados = Ler número de matrizes
n_calculados = int(input())
x = 4
# Laço for para cada uma das n matrizes
contador_n = 0
while contador_n != n_calculados:
    matriz = []

    # l_c = Dimensão da matriz quadrada
    l_c = int(input())

    # Laços para leitura da matriz e conversão para valores inteiros
    for i in range(l_c):
        linhas = input().split()
        for j in range(len(linhas)):
            linhas[j] = int(linhas[j])
        matriz.append(linhas)

    # Trecho para calcular a matriz ao quadrado segundo Atrapalhilton
    matriz_ao_quadrado = []
    for i in range(l_c):
        linha_ao_quadrado = [''] * l_c
        for j in range(l_c):
            linha_ao_quadrado[j] = str(matriz[i][j] ** 2)
        matriz_ao_quadrado.append(linha_ao_quadrado)

    # Calcula a largura máxima de cada coluna na matriz de strings
    larguras_colunas = max_larg_col(l_c, matriz_ao_quadrado)

    # Ajusta as strings na matriz para que estejam alinhadas à direita
    for j in range(l_c):
        for i in range(l_c):
            qtd_espacos = larguras_colunas[j] - len(matriz_ao_quadrado[i][j])
            matriz_ao_quadrado[i][j] = ' ' * qtd_espacos + matriz_ao_quadrado[i][j]

    # Imprime o cabeçalho da matriz conforme especificado
    valor = x + contador_n
    contador_n += 1
    print('Quadrado da matriz #{}:'.format(valor))

    # Imprime a matriz formatada
    for i in range(l_c):
        print(' '.join(matriz_ao_quadrado[i]))

    # Imprime uma linha em branco entre as saídas das matrizes
    if contador_n != n_calculados:
        print()
