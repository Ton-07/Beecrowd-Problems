#estipulamos uma entrada 0<=entrada<=9
entrada = input()
#definimos que a condicional foi um número do tipo str ela deve ser convertida para interio, caso contrario ela deve
#permanecer como str
if entrada == '0' or entrada=='1' or entrada=='2' or entrada=='3' or entrada=='4' or entrada=='5' or entrada=='6' or entrada=='7' or entrada== '8' or entrada=='9':
 entrada = int(entrada)
else:
    entrada = str(entrada)
#escrevemos as condicionais para cada caso e determinamos a mensagem que deve ser mostrada na tela
if entrada == 0:
    print('zero')
elif entrada == 1:
    print('um')
elif entrada == 2:
    print('dois')
elif entrada == 3:
    print('tres')
elif entrada == 4:
    print('quatro')
elif entrada == 5:
    print('cinco')
elif entrada == 6:
    print('seis')
elif entrada == 7:
    print('sete')
elif entrada == 8:
    print('oito')
elif entrada == 9:
    print('nove')

if entrada == 'zero':
    print(0)
elif entrada == 'um':
    print(1)
elif entrada == 'dois':
    print(2)
elif entrada == 'tres':
    print(3)
elif entrada == 'quatro':
    print(4)
elif entrada == 'cinco':
    print(5)
elif entrada == 'seis':
    print(6)
elif entrada == 'sete':
    print(7)
elif entrada == 'oito':
    print(8)
elif entrada == 'nove':
    print(9)