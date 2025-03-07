while True:
    try:
        N = int(input())
    except EOFError:
        break

    polinomio = input().split(' + ')
    pd = ""
    for i in range(N - 1):
        p = polinomio[i].split('x')
        derivado = int(p[0]) * int(p[1])
        expoente = int(p[1]) - 1
        pd += str(derivado) + 'x' + str(expoente)
        pd += ' + '
    p = polinomio[N - 1].split('x')
    derivado = int(p[0]) * int(p[1])
    pd += str(derivado) + 'x'
    print(pd)