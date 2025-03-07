""" esse código foi feito para que os jogadores possam decidir quem será o próximo a pular. Para isso, começamos o código
recebendo um valor de entrada que representará os casos de teste que vem a seguir e criando dois contadores um para o
número de rodadas e outro para a soma dos valoes escolhidos por cada jogador. Criamos um laço de repetição usando o
While e, dentro do While, o programa receberá quatro variáveis uma para o nome do primeiro jogaro, outra para a escolha
do jogaro um, outro para o nome do jogador dois e outro para a escolha do jogador dois. Em seguida o programa
receberá os números escolhidos por cada jogador respectivamente que serão convertidos em inteiros e somados ao contador
soma_valores. Com tudo isso feito, escrevemos as condicionais para cada caso de teste possível das escolhas de cada jogador.
Após as condicionais lidas, o programa somará um ao contador rodadas e irá zerar o contador soma_valores. Por fim, será lido
a condicional que dará fim ao código quando a variável rodadas for igual a variável partidas"""
#valor de casos de teste que vem a seguir
partidas = int(input())
#contador das rodadas
rodadas = 0
#contador que armazenará a soma dos valores dos jogadores
soma_valores = 0
#laço de repetição que será verdadeiro enquanro o número de rodadas for diferente do número de partidas
while True:
#o programa receberá quatro variáveis uma para o nome do primeiro jogaro, outra para a escolha do jogaro um, outro para o nome
#do jogador dois e outro para a escolha do jogador dois
    j1, e1, j2, e2 = input().split()
#o programa receberá os números escolhidos por cada jogador respectivamente
    v1,v2 = input().split()
#os valores são convertidos em inteiros
    v1 = int(v1)
    v2 = int(v2)
#somamos os valores de cada jogador no contador soma_valores
    soma_valores += v1 + v2
#condicinal para caso o jogador 1 tenha escolhido para
    if soma_valores % 2 == 0 and e1 == 'PAR':
        print(j1)
#condicional para caso o jogador 2 tenha escolhido par
    elif soma_valores % 2 == 0 and e2 == 'PAR':
        print(j2)
#condicional para caso o jogador 1 tenha escolhido impar
    elif soma_valores % 2 != 0 and e1 == 'IMPAR':
        print(j1)
#condicional para caso o jogador 2 tenha escolhido par
    elif soma_valores % 2 != 0 and e2 == 'IMPAR':
        print(j2)
#somamos um ao contador rodadas
    rodadas += 1
#zeramos o contador soma_valores
    soma_valores = 0
#condicional que irá parar o laço de repetição quando rodadas for igual a partidas
    if rodadas == partidas:
        break