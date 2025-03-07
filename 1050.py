#atribuímos uma valor de entrada aleatório através da função "input" e transformamos ele em inteiro
#através da função "int"
ddd = int(input())
#escrevemos a condicional para que,de acordo com o número de entrada, seja mostrada alguam dessas 
#mensagens na tela. Caso o número de entrada não cumpra as condições será mostrado "DDD nao cadastrado"
#na tela
if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')