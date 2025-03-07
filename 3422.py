"""Esse programa foi feito para ajudar José a registrar as ocorrências em tempo corrido de 90 minutos. Para isso o programa
inicia recebendo um valor de entrada, além disso riamos dois contadores: um para o número de registros e outro para os 
minutos respectivamente. Com isso feito, usamos o while para criarmos um laço de repetição para que, dentro dele, o programa
receba duas entradas na mesma linha sendo uma delas o minuto da ocorrência e a outra o tempo que ela ocorreu onde,a variável
o será convertida para inteiro. Após isso, escrevemos a condicional para o <= 45 e t = 1T, o > 45 e t = 1T e realizamos dentro
deles os calculos para que o programa mostre o resultado desejado na tela. As condicionais para o segundo tempo seguem a mesma
lógica das condicionais do primeiro tempo. Por fim, a cada repetição do while o programa soma +1 a variável n_registros
de modo que quando n_registros == n o while será interrompído"""
#o programa recebe um valor de entrada para os números de registro
n = int(input())
#criamos dois contadores: um para o número de registros e outro para os minutos respectivamente
n_registros = 0
minuto = 0
#usamos o while para criarmos um laço de repetição
while True:
#o programa irá receber duas entradas na mesma linha sendo uma delas o minuto da ocorrência e a outra o tempo que ela ocorreu
    o,t = input().split()
#transformamos os minutos da ocorrência para inteiro
    o = int(o)
#escrevemos a condicional para o menor ou igual a 45 e t como primeiro tempo e mostramos o valor na tela
    if o <= 45 and t == '1T':
        minuto += o
        print(minuto)
        minuto = 0
#condicional para o maior que 45 e t como primeiro tempo. Esaa condicional calcula a prorrogração do primeiro tempo e mostra
#o resultado na tela
    elif o > 45 and t == '1T':
        diferença = o - 45
        print('45+{}'.format(diferença))
#as duas condicionais a seguir seguem a mesma lógica das duas anteriores, com a diferença que essa faz os calculos para
#o segundo
    elif o <= 45 and t == '2T':
        minuto = 45 + o
        print(minuto)
        minuto = 0
    elif o > 45 and t == '2T':
        diferença2 = o - 45
        print('90+{}'.format(diferença2))
#a cada repetição do while o programa soma +1 a variável n_registros
    n_registros += 1
#condicional que para o while quando n_registros == n
    if n_registros == n:
        break