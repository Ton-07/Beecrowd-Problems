matriz_dimensao = int(input())
p, q, r, s, x, y = input().split()
p = int(p)
q = int(q)
r = int(r)
s = int(s)
x = int(x)
y = int(y)
i_c, j_c = input().split()
valor = 0
i_c = int(i_c)
j_c = int(j_c)
C_ij = 0

for k in range(1, matriz_dimensao + 1):
#calculanmos o valor de A_ij e B_ij
    A_ij = (p * i_c + q * k) % x
    B_ij = (r * k + s * j_c) % y
#acumulamos o resultado em C_ij
    C_ij += A_ij * B_ij

print(C_ij)