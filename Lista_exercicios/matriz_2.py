'''
Lista de matriz 2
nome: Maykoll Rocha
data: 16/11/2022
um lista que era em C sendo passa para python.

'''
import random

'''
Ex 1. Crie um programa que preencha todos os valores de 
uma matriz 2x2, e em seguida exiba todos os valores.

matrix = [[random.randint(0, 100) for j in range(2)] for i in range(2)]

print(*matrix, sep='\n')

'''

'''
Ex 2. Faça um programa que leia uma matriz 3 x 3, conte e 
escreva quantos valores maiores que 5 ela possui.

matrix = [[random.randint(0, 10) for j in range(3)] for i in range(3)]
cont = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] > 5:
            cont += 1

print(f'Temos {cont} valores maiores que 5.')

'''

'''
Ex 3. Escreva um programa que declare e preencha uma 
matriz (5x5) com valores fornecidos pelo usuário. Em 
seguida, o programa deve imprimir os elementos da 
diagonal principal

matrix = [[abs(int(input('valor: ')))for j in range(5)] for i in range(5)]

for i in range(5):
    for j in range(5):
        if i == j:
            print(f'[{i}][{j}]={matrix[i][j]}')
            
'''

'''
Ex 4. Faça um programa que leia uma matriz 4 x 4 e, após 
a leitura de todos os valores, mostre quantos números 
pares ela possui, e exiba a posição em que cada número 
par se encontra e a soma de todos os números pares.

matrix = [[random.randint(0, 9) for j in range(4)] for i in range(4)]
cont = 0
soma = 0
for i in range(4):
    for j in range(4):
        if not matrix[i][j] % 2:
            print(f'[{i}][{j}]={matrix[i][j]}')
            cont += 1
            soma += matrix[i][j]
print(f'A soma deu {soma} e tem {cont} numros pares.')

'''

'''
Os dois ultimos exercios da lisa é muito mais aplicado ao C vou deixalos aqui 
porem não irei resolvelos:
Ex 5. Faça uma solução para armazenar o primeiro nome 
de 5 pessoas e depois mostrar tais nomes. Use a função 
scanf( ) e o formato %s para receber cada nome e para 
imprimi-los, posteriormente.

A ideia do primeiro é uma matriz de char em C exemplo char [5][20]
onde as colunas são o local do nome e o resto pra por o nome tipo no 
nome[0] teira um nome de X carctares < que 20 em python isso não é 
problema ja que toda char é string.


Ex 6. Idem ao exercício anterior, mas agora use a função 
fgets( ) para receber nome e sobrenome

'''
