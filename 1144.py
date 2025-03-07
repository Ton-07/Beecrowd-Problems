"""A questão pede que resolvamos uma sequência lógica a partir de um número de entrada. Para a logica dessa
sequência, pode-se inferir que os valores da primeira linha são dados pelo valor de i que irá interar no intervalo
de [1,6) e os valores de i**2 e i**3, ja na segunda linha temos os valores de i, i**2 + 1, i**3 + 1, ou seja,apenas
vamos somar um ao quadrado e ao cubo de i. Assim, garantimos que valor das linhas mostradas sejam n*2 e contruimos
a sequência lógica desse exercício"""
#valor de entrada n
n = int(input())
#laço de repetição no intervalo [1,6)
for i in range(1, n + 1):
    print(i, i**2, i**3)
    print(i, i**2 + 1, i**3 + 1)