while True:
    try:
        cpf = input()
        cpf = list(cpf)
        CPF = [0]*11
        t = len(cpf)
        b1 = 0
        mult1 = 1
        b2 = 0
        mult2 = 9
        somab2 = 0
        somab1 = 0

        for i in range(t):
            if cpf[i] != '.' and cpf[i] != '-':
                CPF[i] = int(cpf[i])
                b1 = CPF[i] * mult1
                mult1 = mult1 + 1
                somab1 += b1

                b2 = CPF[i] * mult2
                mult2 = mult2 - 1
                somab2 += b2
                if mult2 == 0 and mult1 == 10:
                    b1 = somab1 % 11
                    b2 = somab2 % 11
                    break
        if b1 == 10:
            b1 = 0
        if b2 == 10:
            b2 = 0

        if b1 == int(cpf[12]) and b2 == int(cpf[13]):
            print('CPF valido')
        else:
            print('CPF invalido')
    except EOFError:
        break
