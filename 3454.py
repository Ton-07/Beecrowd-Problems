#estipulamos um valor de entrada
A = input()

#aqui verificamos o vencedor, as inconsistência ou empate
if A == 'XXO' or A == 'OXX':
    print('Alice')

elif A == 'XOX':
    print('*')

else:
    print('?')