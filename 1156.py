"""Esse código foi feito para calcular e mostrar o valor de s. Para isso, devemos criar um contador s
que irá somar os termos de s, outro para sercir como o primeiro termo e outro para servir de denominador.
Com isso feito, criamos um laço de repetição usando o while que realizará o looping ate que o valor do
contador termo1 seja menor ou igual a 39. Por fim, pegamos o valor de s que foi armazenado na variável s
e mostramos na tela aproximando duas casas decimais após a vírgula. """
#contador s que acumulará a soma dos termos de s
s = 0
#contador que recebe o primeiro número da soma e receberá os demais valores do numerador 
termo1 = 1
#contador que irá acumular os valores do denominador
denominador = 1
#estrutura de repetição para calculamos a soma de s
while termo1 <= 39:
#realizamos os calculos para descobrir o valor de s
    s += termo1 / denominador
#numeros que devem ser somados a cada repetição do while
    termo1 += 2
    denominador *=2
#com o fim do while mostramos na tela o valor de s com duas  casas decimais após a vírgula
print('{:.2f}'.format(s))