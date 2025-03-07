while True:
    N,M = input().split()
    if N == '-1' and M == '-1':
        break
    N = int(N)
    M = int(M)
    temp_ac = 0
    temp_temporada = 0
    cap = input().split()
    t = len(cap)
    cap_temp = [0]*N
    for i in range(t):
        temp_temporada += int(cap[i]) * M
        cap_temp[i] = temp_temporada
        temp_ac += cap_temp[i]
    print(temp_ac)