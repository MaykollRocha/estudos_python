import random

while True:
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))

    for i, mult in enumerate(range(10, 1, -1)):
        soma = mult*int(cpf[i]) if not i else soma + mult*int(cpf[i])

    soma *= 10
    soma %= 11

    resultado_primeiro_digt = 0 if soma > 9 else soma

    cpf += str(resultado_primeiro_digt)

    for i, mult in enumerate(range(11, 1, -1)):
        soma = mult*int(cpf[i]) if not i else soma + mult*int(cpf[i])

    soma *= 10
    soma %= 11

    resultado_segundo_digt = 0 if soma > 9 else soma

    cpf += str(resultado_segundo_digt)

    if cpf != cpf[0]*len(cpf):
        print(cpf)
        break
