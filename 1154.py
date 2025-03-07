"""esse código foi feito para ler um número indeterminado de dados e parar quando um desses valores de entrada
for negativo e, após isso mostrar o valor da média dessas idades com dois dígitos após o ponto. Para isso definimos
 dois contadores que começam em zero sendo um deles para contar o total das somas das idades e outro para contar
 o número de idades inseridas para que depois possamos dividir o total da soama das idades pela quantidade de idade para
 conseguirmos a média. Para isso devemos usar a função while para receber as idades e estabelecer que caso uma dessas idades
  seja negativa o interpretador python deve sair do while e mostar a média das idades que foram armazenadas dentro das variáveis
  totalid e quantidadeid na variável media = totalid / quantidadeid"""
#criamos um contador para a soma das idades
totalid = 0
#crimos outro contador para armazenar a quantidade de idades recebidas
quantidadeid = 0
#usamos o while para que o código possa receber vários valores de entrada repetidamente
while True:
#usamos o int(input()) para recebermos "n" valores de entradas
    idades = int(input())
#escrevemos a condicional que irá tirar o interpretador python do while com todas as informações que ele conseguiu armazenar
#caso a condicional seja respeitada que no nosso cado é o valor da idade ser menor que 0
    if idades < 0:
        break
#somamos ao totain o valor das idades
    totalid = totalid + idades
#somamos à quantidadeid +1 para conseguirmos o número de idades que entraram em idades = int(input())
    quantidadeid = quantidadeid + 1
#calculamos a média das idades fora do while
media = totalid / quantidadeid
#transformamos a media em float
media = float(media)
#mostramos na tela o valor da media com dois dígitos após o ponto
print('{:.2f}'.format(media))