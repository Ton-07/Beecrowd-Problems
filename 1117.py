"""esse código foi feito para ler valores entrada positivos, negativos ou reais de modo que, caso o valor lido
não esteja entre o intervalo[0,10] o programa deve mostrar a mensagem: nota invalida e pedir novamente o valor de
entra nota1 até que a condição ja mencionada seja cumprida.Para fazer esse looping criamos um laço de repetição
dentro da condicional. Caso a nota pertença ao intervalo [0,10] o programa vai abrir uma entrada nota2 que seguirá a mesma
lógica explicada anteriomente para a nota1. Para criarmos a repetição que continuará a repetir as etapas até todas
as etapas se cumprirem usaremos o while que criará um laço de repetição. Assim, se a nota1 e nota2 cumprirem a
condição de estarem localizadas no intervalo [0,10] o programa irá calcular a média entre as notas e finalizar o laço
formado pelo while de modo que mostraremos na tela com a função print a média das notas"""
#usamos o while para criarmos o laço de repetição
while True:
#criamos o primeiro valor de entrada para receber a primeira nota
    nota1 = float(input())
#passamos o valor por uma condicional que so aceitará ele quando a nota for válida
    if nota1<0 or nota1 > 10:
        while nota1<0 or nota1 > 10:
            print('nota invalida')
            nota1 = float(input())
#se o valor da nota1 cumprir a condição de estar entre [0,10] o programa deve pular a a condicional anterior
    else:
        pass
#a mesma lógica usada para a nota1 também é usada aqui
    nota2 = float(input())
    if nota2<0 or nota2>10:
        while nota2<0 or nota2>10:
            print('nota invalida')
            nota2 = float(input())
    else:
        pass
#escrevemos a condicional que irá calcular a média entre nota1 e nota2 e encerrar o looping
    if 0<=nota1<=10 and 0<=nota2<=10:
        media = (nota1 + nota2)/2
        break
#mostramos o valor da media na tela
print('media = {}'.format(media))