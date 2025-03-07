#atribui-se input e float nas variáveis "tempo_gasto" e "velocidade_media"
#para que elas possam receber valores do tipo float
tempo_gasto = float(input())
velocidade_media = float(input())
#atribui-se a fórmula da distância percorrida à "distancia_percorrida"
distancia_percorrida = tempo_gasto*velocidade_media
#calcula-se os litros usados
litros_usados = distancia_percorrida/12
#pedimos para mostrar na tela o resultado do litros_simplificados usando (:.3f) para
#sinalizar que o resultado deve ser impresso com 3 casas decimais após o ponto
print('{:.3f}'.format(litros_usados))