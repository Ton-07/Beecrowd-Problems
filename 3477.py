#definimos tres valores de entrada que serão recebidos pelo input e lidos
#na mesma linha pelo split
X, Y, Z = input().split()
#transformamos os valores em inteiros através da função int
X = int(X)
Y = int(Y)
Z = int(Z)
#escrevemos a fórmula da área do círculo e dividimos por 2
Asc = (3*(Z/2)**2)/2
#verificamos se os valores formam um triangulo retangulo
if X**2 == Y**2 + Z**2:
#calculamos a área do triangulo
    area = ((Z*Y)/2)
#somamos a área do triangulo com a área do semi círculo para termos a área total
    Areatotal = area + Asc
#transformamos o resultado da área total em inteiro 
    areainteira = int(Areatotal)
#mostramos na tela o resultado caso os lados formem um triangulo
    print('AREA = {}'.format(areainteira))
#se não formar um triangulo mostraremos na tela a mensagem "Nao eh retangulo!"
else: print('Nao eh retangulo!')