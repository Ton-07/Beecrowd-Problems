N = int(input())
lista_valores = [0]*N
valor = input().split()

for i in range(N):
    lista_valores[i] = int(valor[i])

menor_valor = lista_valores[0]
posicao_menor = 0

for a in range(1, N):
    if lista_valores[a] < menor_valor:
        menor_valor = lista_valores[a]
        posicao_menor = a

print('Menor valor:', menor_valor)
print('Posicao:', posicao_menor)