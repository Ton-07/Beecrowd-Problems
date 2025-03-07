"""esse código foi escrito para calcular o número de pontos de um jogo de dardos por rodada e mostrar o vencedor
de cada round. Para isso o programa deve receber um valor de entrada que determinará o número de rodadas bem como
 deve ser criado 3 contadores: um para os pontos de João, outro para os pontos de Maria e outro para o número de
rodadas. Assim, usaremos o While para criar um laço de repetição de modo que ele repita as rodadas até que se torne
falso que, nessa caso será quando o numero de rodadas for igual a numerorodadas. Para as jogadas de cada indivíduo
fazemos uso do for que criará um laço de repetição no intervalo [0,3) que no caso representa o número de jogadas na
primeira rodada de cada participamte. Ao fim do primeiro round o programa irá mostrar quem foi o vencedor daquela
fase e começará uma nova rodada com os contadores zerados. Esse processo se repetirá até que todas as rodadas
recebidas por numerorodadas sejam jogas """
#definimos 3 contadores: um para os pontos de João, outro para os pontos de Maria e outro para o número de rodadas
Joaoponto = 0
mariaponto = 0
rodadas = 0
#o programa recebe um valor de entrada que será convertido de str para inteiro
numerorodadas = int(input())
#usamos o while para criarmos um laço de repetição
while True:
#usamos o for para criarmos um laço de repetição que deve ir de 0 a 2 mostrando, portando, as tres primeiras
#jogas do primeiro jogador
    for i in range(3):
#o programa recebe 2 valores de entrada que serão convertidos em float
        xj, dj = input().split()
        xj = float(xj)
        dj = float(dj)
#o programa calcula os pontos de João da primeira rodada e soma no contador Joaoponto
        pontosjoao = xj * dj
        Joaoponto += pontosjoao
#a mesma lógica usada no for anterior também é usada aqui
    for i in range(3):
        xm, dm = input().split()
        xm = float(xm)
        dm = float(dm)
        pontosmaria = xm * dm
        mariaponto += pontosmaria
#escrevemos a condicional que mostrará na tela o vencedor e irá zeras os pontos de ambos os jogadores
#para a próxima rodada
    if Joaoponto > mariaponto:
        print('JOAO')
        Joaoponto = 0
        mariaponto = 0
    elif mariaponto > Joaoponto:
        print('MARIA')
        Joaoponto = 0
        mariaponto = 0
#ao fim da rodada será somado 1 ao contador rodada
    rodadas += 1
#o laço de repetição feito pelo while terminará quando o numero de rodadas for igual a numerorodadas
    if rodadas == numerorodadas:
        break