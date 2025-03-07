def letra_mais_frequente(texto):
    """Criamos a função letra_mais_frequente que
    recebe um texto e retorna as letras que mais
    aparecem na mensagem caso existam mais de uma letra
    com frequencias iguais"""
    t = len(texto)
    contador_letras = [0] * 26
    for i in range(t):
        caracter = texto[i]
        # se o caracter estiver entre a e z o programa calculará a posição do caracter
        if 'a' <= caracter <= 'z':
            # operação para descobrir a posição. Ex: letra 'e' será a quarta posição pois 101 - 97 = 4
            posicao = ord(caracter) - ord('a')
            # somamos 1 à posição da letra lida
            contador_letras[posicao] += 1
    #str que vai armazenar as letras de maior frequencia
    letras_maior_frequencia = ""
    maior_frequencia = 0
    #for para descobrirmos o valor mácimo da lista contador_letras
    for j in range(len(contador_letras)):
        if contador_letras[j] > maior_frequencia:
            maior_frequencia = contador_letras[j]
    #for para concatenarmos as letras de maior frequencia em letras_maior_frequencia
    for a in range(len(contador_letras)):
        if contador_letras[a] == maior_frequencia:
            letras_maior_frequencia += chr(a + ord('a'))
    #retornamos letras_maior_frequencia
    return letras_maior_frequencia

casos_testes = int(input())
contador_casos_testes = 0
while contador_casos_testes != casos_testes:
    mensagem = input()
    t = len(mensagem)
    #for mar transformar em minúscula
    nova_mensagem = ""
    for i in range(t):
        if 90 >= ord(mensagem[i]) >= 65:
            nova_mensagem += chr(ord(mensagem[i]) + 32)
        else:
            nova_mensagem += mensagem[i]
    #usamos a função letra_mais_frequente para encontrar a letra que mais aparece
    print(letra_mais_frequente(nova_mensagem))
    contador_casos_testes += 1