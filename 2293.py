def max_function(vet):
    """
    Descobre o máximo de n números, inteiros ou reais,
    ou de uma string de n caracteres, e o retorna.
    vet: qualquer sequência (lista, tupla ou string)
    Retorna o valor máximo do vetor
    """
    n = len(vet)
    maximo = vet[0] # Inicializa o máximo com o
                    # valor da primeira posição do vetor.
    for i in range(1, n): # Compara o segundo valor em diante
        if (vet[i] > maximo): # Se for maior que o máximo
            maximo = vet[i]   # passa a ser o novo máximo
    return maximo
l, c = input().split()
l = int(l)
c = int(c)
soma = 0
matriz = []
# criamos a matriz
for i in range(l):
    linha = input().split()
    matriz.append(linha)
# precisamos fazer a soma de cada coluna e de cada linha e ver qual possui o maior valor
maior_valor = []
#for para somar as linhas
for j in range(len(matriz)):
    linha_vez = matriz[j]

    for a in range(len(linha_vez)):
        soma += int(linha_vez[a])
    maior_valor.append(soma)
    soma = 0
# for para fazer a soma das colunas
for q in range(c):
    for p in range(l):
        soma += int(matriz[p][q])
    maior_valor.append(soma)
    soma = 0
# encontramos o maior valor e mostramos na tela
maior_soma = max_function(maior_valor)
print(maior_soma)