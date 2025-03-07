N = int(input())
dias = 0
contador_N = 0
while contador_N != N:
    estoque = float(input())
    dias = 0
    while estoque > 1:
        estoque = estoque / 2
        dias += 1
    print('{} dias'.format(dias))
    contador_N += 1