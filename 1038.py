#primeiro cria-se uma lista para armazenar os valores do prato e seus respectivos
#códigos
itens = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
#usando o input para que as variáveis usadas possam receber os valores desejados e o split
#para que esses valores possam ser lidos na mesma linha
pedido, quantidade = input().split()
#transformamos os valores de "pedido" e quantidade em float
prato = float(pedido)
quantidade = float(quantidade)
#definimos que os valores usados devem vir da lista"itens" criada e multiplicamos pela quantidade desejada
pratos_escolhidos = itens[prato] * quantidade
#mostramos na tela com o print o valor arredodado com duas casas decimais
print('Total: R$ {:.2f}'.format(pratos_escolhidos))