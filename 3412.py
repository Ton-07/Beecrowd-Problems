na = int(input())
contador_na = 0
nt = 0
while contador_na != na:
    nome = input()
    notas = input().split()
    t = len(notas)
    if t < 2:
        notas += '0'
        t = len(notas)
        for i in range(t):
            notas[i] = float(notas[i])

        for v in range(t):
            nt += notas[v]

        media = nt / t
    elif t == 2:
        for i in range(t):
            notas[i] = float(notas[i])

        for v in range(t):
            nt += notas[v]

        media = nt / t
    elif t == 3:
        for i in range(t):
            notas[i] = float(notas[i])

        for v in range(t):
            nt += notas[v]

        media = nt / t
    elif t == 4:
        for i in range(t):
            notas[i] = float(notas[i])

        menor_valor = notas[0]
        for a in range(1, t):
            if notas[a] < menor_valor:
                menor_valor = notas[a]

        notas.remove(menor_valor)
        for v in range(t - 1):
            nt += notas[v]
        media = nt / 3

    print('{}: {:.1f}'.format(nome, media))

    contador_na += 1
    nt = 0