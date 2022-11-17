# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
import random


def multiplicadorr(mulplex):
    def numultiple(num):
        return num*mulplex
    return numultiple


# for i in range(2, 5):
#     tabuada.append(multiplicadorr(i))

num = random.randint(0, 100)
def tabuada(i): return lambda n: n*i, num


for i in range(len(tabuada)):
    print(f'{num}*{i+2} = {tabuada(i)}')
