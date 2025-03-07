"""esse código foi feito para mostrar a diferença entre o número dos soldados de Hashmat e do
exército inimigo. Para isso usamos um laço de repetição que vai calcular essa diferença até
que a entrada termine com o fim do arquivo (EOF). Usamos o try e o except para lidar com
exceções, que são erros que ocorrem durante a execução do programa. No nosso caso a exceção
sera o EOF que acontecerá quando a função input atinge o final de arquivo de entrada sem ler
qualquer dado. Escrevemos, dentro do try, os inputs que vão receber os valores dos soldados
de Hashmat e dos soldados inimigos. Após isso esvrevemos a condicional para garantir que o
resultado da subtração sempre será um valor positivo independente da ordem de entrada. Após
isso, escrevemos outra condicional que mostrará a diferença entre o número de soldados de
Hashmat e do seu oponente desde que os valores recebidos pelos inputs sejam menores ou iguais
a 2**32. Por fim, escrevemos o except com o comando EOF e dizemos que se isso acontecer o laço
de repetição gerado pelo while deve ser finalizado"""
#o while vai criar um laço de repetição
while True:
#escrevemos o código dentro do try para que o python tente executar esse código de modo que
#se alguma exceção ocorrer nesse código o python vai procurar um bloco except
    try:
#o programa vai receber dois valores de entrada na mesma linha
        soldadosh, soldadosi = input().split()
        soldadosh = int(soldadosh)
        soldadosi = int(soldadosi)
#condicional para garantir que a ordem de entrada dos valores não importa de modo a sempre garantir
#um valor positivo como resposta
        if soldadosi > soldadosh:
            aux = soldadosh
            soldadosh = soldadosi
            soldadosi = aux
        else:
            pass
#condicional que vai calcular a diferença entre os soldados de Hashmat e de seu oponente caso os valores
#de entrada seja menor ou igual que 2**32 e vai mostrar essa diferença na tela
        if soldadosh <= 2**32 or soldadosi <= 2**32:
            diferença = soldadosh - soldadosi
            print(diferença)
#bloco except contendo o EOFError e o comando para parar o while caso o EOFError seja cumprido.
    except EOFError:
        break
