"""esse código foi criado para interpretar as piscadas de um corvo de 3 olhos que preve os números
da loteria. As piscadas do corvo são dadas em números binários e a cada grito ele mostra um número
correto da loteria. Para calcularmos esse número criamos dois contadores: um para acumular o valor dos
números e outro para acumular a quantidade de gritos. Com isso em mãos, criamos um laço de repetiço com
o While que só terminara quando o contador gritos for igual a 3. Dentro do While o programa receberá
um valor de entrada que poderá ser um número em binário ou um grito. Se for um número em binario o
programa somará o valor correspondente ao número em binário. """
##escrevemos um contador que armazenará os números sorteados e outro para o número de gritos
gritos = 0
contadorn = 0
#usamos o While para criarmos um laço de repetição que só terminara quando o contador gritos for igual a 3
while True:
#o programa receberá um valor n de entrada 
    n = input()
#se essa entrada for igual a "caw caw" o programa mostrará o valor do contadorn e somará um ao contador
#gritos
    if n == "caw caw":
        print(contadorn)
        contadorn = 0
        gritos = gritos + 1
        if gritos == 3:
            break
#escrevemos a condicional para cada número binario de 0 a 7 de modo que ele somará os números caso necessário
#e mostrara o resultado do contadorn na tela a cada "caw caw"
    elif n  == "--*":
        contadorn = contadorn + 1
    elif n == "-*-":
        contadorn = contadorn + 2
    elif n == "-**":
        contadorn = contadorn + 3
    elif n == "*--":
        contadorn = contadorn + 4
    elif n == "*-*":
        contadorn = contadorn + 5
    elif n == "**-":
        contadorn = contadorn + 6
    else:
        contadorn = contadorn + 7

