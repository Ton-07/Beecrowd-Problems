casos_testes = int(input())

casos_testes_contador = 0
while casos_testes_contador != casos_testes:
    nome = input()
    nomel = list(nome)
    t = len(nomel)


    nome_facil = True

    
    for i in range(t - 2): 
        if nomel[i] != 'a' and nomel[i] != 'e' and nomel[i] != 'i' and nomel[i] != 'o' and nomel[i] != 'u' and nomel[i] != 'A' and nomel[i] != 'E' and nomel[i] != 'I' and nomel[i] != 'O' and nomel[i] != 'U':
            if nomel[i + 1] != 'a' and nomel[i + 1] != 'e' and nomel[i + 1] != 'i' and nomel[i + 1] != 'o' and nomel[i + 1] != 'u'and nomel[i + 1] != 'A' and nomel[i + 1] != 'E' and nomel[i + 1] != 'I' and nomel[i + 1] != 'O' and nomel[i + 1] != 'U':
                if nomel[i + 2] != 'a' and nomel[i + 2] != 'e' and nomel[i + 2] != 'i' and nomel[i + 2] != 'o' and nomel[i + 2] != 'u'and nomel[i + 2] != 'A' and nomel[i + 2] != 'E' and nomel[i + 2] != 'I' and nomel[i + 2] != 'O' and nomel[i + 2] != 'U':
                    nome_facil = False
                    break  

    
    if nome_facil:
        print("{} eh facil".format(nome))
    else:
        print("{} nao eh facil".format(nome))

    casos_testes_contador += 1
