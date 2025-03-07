"""esse código foi feito para ler 2 valores de entrada e mostrar a soma dos números ímpares entre eles.Para
isso, o programa receberá dois valores de entrada para receber os valores de X e Y. Além disos criamos um contador
soma para armazenar o resultado da soma dos valores entre o intervalo de (Y,X). Criamos uma condicional para garantir
que, independente da ordem de entrada de X e Y, o programa sempre mostre o resultado da soma dos números ímpares do
intervalo (Y,X). Depos de assegurarmos o intevalo (Y,X),independente da ordem de entrada das duas variáveis,
vamos fazer outra condicional para que, caso o valor de Y seja ímpar, seja somado 1 a ele tornando-o par de modo a
garantir que apenas os números ímpares entre (Y,X) sejam considerados se o valor de Y for para o programa não fara nada.
Usamos o for para criarmos um laço de repetição que só terminara quando todos os valores ímpares entre (Y,X) forem somandos.
Para assegurar que os valores de i sejam sempre ímpares escvrevemos uma condicional para considerar apenas os valores que possuem
o resto da divisão por 2 diferente de 0 e somando no contador soma todos os valores que i poderá assumir. Então, com
o valor da soma nos números pertencentes ao intervalo (Y,X) mostraremos na tela através da função print o resultado
do contador soma."""
#o programa recebe dois valores de entrada X e Y que são convertidos para inteiros através da função int
x = int(input())
y = int(input())
#contador que armazenará a soma dos ímpares entre (Y,X)
soma = 0
#condicional para garantir que o intervalo recebido sempre seja (Y,X)
if y > x:
    aux = y
    y = x
    x = aux
#se a ordem do intervalo for respeitada o programa não fará nada
else:
    pass
#condicional para que caso o valor de y sejam ímpar ele seja transformado em par
if y % 2 != 0:
    y += 1
#usamos o for para somarmos todos os valores de i no contador soma
    for i in range(y,x):
        if i % 2 != 0:
            soma += i
#se o y for par não sofrerá nenhuma alteração
elif y % 2 == 0:
    y += 0
#a mesma lógica usada no for anterior também se aplica aqui
    for i in range(y,x):
        if i % 2 != 0:
            soma += i

print(soma)