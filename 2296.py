N = int(input())
posi_trilha = 0
contador_N = 0
mnt = 0  

while contador_N < N:
    trilhas = input().split()

    
    menor_valorida = 0
    menor_valorvolta = 0

    
    for i in range(1, int(trilhas[0])):
        if int(trilhas[i]) < int(trilhas[i + 1]):
            menor_valorida += int(trilhas[i + 1]) - int(trilhas[i])

    
    for j in range(int(trilhas[0]), 1, -1):
        if int(trilhas[j - 1]) > int(trilhas[j]):
            menor_valorvolta += int(trilhas[j - 1]) - int(trilhas[j])

    
    if menor_valorida > menor_valorvolta:
        mv = menor_valorvolta
    else:
        mv = menor_valorida

    
    if contador_N == 0 or mv < mnt:  
        mnt = mv
        posi_trilha = contador_N + 1  

    contador_N += 1

print(posi_trilha)

