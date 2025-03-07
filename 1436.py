T = int(input())
contador_T = 0
x = 0
while contador_T != T:
    N = input().split()
    N_jogadores = int(N[0])
    p_cap = int((N_jogadores + 1) // 2)
    x +=1
    print('Case {}: {}'.format(x,N[p_cap]))
    contador_T +=1
