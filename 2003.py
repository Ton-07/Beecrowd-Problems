"""esse código foi feito para calcular o atraso máximo de Bino. Para isso escrevemos o código dentro do
While True. Começamos Criando um bloco try que conterá o as entradas paras as horas e os minutos que são
conertidos para inteiros e depois calcularemos os minutos totais e atribuiremos esse valor a variável
atrasomaxmin. Criaremos duas condicionais: uma para mostrar o tempo que ele atrasou e outra para mostrar
que ele chegou exatamente no horário,respectivamente. Por fim, criamos o bloco except contendo o EOFError"""
#laço de repetição que so será parado com o EOFError
while True:
#escrevemos o try dentro do While
    try:
#o progrma vai receber dois valores de entrada: um para as horas e outro para os minutos
        H,M = input().split(':')
#transformamos as varíaveis H e M em inteiros
        H = int(H)
        M = int(M)
#transformamos as horas em minutos
        hm = H * 60
#somamos as horas em minutos e os minutos para descobrirmos o tempo total em minutos
        tempmin = hm + M
#atribuímos a variável tempmin na variável atrasomaxmin
        atrasomaxmin = tempmin
#se o atrasomaxmin for maior que 420 o programa mostrará na tela quanto tempo Bino atrasará
        if atrasomaxmin > 7*60:
            atraso = atrasomaxmin - 420
            print('Atraso maximo: {}'.format(atraso))
#se o atrasomaxmin for menor ou igual que 420 o programa mostrará que Bino chegou na hora
        elif atrasomaxmin <= 7*60:
            print('Atraso maximo: 0')
#bloco except contendo o EOFError
    except EOFError:
        break