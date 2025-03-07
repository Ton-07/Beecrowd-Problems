"""esse código foi criado com a finalidade de ler um Valor de entranda 0<N<13. Portando, usamos o while true
para mostrarmos que, caso o valor de N obedeça a condição escrita no if o código deve ser parado
caso o contrario ele deve proseguir para as próximas etapas. Assim, definimos uma variável chamada
fatorial = 1 para calcular o fatorial dentro do intervalo de (1, N + 1) usando o laço for v range(1, N + 1).
Assim sendo, multiplivamos o valor do fatorial por v e depois mostramos esse valor na tela através da funçãp print"""
#usamos o while True para fazer uma estrutura de repetição que so finaliza caso uma condição seja estabelecida
while True:
# escrevemos N que receberá um valor de entrada
    N = int(input())
#escrevemos uma condicional que finalizará o código caso ela seja cumprida
    if 0 < N < 13:
        break
#definimos uma variável chamada fatorial para armazenar o resultado do fatorial de "N"
fatorial = 1
#usamos um laço de repetição para calcular o fatorial do intervalo de (1, N + 1)
for v in range(1, N + 1):
    fatorial *= v
#mostramos o valor do fatorial na tela
print(fatorial)