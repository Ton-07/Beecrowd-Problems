def pao_de_queijo(matriz):
    """Essa função receberá uma matriz e retornará
    outra matriz contendo as respostas para o problema"""
    matriz_resultados = []
    for i in range(len(matriz)):
        lista_resultados = [0] * len(matriz[i])
        for j in range(len(matriz[i])):
            pos_analisada = int(matriz[i][j])
            if pos_analisada == 1:
                lista_resultados[j] = 9
            elif pos_analisada >= 0 and pos_analisada <= 4:
                contador_adjacentes = 0
                # Condicional linha a direita
                if j + 1 < len(matriz[i]) and int(matriz[i][j + 1]) == 1:
                    contador_adjacentes += 1
                # Condicional linha a esquerda
                if j - 1 >= 0 and int(matriz[i][j - 1]) == 1:
                    contador_adjacentes += 1
                # Condicional coluna abaixo
                if i + 1 < len(matriz) and int(matriz[i + 1][j]) == 1:
                    contador_adjacentes += 1
                # Condicional coluna acima
                if i - 1 >= 0 and int(matriz[i - 1][j]) == 1:
                    contador_adjacentes += 1
                lista_resultados[j] = contador_adjacentes
        matriz_resultados.append(lista_resultados)
    return matriz_resultados

# Exemplo de uso:
while True:
    try:
        N, M = input().split()
    except EOFError:
        break

    N = int(N)
    M = int(M)
    mat = []
    # Vamos criar a matriz NxM
    for _ in range(N):
        linha = input().split()
        mat.append(linha)

    # Com a matriz criada, vamos criar uma função que faz a contagem da quantidade de pães de queijo
    # adjacentes a ela. Essa função vai receber uma matriz e retornar outra matriz com os resultados
    resultado = pao_de_queijo(mat)
    # Por fim, vamos fazer um for para mostrar os resultados da matriz
    for i in range(len(resultado)):
        for j in range(len(resultado[i])):
            print(resultado[i][j], end='')
        print()