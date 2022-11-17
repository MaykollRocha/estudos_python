'''
Nome: Maykoll Rocha
data: 16/11/2022
É uma lista de matriz.
'''
import random

'''
1. Faça uma solução para inicializar uma matriz quadrada de tamanho 3, 
automaticamente, tal que o elemento a posição (i,j) seja 2*i+j. Em 
seguida, o usuário poderá escolher uma das seguintes operações:
Use a estrutura switch-case para a seleção da opção
A) imprimir todos os elemtentos da mariz
B) somar os elementos de cada linha e mostrar o resultado
C) somar os elementos de cada coluna e mostrar o resultado
D) imprimir os elementos da diagonal principal
E) imprimir todos os elementos, exceto os da diagonal principal
F) imprimir os elementos, tal que a linha é par e a coluna é ímpar
G) imprimir os elementos da coluna 0, apena

matriz = [[2*i+j for j in range(3)] for i in range(3)]

print('\nimprimir os elementos da coluna 0, apenas:')
for j in range(3):
    print(matriz[0][j], end='-')

while True:
    print('\nA) imprimir todos os elemtentos da mariz',
          'B) somar os elementos de cada linha e mostrar o resultado',
          'C) somar os elementos de cada coluna e mostrar o resultado',
          'D) imprimir os elementos da diagonal principal',
          'E) imprimir todos os elementos, exceto os da diagonal principal',
          'F) imprimir os elementos, tal que a linha é par e a coluna é ímpar',
          'G) imprimir os elementos da coluna 0, apenas', sep='\n')
    op = input('Entre com a letra: ').upper() or 'S'

    match op:
        case 'A':
            print('Todos os elementos:')
            for i in range(3):
                print(*matriz[i], sep='-')
        case 'B':
            print('Soma das linhas:')
            for i in range(3):
                soma = 0
                for j in range(3):
                    soma += matriz[i][j]
                print(i, soma)
        case 'C':
            print('Soma de cada coluna: ')
            for j in range(3):
                soma = 0
                for i in range(3):
                    soma += matriz[i][j]
                print(j, soma)
        case 'D':
            print('Diagonal Pricipal: ')
            for i in range(3):
                for j in range(3):
                    if j == i:
                        print(matriz[i][j], end='-')
        case 'E':
            print('\nTudo menos diagonal principal: ')
            for i in range(3):
                for j in range(3):
                    if not j == i:
                        print(matriz[i][j], end='-')
        case 'F':
            print('\nImprimir os elementos j é par e i é ímpar: ')
            for i in range(3):
                for j in range(3):
                    if not j % 2 and i % 2:
                        print(matriz[i][j], end='-')
        case 'G':
            print('\nimprimir os elementos da coluna 0, apenas:')
            for j in range(3):
                print(matriz[0][j], end='-')
        case 'S':
            break
        case _:
            print('valor invalido.')

'''

'''
2. Faça uma solução para guardar valores numéricos em uma matriz de 
tamanho NxM
Em seguida, leia os elementos da matriz e imprima o menor e o maior 
valor dessa matriz, bem como a respectiva posição onde se encontram tais 
elementos

n = random.randint(1, 5)
m = random.randint(1, 5)
matriz = [[random.randint(0, 100) for j in range(m)] for i in range(n)]
for i in range(n):
    print(matriz[i])

maior = matriz[0][0]
menor = matriz[0][0]
repo_maio = [matriz[0][0], 0, 0]
repo_menor = [matriz[0][0], 0, 0]
for i in range(n):
    for j in range(m):
        if maior < matriz[i][j]:
            repo_maior = [matriz[i][j], i, j]
            maior = matriz[i][j]

        if menor > matriz[i][j]:
            repo_menor = [matriz[i][j], i, j]
            menor = matriz[i][j]
print('-'*10)
print(repo_menor)
print(repo_maior)

'''

'''
3. Faça uma solução para guardar valores numéricos em uma matriz A 
quadrada de tamanho N. Em seguida, guarde em B a matriz transposta de A

matrizA = [[random.randint(0, 100) for j in range(2)] for i in range(2)]
matrizB = [[matrizA[j][i] for j in range(2)] for i in range(2)]
for i in range(2):
    print(matrizA[i])
print('-'*10)
for i in range(2):
    print(matrizB[i])
    
'''
