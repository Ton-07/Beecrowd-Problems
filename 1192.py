N = int(input())
cotador_N = 0
resultado = 0
while cotador_N != N:
    x, l, y = input()
    x = int(x)
    y = int(y)
    if x == y:
        resultado = y * x
    elif 97 <= ord(l) <= 122:
        resultado = y + x
    elif 65<= ord(l) <= 90:
        resultado = y - x
    cotador_N += 1
    print(resultado)