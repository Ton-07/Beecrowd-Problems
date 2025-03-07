#definimos um valor float "x" de entrada
x = float(input())
#escrevemos a condicional para cada intervalo
if 0 <= x <= 25:
    print('Intervalo [0,25]')
elif 25 < x <= 50:
    print('Intervalo (25,50]')
elif 50 < x <= 75:
    print('Intervalo (50,75]')
elif 75 < x <= 100:
    print('Intervalo (75,100]')
#se a condicional não se cumprir mostramos na tela "Fora de intervalo"
else:
    print('Fora de intervalo')