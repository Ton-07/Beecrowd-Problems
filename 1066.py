#definimos cinco valores aleatórios e inteiros de entrada
x = int(input())
y = int(input())
z = int(input())
a = int(input())
b = int(input())
#definimos os valores pares, impares, negativos e positivos como "0"
#para que à eles sejam somados os valores da condicional
par = 0
impar = 0
positivo = 0
negativo = 0
#criamos a estrutura da condicional definindo como par os números cujo resto da divisão é zero
#e como impar aquele que não cumpre essa condição.
#definimos como positivo os números maiores que zero e como negativo os números menores que zero.
#definimos também que será somado "1" nas variáveis par ou impar, postivo ou negativo de acordo
#com a condicional cumprida.
if x % 2==0:
    par = par + 1
else:
    impar = impar + 1
if x > 0:
    positivo = positivo + 1
if x < 0:
 negativo = negativo + 1
if y % 2==0:
    par = par + 1
else:
    impar = impar + 1
if y > 0:
    positivo = positivo + 1
if y < 0:
    negativo = negativo + 1
if z % 2==0:
    par = par + 1
else:
    impar = impar + 1
if z > 0:
    positivo = positivo + 1
if z < 0:
    negativo = negativo + 1
if a % 2==0:
    par = par + 1
else:
    impar = impar + 1
if a > 0:
    positivo = positivo + 1
if a < 0:
    negativo = negativo + 1
if b % 2==0:
    par = par + 1
else:
    impar = impar + 1
if b > 0:
    positivo = positivo + 1
if b < 0:
    negativo = negativo + 1
#mostramos os valores pares, impares, positivos e negativos através da função print
print('{0:d} valor(es) par(es)'.format(par))
print('{0:d} valor(es) impar(es)'.format(impar))
print('{0:d} valor(es) positivo(s)'.format(positivo))
print('{0:d} valor(es) negativo(s)'.format(negativo))