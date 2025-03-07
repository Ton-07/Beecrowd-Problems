#usamos a função input para coletar os dados de entrada
A,B,C = input().split()
#definimos o tipo da entrada como "float"
A = float(A)
B = float(B)
C = float(C)
#criamos uma lista com os valores de entrada
valores = [A, B, C]
#usamos a função ".sort(reverse = True)" para ordenar os valores em ordem decrescente
valores.sort(reverse = True)
A, B, C = valores
#fazemos uso da condicional para definirmos qual o tipo de triângulo que vai ser mostrado na tela
if A>=B+C:
    print('NAO FORMA TRIANGULO')
else:
 if A**2 == B**2 + C**2:
    print('TRIANGULO RETANGULO')
 if A**2>B**2 + C**2:
    print('TRIANGULO OBTUSANGULO')
 if A**2<B**2 + C**2:
    print('TRIANGULO ACUTANGULO')
 if A==B==C:
    print('TRIANGULO EQUILATERO')
 if A == B != C or A == C != B or B == C != A:
    print('TRIANGULO ISOSCELES')