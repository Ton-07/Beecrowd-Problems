mensagem = input().split()
mensagem_decodificada = ""
contador = 0
t = len(mensagem)

for i in range(t):
    m = str(mensagem[i])
    t1 = len(m)
    for j in range(t1):
        if j % 2 != 0:
            mensagem_decodificada += m[j]
    contador += 1
    if contador == t:
        break
    mensagem_decodificada += ' '

print(mensagem_decodificada)