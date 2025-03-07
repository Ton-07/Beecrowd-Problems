#usamos o "input" para receber um valor de entrada que será convertido em inteiro
#atravé da função "int"
idade_dias = int(input())
#fazemos uma divisão inteira entre o valor de entrada e 365 dias que corresponde à um anopara descobrir
#a idade em anos
idade_anos = idade_dias // 365
#com o resto da divisão de dias dividido por 365 dividimos ele por 30 para descobrir o
#número de meses
idade_meses = (idade_dias % 365) // 30
#com o resto da divisão de idade_dias por 365 fazemos o resto desse valor por 30
#para descobriemos o número de dias
idade_dias_resto = (idade_dias % 365) % 30
#usamos a função "print" para mostrar os valores na tela
print('{} ano(s)'.format(idade_anos))
print('{} mes(es)'.format(idade_meses))
print('{} dia(s)'.format(idade_dias_resto))