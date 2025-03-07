"""A questão pede para ajudarmos Sr Pi encontrar o tamanho mínimo de terreno necessário para construir
uma casa, de acordo com as regulamentações municipais.Para isso, começamos o  código criando um laço de
repetição através do While que só se encerrará quando o valor de entrada x for igual a '0'. Dentro do
While escrevemos um valor de entrada x que terá seus valores de entrada atribuídos para 3 outras variáveis
de modo que eles sejam lidas na mesma linha usando o .split. Com os 3 valores de entrada convertidos
para inteiros, calculamos a área total com os 2 primeiros valores que representam o lado do quadrado e usamos
o terceiro valor, respectivamente, para calcularmos a fração do terreno total disponível para construção
dividindo esse valor por 100 de modo a torna-lo uma fração para que assim possamos descobrir a área de construção
possível dentro do terreno disponível.Por fim, mostramos na tela a área de construção possível dentro do terreno
disponível após ele ter sido transformada para um valor inteiro"""
#laço de repetição feito com o While
while True:
#o programa receberá um valor de entrada x
    x = input()
#se x = '0' o programa irá sair do looping
    if x == '0':
        break
#atribuímos os valores de entrada de x para 3 variáveis e transformamos x em .split para que ele leia mais de um
#valor na mesma linha
    l1,l2,am = x.split()
#transformamos os valores l1,l2 e am em inteiros
    l1 = int(l1)
    l2 = int(l2)
    am = int(am)
#calculamos a área total da casa
    area = l1*l2
#calculamos a fração do terreno total disponível para construção.
    area_contrução = area/(am/100)
#calculamos a área de construção possível dentro do terreno disponível
    tm = (area_contrução)**0.5
#transformamos tm em inteiro e mostramos ele na tela
    tm = int(tm)
    print('{}'.format(tm))