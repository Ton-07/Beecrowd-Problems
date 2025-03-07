"""Este código foi desenvolvido para encontrar o K-ésimo número na sequência de Fibonot, uma série de números inteiros
positivos que não fazem parte da famosa sequência de Fibonacci. Para alcançar esse objetivo, o programa inicia inicializando
variáveis para contar os números na sequência de Fibonot e definir o número atual a ser verificado. Após isso, entra em um
loop que continua indefinidamente até que o K-ésimo número de Fibonot seja encontrado. Dentro desse loop, o programa verifica
se o número atual pertence à sequência de Fibonacci, usando uma troca de variáveis para percorrer essa sequência. Se o número 
não pertencer à sequência de Fibonacci, ele é contado como parte da sequência de Fibonot. Quando o K-ésimo número de Fibonot é 
encontrado, o programa o mostra esse valor na tela. Em resumo, o código itera pelos números inteiros positivos, verifica se 
eles pertencem à sequência de Fibonacci, conta os números que não pertencem (sequência de Fibonot) e imprime o K-ésimo número 
de Fibonot encontrado"""
#k-éssimo termo da sequência
k = int(input())

#criamos um contador para contar os números da sequencia de fibonot
fibonot_contador = 0
#criamos a variável num como 1, que será nosso contador para iterar pelos números inteiros positivos.
num = 1

#criamos um loop infinito para iterar pelos números inteiros positivos até encontrar o K-ésimo número de Fibonot.
while True:
    num += 1

# Verificação se o número atual pertence à sequência de Fibonacci
    é_fibonacci = False
#a e b são os dois primeiros termos da sequência de Fibonacci
    a = 1
    b = 1
#criamos um um loop dentro do loop principal para verificar se o
#número atual (num) pertence à sequência de Fibonacci
    while a <= num:
#se a for igual a num o While é encerrado e a variável é_fibonacci se torda Verdadeira
        if a == num:
            é_fibonacci = True
            break
        aux = a
#Atualizamos o valor de a para o valor de b, que é o próximo número na sequência de Fibonacci.
        a = b
#Atualizamos o valor de b para a soma do valor anterior de a (armazenado em aux) e
# o valor atual de a, o que nos dá o próximo número na sequência de Fibonacci.
        b = aux + a

#Se o número atual não pertencer à sequência de Fibonacci soma-se 1 a variável fibonot_contador
    if not é_fibonacci:
        fibonot_contador += 1

#Se encontrarmos o k-ésimo número da sequência de Fibonot, encerramos a iteração
        if fibonot_contador == k:
            break
#mostramos na tela o contador num
print(num)