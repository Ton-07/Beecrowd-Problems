"""Esse código foi feito para ajudar Maria a organizar os experimentos de um laboratório o qual ela é
responsável. Para a construção desse código vamos começar criando os contadores para cada animal : coelhos,
ratos e sapos. Além disso devemos criar um contador para acumular o número dos casos de teste e outro para
acumular o total de cobais. Com tudo isso feito, criamos um laço de repetição com o While que so terminará
quando o caso_contador for diferente de casos_testes. Dentro do While o programa receberá duas entras: uma
para a quantidade de animais e outro para o tipo desse animal onde a quantidade de animal será convertida
para inteiro. Tendo essas duas variáveis escrevemos a condicional  para cada animal de modo que o programa
some aos contadores dos animais o valor da variável quantia a depender do tipo de animal. Além disso, o
programa somará mais um ao contador caso_contador para que o While seja interrompido quando a condição
for cumprida. Por fim, calculamos o percentual de cada animal em relação ao total de cobaias utilizadas e 
mostramos na tela o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual
de cada uma em relação ao total de cobaias utilizadas """
#contadores para o número de coelhos, ratos, sapos, para o contar quantos casos de testes ja foram
#e um último para acumular o total de cobais dos experimentos
coellho = 0
rato = 0
sapo = 0
caso_contador = 0
total_cobais = 0
#entrada que indica a quantidade de caso de testes
casos_testes = int(input())
#iniciamos o laço de repetição com o While que so terminará quando o caso_contador for diferente de casos_testes
while caso_contador != casos_testes:
#o interpretador lerá dois valores na mesma linha onde um deles representa a quantidade e o outro o animal
    quantia, animal = input().split()
#transformamos a quantia dos animais para inteiro
    quantia = int(quantia)
#escrevemos as condicionais para cada animal de modo que o programa some aos contadores dos animais o valor
#da variável quantia a depender do tipo de animal
    if animal == 'C':
        coellho += quantia

    elif animal == 'R':
        rato += quantia

    elif animal == 'S':
        sapo += quantia
#somamos um ao contador caso_contador
    caso_contador += 1
#somamos ao contador total_cobais os contadores dos 3 animais para descobrirmos quantos animais foram
#utilizados nos experimentos
total_cobais = coellho + rato + sapo
#calculamos o percentual de cada animal
coelho_percentual = coellho * 100 / total_cobais
rato_percentual = rato * 100 / total_cobais
sapo_percentual = sapo * 100 / total_cobais
#mostramos na tela o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual
#de cada uma em relação ao total de cobaias utilizadas
print('Total: {} cobaias'.format(total_cobais))
print('Total de coelhos: {}'.format(coellho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format(coelho_percentual))
print('Percentual de ratos: {:.2f} %'.format(rato_percentual))
print('Percentual de sapos: {:.2f} %'.format(sapo_percentual))
