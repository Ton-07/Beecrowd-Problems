N = int(input())
lista = [0]*N
pontos = 0
vn = 1

valores = input().split()

for i in range(N):
    lista[i] = int(valores[i])

for j in range(N - 1):
    if lista[j] == lista[j + 1]:
        vn += 1
    else:
        if vn > pontos:
            pontos = vn
        vn = 1

if vn > pontos:
    pontos = vn

print(pontos)