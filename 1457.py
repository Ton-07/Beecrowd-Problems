instancias = int(input())

for i in range(instancias):
    entrada = input().split('!')
    N = int(entrada[0])
    K = len(entrada) - 1

    resultado = 1
    fatorial = N
    while fatorial > 0:
        resultado *= fatorial
        fatorial -= K

    print(resultado)