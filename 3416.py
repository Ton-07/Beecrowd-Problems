#usamos o "input" para receber um valor de entrada e a função ".split" para que
#esses valores sejam lidos na mesma linha
N, L, D = input().split()
#transformamos os valores em inteiros através da função "int"
N = int(N)
L = int(L)
D = int(D)
#usamos a função "import math" para que possamos usar a função  math.ceil que arredondará o valor para
#cima para o inteiro mais próximo
import math
#escrevemos a operação que mostra a quantidade de litros de café que o Prof. Galou precisa preparar.
Quantidade_cafe_litros = math.ceil(N * D / 1000 / L) * L
#usamos a função "print" para mostrar os valores na tela
print('{}'.format(Quantidade_cafe_litros))