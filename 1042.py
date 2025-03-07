#usamoas input e .split para receber mais de um valor na mesma linha
x, y, z = input().split()
#transformamos os valores recebidos em inteiros através da função int
x = int(x)
y = int(y)
z = int(z)
#atribuimos os primeiros valores de x,y e z nas variáveis a,b e c
a = x
b = y
c = z
#escrevemos a condicional para deixar os valores em ordem crescente
if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y
#escrevemos os valores que queremos mostrar na tela
print(x)
print(y)
print(z)
print()
print(a)
print(b)
print(c)