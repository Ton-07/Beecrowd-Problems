def in_function(seq, val):
    """
    in_function(seq, val):
    Recebe uma sequência seq, de qualquer tipo,
    e um valor val, e retorna True ou False.
    seq: uma sequência
    val: um valor a ser procurado na sequência
    Retorna True se val está em seq, e False, caso contrário.
    """
    if str(type(seq)) != "<class 'str'>":
        # No caso de lista e tupla, basta verificar
        # se alguma posição armazena val
        for i in range(len(seq)):
            if (val == seq[i]):
                return True
        return False
    else:
        # No caso de string, temos que procurar
        # val em seq. O código a seguir não é o mais eficiente
        # e está apenas aqui para ilustrar. Em Estruturas de
        # Dados serão estudados algoritmos mais eficientes,
        # como o de KMP.
        M = len(val)
        N = len(seq)
        for i in range(0, N-M+1):
            j = 0
            while j < M:
                if (seq[i+j] != val[j]):
                    break;
                j += 1
            if (j == M):
                return True;
        return False

letra = input()
palavra = input().split()
t = len(palavra)
contador_palavra = 0


for i in range(t):
    if in_function(palavra[i],letra):
        contador_palavra += 1

resultado = (contador_palavra/ t) * 100
print('{:.1f}'.format(resultado))