#o código consiste em permitir a entrada de duas váriaveis na mesma linha.
#Portanto, usa-se a função split para permitir isso e a função input para
#receber os dados do usuário
x1, y1 = input().split()
#aqui estipulamos que as váriaveis são do tipo float
x1 = float(x1)
y1 = float(y1)
#o mesmo feito nos passos acima também é replicado aqui
x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)
#atribuimos a equação da distância em "s" para que pudéssemos resumi-la através do round
s = (((x2-x1)**2 + (y2-y1)**2)**0.5)
#o round foi usado para simplificar o número de casas decimais desejado(4)
rs = round(s,4)
#comando "print" para executar o código
print(rs)