"""esse código foi feito para ler um valor x de entrada e mostra na tela os 6 valores ímpares
consecutivos a partir de X. Para isso usamos a variável X para receber um valor de entrada que
será convertido em inteiro e criamos um contador para mostrar os 6 números ímpares consecutivos
de x. Depois disso escrevemos uma condicional para caso o número seja ímpar e outra para caso
ele seja par. Para o número ímpar usaremos o for com um intervalo de [0,12) e pediremos que ele
pule 2 casas para cada valor de i garantindo que os próximos 6 valores consecutivos de x sejam
ímpares.Para os números pares usaremos a mesma lógica com a diferença de que somaremos 1 no
contador soma para garantir que o primeiro número mostrado na tela seja ímpar"""
#x recebe um valor de entrada
x = int(input())
#criamos um contador para armazenar cada número ímpar consecutivo de X
soma = 0
#escrevemos uma condicional para caso o número seja par
if x % 2 == 0:
#usamos o for para criar um laço de repetição que vai de [0,12) e pula duas casas decimais 
#dentro do intervalo
    for i in range(0,12,2):
#somamos 1 ao valor de x para garantirmos que o primeiro número seja ímpar e somamos i para
#que o contador soma sempre receba valores ímpares
        soma = x + i + 1
#mostramos na tela os diferentes resultados do contador soma um em cada linha
        print(soma)
#condicional para caso o número seja ímpar
elif x % 2 != 0:
#a mesma lógica usado para os pares também é usada aqui com a diferença de que não somamos um ao contador
#soma pois ele já é ímpar e deve ser mostrado na tela
    for i in range(0,12,2):
        soma = x + i
        print(soma)
