"""Esse programa foi feito para ler dois valores X e Y e a seguir, mostre uma sequência de 1 até Y, passando para
a próxima linha a cada X números. Para isso, o programa receberá dois valores de entrada x e y que serão convertidos
para inteiros e será definido um valor z como 1, que será o início da sequência atual. Além de definirmos rep como
x, que representa a quantidade de números a serem impressos em cada linha. Após isso, escrevemos a condicional que
limita o intervalo de x e y e, dentro dessa condicional, usamos for i in range para cada repetição necessária para 
imprimir a sequência até o valor y para cada número na linha atual  Imprimimos o número seguido de um espaço, exceto
se for o último número da linha , de modo que mostramos na tela o valor de i e usamos o end para que o próximo valor 
de i seja lido na mesma linha. Se o resto da divisão de i por x for igual a 0, o programa irá para a próxima linha.
Se não for o último valor da linha, imprime um espaço em branco. Por fim atualiza o início da próxima linha e atualiza
x para o próximo número a ser impresso na linha seguinte"""

# Recebe dois valores de entrada x e y
x, y = input().split()

# Converte os valores para inteiros
x = int(x)
y = int(y)

# Define z como 1, que será o início da sequência atual
z = 1

# Define rep como x, que representa a quantidade de números a serem impressos em cada linha
rep = x

# Verifica se x e y estão dentro dos limites especificados
if 1 < x < 20 and x < y < 100000:
    # Para cada repetição necessária para imprimir a sequência até o valor y
    for n in range(1, (y // x) + 1):
        # Para cada número na linha atual
        for i in range(z, x + 1):
            # Imprime o número seguido de um espaço, exceto se for o último número da linha
            if i != x:
                print(i, end=" ")
            # Se for o último número da linha, imprime o número sem espaço e quebra de linha
            elif i == x:
                print(i)

        # Atualiza o início da próxima linha
        z = z + rep
        # Atualiza x para o próximo número a ser impresso na linha seguinte
        x = x + rep
