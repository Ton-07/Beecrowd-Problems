"""A questão pede que mostremos na tela o resultado de s com dois dígitos após o ponto decimal. Para iss,
definimos s como zero(ele será responsável por receber a soma de 1 dividido pelo denominador a cada repetição 
do While) e definimos o denominador que deve começar em um. Após isso, criamos um laço de repetição que parará 
o While quando o denominador dor menor ou igual a 100 e escrevemos dentro dele que s recebe a soma de 1 dividido 
pelo denominador. A cada repetição o valor de s e do denominador irá crescer até que a condição estabelecida pare 
o While. Por fim, mosramos o valor de s na tela"""
#primeiro termo da sequência deve começar em zero para que seja somado 1 a ele dentro do While
s = 0
#valor do denominador
denominador = 1
#criamos um laço de repetição que parará o While quando o denominador dor menor ou igual a 100
while denominador <= 100:
#s recebe a soma de 1 dividido pelo denominador
    s += 1 / denominador
#soma-se um ao denominador 
    denominador +=1
#mostramos na tela o resultado com dois dígitos após o ponto decimal.
print('{:.2f}'.format(s))