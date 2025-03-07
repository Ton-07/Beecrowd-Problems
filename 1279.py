"""A questão pede que imprimamos as diferentes propriedades dos anos em diferentes linhas de acordo
com a descrição anterior. Para isso, criamos a variável pula linha como falsa e iniciamos um laço de repetição
usando o While. Dentro do while escrevemos o bloco Try no qual escreveremos a variável ano que receberá um valor 
de entrada, a condicional para pula uma linha caso o pula linha seja verdadeiro e caso seja falso ele deve ser 
convetido para verdadeiro, escrevemos também a variável bissexto com as características do ano bissexto especificadas
na questão e, por fim, escrevemos as condicionais para as diferentes propriedades dos anos em diferentes linhas
e mostramos o tipo do ano na tela"""
#criamos a variável pula linha como falsa
pula_linha = False
#Cria-se um laço de repetição com o While
while True:
#no bloco Try escrevemos o valor de entrada e as condicionais
    try:
#ano recebe uma entrada que será convertida para inteiro
        ano = int(input())
#se pula_linha for verdadeiro o programa pulará uma linha, se não ele converte pula linha para verdade
        if pula_linha:
            print()
        else:
            pula_linha = True
#dentro da variável bissexto escrevemos as condições para o ano bissexto
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
#escrevemos as condicionais para as diferentes propriedades dos anos em diferentes linhas
        if bissexto:
            print('This is leap year.')
        if ano % 15 == 0:
            print('This is huluculu festival year.')
        if bissexto and ano % 55 == 0:
            print('This is bulukulu festival year.')

        if not (bissexto or ano % 15 == 0 or (bissexto and ano % 55 == 0)):
            print('This is an ordinary year.')
#bloco except contendo o EOFError e o comando de parar o While
    except EOFError:
        break
