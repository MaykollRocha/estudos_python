# Exercícios com função


# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

import random


def multiplis(*args):
    mulp = 1
    for i in args:
        mulp *= i

    return mulp, len(args)


chars = [random.randint(0, 10) for i in range(random.randint(1, 11))]

mulp, varis = multiplis(*chars)
print(f'O foram {varis} e a multiplicação deu {mulp}.')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(num=None):
    if num:
        if not num % 2:
            return True
        else:
            return False
    else:
        return False


print(f'{mulp} é par ?', par_impar(mulp))
