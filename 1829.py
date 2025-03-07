import math

def fatmaior(n, exp):
    if n >= 6:
        if n >= math.log(exp)/math.log(n/3):
            return True
        if n <= math.log(exp)/math.log(n/2):
            return False
    total = 1
    for i in range(n, 1, -1):
        total *= i
    if total > exp:
        return True
    return False


rodadas = int(input())
vitorias_lucas = 0
vitorias_pedro = 0
lista_vencedores = ['0'] * rodadas

for i in range(rodadas):
    lucas = input().split('^')
    pedro = input().split('!')
    fat = int(pedro[0])

    expo = int(lucas[0]) ** int(lucas[1])

    if fatmaior(fat, expo):
        vitorias_pedro += 1
        lista_vencedores[i] = 'Rodada #{}: Pedro foi o vencedor'.format(i + 1)
    else:
        vitorias_lucas += 1
        lista_vencedores[i] = 'Rodada #{}: Lucas foi o vencedor'.format(i + 1)

if vitorias_lucas == vitorias_pedro:
    print('A competicao terminou empatada!')
else:
    if vitorias_lucas > vitorias_pedro:
        print('Campeao: Lucas!')
    else:
        print('Campeao: Pedro!')

for j in range(rodadas):
    print(lista_vencedores[j])