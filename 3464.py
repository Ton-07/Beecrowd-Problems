# N, M = Ler os inteiros N e M
nn, mm = input().split()
N = int(nn)
M = int(mm)

# S = ler a quantidade de sensores
S = int(input())

# setores = 0
setores = 0

# para i de 1 a S
for i in range(S):
    # X, Y, R = ler a tripla linha, coluna, alcance
    xx, yy, rr = input().split()
    X = int(xx)
    Y = int(yy)
    R = int(rr)
    
    # Definir limites da linha de acordo com o alcance do sensor
    ix = X - R
    fx = X + R
    
    # Definir limites da coluna de acordo com o alcance do sensor
    iy = Y - R
    fy = Y + R
    
    # Ajustar limites da linha para dentro da matriz
    if ix < 1:
        ix = 1
    if fx > N:
        fx = N
        
    # Ajustar limites da coluna para dentro da matriz
    if iy < 1:
        iy = 1
    if fy > M:
        fy = M
        
    # Calcular o número de setores alcancáveis pelo sensor
    setores += (fx - ix + 1) * (fy - iy + 1)

media = setores / (N*M)

# mostrar inteiro(media)
print(int(media))