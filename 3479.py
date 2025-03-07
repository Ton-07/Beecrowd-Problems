#usamos a função input para recebermos uma entrada e o split('/') para que essa entrada esteja entre barra
#e os valores de "dia"e "mes" sejam lidos na mesma limha. ex: 9/08
dia, mes = input().split('/')
#transformamos os valores de entrada em inteiros através da função int
dia = int(dia)
mes = int(mes)
#escrevemos a condicional e o seu respectivo comando caso a condição seja verdadeira. se a condição
#for falsa será lido a condicional de baixa e executado seu comando e assim sucessivamente.
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print('aries')
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print('touro')
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print('gemeos')
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <=22):
    print('câncer')
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print('leao')
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <=22):
    print('virgem')
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print('libra')
elif (mes == 10 and dia >=23) or (mes == 11 and dia <=21):
    print('escorpiao')
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <=21):
    print('sargitário')
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print('capricornio')
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    print('aquário')
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <=20):
    print('peixes')