#usamos a função input junto da split para que os 3 valores possam ser lidos na mesma linha
a,b,c = input().split()
#definimos que "a","b","c" são inteiros através da função "int"
a = int(a)
b = int(b)
c = int(c)
#escrevemos a fórmula que calcula o menor entre "a" e "b"
maior_AB = (a+b+abs(a-b))/2
#usamos a condicional para definir se o maior entre "a" e "b" tbm é maior ou menor que "c".
#Com base n condicional mostrasse uma das duas mensagens na tela
if c > maior_AB:
 print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(int(maior_AB)))