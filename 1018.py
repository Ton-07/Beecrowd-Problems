#notas recebe um valor "x" que é transformado em inteiro
notas = int(input())
#realizamos uma divisão inteira por 100 para descobrirmos o número de notas de 100
notas100 = notas // 100
#usamos uma variável auxiliar para armazenarmos o resto da divisão de notas por 100. A mesma lógica
#usada nessa linha vai se repetir nas demais, onde vamos sempre realizar divisões inteiras
#e atualizar o valor da variável aleatoria "nr"
nr= notas%100
notas50 = nr// 50
nr = nr % 50
notas20 = nr//20
nr = nr % 20
notas10 = nr//10
nr = nr % 10
notas5 = nr//5
nr = nr % 5
notas2 = nr//2
nr = nr % 2
notas1 = nr//1
#usamos a função "print" para mostrarmos na tela as quantidades do número de notas de cada valor pedido e o valor inicial
print('{}'.format(notas))
print('{} nota(s) de R$ 100,00'.format(notas100))
print('{} nota(s) de R$ 50,00'.format(notas50))
print('{} nota(s) de R$ 20,00'.format(notas20))
print('{} nota(s) de R$ 10,00'.format(notas10))
print('{} nota(s) de R$ 5,00'.format(notas5))
print('{} nota(s) de R$ 2,00'.format(notas2))
print('{} nota(s) de R$ 1,00'.format(notas1))
