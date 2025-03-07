def MDC (x,y):
    """
        O MDC(x,y) recebe dois valores de entrada que representam
        o comprimento e a largura do terreno e calcula o MDC entre
        eles(tudo isso dentro do while que só se encerrará quando
        y = 0. Quando y finalmente se torna zero, retorna-se o valor
        de x, que será o MDC entre os dois números.
        """
    while y != 0:
        resto = x % y
        x = y
        y = resto
    return x

while True:
    try:
        x,y = input().split()
    except EOFError:
        break
    x = int(x)
    y = int(y)
    comprimento_cerca = MDC(x,y)
    perimetro = (x + y) * 2
    estacas = perimetro // comprimento_cerca
    print(estacas)
