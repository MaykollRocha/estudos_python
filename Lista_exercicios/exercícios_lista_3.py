import random

'''
nome: Maykoll Rocha
dia: 14/11/2022
site: https://wiki.python.org.br/EstruturaDeRepeticao
'''

'''
1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor 
válido.


nota = -1
while 0 > nota < 10:
    nota = float(input('Entre com a nota: '))
    if 0 > nota < 10:
        print('Invalida')
else:
    print('Valido.')
    
'''

'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as 
informações.

while True:
    nome = input('Nome: ').capitalize()
    inputpass = input('senha: ')
    if inputpass.capitalize() == nome:
        print('ERRO')
    else:
        break

'''

'''
3.Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Name: ')
    idade = abs(int(input('Idade:')))
    salario = abs(float(input('Salario: ')))
    sexo = input('Sexo: ').lower()
    estado_civil = input('Estado Civil: ').lower()
    if len(nome) > 3 and idade < 151 and sexo in 'mf' and estado_civil in 'scvd':
        break
        
'''

'''
4.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale 
a população do país B, mantidas as taxas de crescimento.

a = 80000
b = 200000
anos = 0
while a < b:
    a += a*0.03
    b += b*0.015
    anos += 1
print(anos)

'''

'''
5.Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = abs(int(input("Entre com a população A:")))
txca = abs(float(input("Entre com a taxa de crescimento de A:")))/100
b = abs(int(input("Entre com a população B:")))
txcb = abs(float(input("Entre com a taxa de crescimento de B:")))/100
anos = 0
while a < b:
    a += a*txca
    b += b*txcb
    anos += 1
print(anos)

'''

'''
6.Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    print(i, end=' ')

'''

'''
7.Faça um programa que leia 5 números e informe o maior número.
maior = -11
for i in range(5):
    num = random.randrange(100)
    if maior < num:
        maior = num
print(maior)
'''

'''
8.Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range(5):
    num = random.randrange(100)
    soma += num
print(f'{soma=} media={soma//5}')
'''

'''
9.Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for i in range(1, 51):
    if i % 2:
        print(i)

'''

'''
10.Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.

lim_inf = abs(int(input('Entre com o limite inferior: ')))
lim_sup = abs(int(input('Entre com o limite superior: ')))

for i in range(lim_inf + 1, lim_sup):
    print(i, end=' ')
'''

'''
11.Altere o programa anterior para mostrar no final a soma dos números.

lim_inf = abs(int(input('Entre com o limite inferior: ')))
lim_sup = abs(int(input('Entre com o limite superior: ')))
soma = 0
for i in range(lim_inf + 1, lim_sup):
    soma += i
print(f'{soma=}')
'''

'''
12.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a 
tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

num = abs(int(input('Entre com um numero inteiro de 1-10: ')))

if 1 <= num <= 10:
    print(f'Tabuada de {num}: ')
    for i in range(1, 11):
        print(f'{num} X {i} = {num*i}')
else:
    print('Valor invalido.')
'''

'''
13.Faça um programa que peça dois números, base e expoente, calcule e mostre o 
primeiro número elevado ao segundo número. Não utilize a função de potência da
linguagem.

base = int(input('Entre com a base: '))
expoente = abs(int(input('Entre com o expoente: ')))

if expoente != 0 and base != 0:
    pot = 1
    for i in range(1, expoente+1):
        pot *= base
    print(f'{pot=}')

'''

'''
14.Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade 
de números pares e a quantidade de números impares.

num_par = 0
num_impar = 0
for i in range(10):
    num = random.randrange(100)
    if not num % 2:
        num_par += 1
    else:
        num_impar += 1

print(f'{num_impar=} {num_par=}')

'''

'''
15.A série de Fibonacci é formadapela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o nésimo termo.
n = int(input('Qual termo quer ver: '))
n1 = 1
n2 = 1
for i in range(n-2):
    aux = n1 + n2
    print(aux)
    n1 = n2
    n2 = aux

'''

'''
16.A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.

n1 = 1
n2 = 1
while n1+n2 < 500:
    aux = n1 + n2
    print(aux)
    n1 = n2
    n2 = aux

'''

'''
17.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo 
usuário. Ex.: 5!=5.4.3.2.1=120

num = abs(int(input('Entre com o N: ')))
fat = 1
for i in range(1, num+1):
    fat *= i
print(f'{fat=}')

'''

'''
18.Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.

n = abs(int(input('Entre ate que termo tera a conta: ')))
menor = random.randrange(1, 100)
maior = 0
for i in range(n):
    num = random.randrange(1, 100)

    if menor > num:
        menor = num

    if maior < num:
        maior = num

print(f'{maior=} {menor=} soma={menor+maior}')

'''

'''
19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = abs(int(input('Entre ate que termo tera a conta: ')))
menor = random.randrange(1, 100)
maior = 0
for i in range(n):
    num = random.randrange(0, 1000)

    if menor > num:
        menor = num

    if maior < num:
        maior = num

print(f'{maior=} {menor=} soma={menor+maior}')
'''

'''
20.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
fatorial várias vezes e limitando o fatorial a números inteiros positivos e 
menores que 16.

while True:
    num = abs(int(input('Entre com o N: ')))
    if num <= 16:
        fat = 1
        for i in range(1, num+1):
            fat *= i
        print(f'{fat=}')
    else:
        break
'''

'''
21.Faça um programa que peça um número inteiro e determine se ele é ou não um 
número primo. Um número primo é aquele que é divisível somente por ele mesmo 
e por 1.

num = abs(int(input('Entre com um numero primo: ')))

for i in range(2, num+1):
    if not num % i:
        break

if i == num:
    print('é primo')
else:
    print('Não é primo.')
'''

'''
22.Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível.

num = abs(int(input('Entre com um numero primo: ')))

for i in range(2, num+1):
    if not num % i:
        break

if i == num:
    print('é primo')
else:
    print('Não é primo.')
    for p in range(1, num + 1):
        if not num % p:
            print(p, end=' ')
            
'''

'''
23.Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos. Serão avaliados o
funcionamento, o estilo e o número de testes (divisões) executados.

n = abs(int(input('Entre com o n-ésimo termo: ')))
for k in range(n+1):
    num = k
    num_div = 1
    for i in range(2, num+1):
        if not num % i:
            break
    else:
        i = k

    if i == num:
        print(f'{k} é primo')
    else:
        print(f'{k} Não é primo.')
        for p in range(1, num + 1):
            if not num % p:
                print(p, end=' ')
        print('\n')

'''

'''
24.Faça um programa que calcule o mostre a média aritmética de N notas.
n = abs(int(input('Entre com o n-ésimo: ')))
soma = 0
for i in range(n):
    notas = random.randrange(0, 10)
    soma += notas

print('medias = ', soma/n)

'''

'''
25.Faça um programa que peça para n pessoas a sua idade, ao final o programa 
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior
que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média 
calculada.

cont = 0
soma = 0
while True:
    idade = int(input('Entre com a idade: '))
    if idade < 0:
        break

    soma += idade
    cont += 1

if soma/cont <= 25:
    print('Jovem')
elif 26 <= soma/cont < 60:
    print('Adulto')
else:
    print('Idosa')

'''

'''
26.Numa eleição existem três candidatos. Faça um programa que peça o número 
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato

candidato_A = 0
candidato_B = 0
candidato_C = 0
while True:
    voto = input('A - B - C : ').upper() or 'd'

    match voto:
        case 'A': candidato_A += 1
        case 'B': candidato_B += 1
        case 'C': candidato_C += 1
        case _: break

print(f'{candidato_A=} {candidato_B=} {candidato_C=}')

'''

'''
27.Faça um programa que calcule o número médio de alunos por turma. Para isto, 
peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas 
não podem ter mais de 40 alunos.

turmas = abs(int(input('Entre com o número de turmas: ')))
alunos = 41#Força entrada no laço while.
total_alunos = 0
for i in range(turmas):
    while alunos > 40:
        alunos = abs(int(input(f'Entre com o numero de aulos da turmas {i}: ')))
    total_alunos += alunos
    alunos = 41#Forçar voltar pro laço while.


print(f'A media de aulos por turma é de {total_alunos/turmas}')

'''

'''
28.Faça um programa que calcule o valor total investido por um colecionador em 
sua coleção de CDs e o valor médio gastoem cada um deles. O usuário deverá 
informar a quantidade de CDs e o valor para em cada um.

cds = abs(int(input('Entre com o numero de Cds:')))
valor_total = 0
for i in range(cds):
    valor_cds = abs(float(input(f'Quando você gastou no cd {i}: ')))
    valor_total += valor_cds
print(f'O valor total foi de R${valor_total:.2f} e'
      f'a media por cd foi de {valor_total/cds:.2f}.')

'''

'''
29.O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca 
de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele 
desenvolveu um tabela que contém o número de itens que o cliente comprou e ao 
lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar 
quantos itens o cliente está levando e olhar na tabela de preços. Você foi 
contratado para desenvolver o programa que monta esta tabela de preços, que 
conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50

print('Loja Quase Doisa - Tabela de preços: ')
for i in range(1, 51):
    print(f'{i: <2} - R${1.99*i:.2f}')

'''

'''
30.O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar 
a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi 
contratado para desenvolver o programa que monta a tabela de preços de pães, 
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o 
exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00

preço_pao = abs(float(input('Preço do pão: R$ ')))
print('Panificadora Pão de Ontem - Tabela de preços: ')
for i in range(1, 51):
    print(f'{i: <2} - R${preço_pao*i:.2f}')

'''

'''
31.O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e 
agora possui uma loja de conveniências. Faça um programa que implemente uma 
caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser 
informado pelo operador para indicar o final da compra. O programa deve então 
mostrar o total da compra e perguntar o valor em dinheiro que o cliente 
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o 
programa deverá voltar ao ponto inicial, para registrar a próxima compra. A 
saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 8.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...

while True:
    cont_produto = 1
    total = 0
    while True:
        preco_produto = input(f'Produto {cont_produto}: R$ ') or '...'
        if preco_produto == '...':
            break

        if not abs(float(preco_produto)):
            break

        cont_produto += 1
        total += abs(float(preco_produto))

    if preco_produto == '...':
        break
    print(f'Total = RS {total:.2f}')
    dinheiro = abs(float(input('Dinheiro: R$ ')))
    print(f'Troco: R$ {dinheiro-total :.2f}')

'''

'''
32.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo 
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120

num = abs(int(input("Farorial de: ")))
fat = num
print(f'{num}! = {num}', end='')
for i in range(num - 1, 0, -1):
    print(f".{i}", end='')
    fat *= i

print(f' = {fat}')

'''

'''
33.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
programa que leia as um conjunto indeterminado de temperaturas, e informe ao 
final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.

maior = 0
menor = 1000
media_temp = 0
cont = 0
while True:
    temperatura = float(input('Temperatura em celcius -273,15 e 100: '))
    if -273.15 > temperatura or temperatura > 100:
        break

    if maior < temperatura:
        maior = temperatura

    if menor > temperatura:
        menor = temperatura

    media_temp += temperatura
    cont += 1

print(f'{maior=}\n{menor=}\nmedia={media_temp/cont}')

'''

'''
34.Os números primos possuem várias aplicações dentro da Computação, por exemplo
na Criptografia. Um número primo é aquele que é divisível apenas por um e por 
ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou 
não um número primo.

num = abs(int(input('Entre com um numero primo: ')))
for i in range(2, num+1):
    if not num % i:
        break

if num == i:
    print('É primo.')
else:
    print('Não é primo')
    
'''

'''
35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma 
lista dos números primos existentes entre 1 e um número inteiro informado 
pelo usuário.

n = abs(int(input('Entre com um n-ésimo: ')))
for k in range(1, n+1):
    num = k
    if k != 1:
        for i in range(2, num+1):
            if not num % i:
                break
    else:
        i =1
        
    if num == i:
        print(k,'É primo.')
    else:
        print(k,'Não é primo')
        
'''

'''
36.Desenvolva um programa que faça a tabuada de um número qualquer inteiro que 
será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 
e terminar em 10, o valor inicial e final devem ser informados também pelo 
usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35


tabuada = int(input('Montar a tabuada de: '))
lim_inf = int(input('Começar por: '))
lim_sup = int(input('Terminar em: '))
if lim_inf < lim_sup:
    print(f'Vou montar a tabuada de {tabuada} começando em {lim_inf} '
        f'e terminando em {lim_sup} :')
    for i in range(lim_inf, lim_sup+1):
        print(f'{tabuada} X {i} = {tabuada*i}')
else:
    print('Começo é maior que final.')
'''

'''
37.Uma academia deseja fazer um senso entre seus clientes para descobrir o mais 
alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um 
programa que pergunte a cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar
0 (zero) no campo código. Ao encerrar o programa também deve ser informados os 
códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais 
magro, além da média das alturas e dos pesos dos clientes

cod_mais_gordo = 0
cod_mais_alto = 0
cod_mais_magro = 0
cod_mais_baixo = 0
mais_gordo = 0
mais_baixo = 2
mais_magro = 100
mais_alto = 0
while True:
    cod = abs(int(input('Entre com o Codigo do cliente: ')))
    if not cod:
        break

    altura = abs(float(input('Altura: ')))
    peso = abs(float(input('Peso:')))

    if mais_alto < altura:
        cod_mais_alto = cod
        mais_alto = altura

    if mais_baixo > altura:
        cod_mais_baixo = cod
        mais_baixo = altura

    if mais_gordo < peso:
        mais_gordo = peso
        cod_mais_gordo = cod

    if mais_magro > peso:
        mais_magro = peso
        cod_mais_magro = cod

print(f'{cod_mais_alto=} {mais_alto=}')
print(f'{cod_mais_baixo=} {mais_baixo=}')
print(f'{cod_mais_magro=} {mais_magro=}')
print(f'{cod_mais_gordo=} {mais_gordo=}')

'''

'''
38.Um funcionário de uma empresa recebe aumento salarial anualmente: 
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro 
do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir
isto, altere o programa permitindo que ousuário digite o salário inicial do 
funcionário.

salario_inicial = abs(float(input('Entre com o salário incial: ')))
salario = salario_inicial
for i in range(1, 2023-1995):
    salario += salario_inicial*(0.015*i)

print('Salario atual(1995~2022): ', salario)

'''

'''
39.Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura em 
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas.

num_aluno_alto = 0
num_aluno_baixo = 0
mais_alto = 0
mais_baixo = 2
for i in range(10):
    num_aluno = abs(int(input('Entre com o número do aluno: ')))
    altura = abs(float(input('Entre com a altura do aluno: ')))

    if altura > mais_alto:
        num_aluno_alto = num_aluno
        mais_alto = altura

    if altura < mais_baixo:
        num_aluno_baixo = num_aluno
        mais_baixo = altura

print(f'{num_aluno_alto=} {mais_alto=}')
print(f'{num_aluno_baixo=} {mais_baixo=}')

'''

'''
40.Foi feita uma estatística em cinco cidades brasileiras para coletar dados
sobre acidentes de trânsito. Foram obtidos os seguintes dados:
1.Código da cidade;
2.Número de veículos de passeio (em 1999);
3.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
4.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
5.Qual a média de veículos nas cinco cidades juntas;
6.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

maiorIDA = 0
cod_maiorIDA = 0
menorIDA = 0
cod_menorIDA = 0
cont_menor_2k = 0
med_acidentes = 0
soma = 0
for i in range(5):
    cod = abs(int(input('Codigo da cidade: ')))
    num_veiculos = abs(int(input('Veiculos de passeio: ')))
    num_acidente = abs(int(input('Num de acidentes c/vitimas: ')))

    if not i:
        mairIDA = menorIDA = num_acidente
        cod_maiorIDA = cod_menorIDA = cod

    if maiorIDA < num_acidente:
        maiorIDA = num_acidente
        cod_maiorIDA = cod

    if menorIDA > num_acidente:
        menorIDA = num_acidente
        cod_menorIDA = num_acidente

    soma += num_veiculos

    if num_veiculos <= 2000:
        cont_menor_2k += 1
        med_acidentes += num_acidente

print(f'{cod_maiorIDA=} {maiorIDA=}')
print(f'{cod_menorIDA=} {menorIDA=}')
print(f'Media de acidentes cidade menor 2k {med_acidentes/cont_menor_2k}.')
print(f'Media de veiculos nas cidades {soma/5}.')

'''

'''
41.Faça um programa que receba o valor de uma dívida e mostre uma tabela com os 
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e 
valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25
Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67

valor_da_divida = abs(float(input('Entre com o valor da dívida: ')))
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
print(f'R${valor_da_divida:.2f}     0       1                        R${valor_da_divida:.2f}')
for i in range(1, 5):
    print(f'R${valor_da_divida*(1.05 + 0.05*i):.2f}     R${valor_da_divida*(0.05 + 0.05*i):.2f}'
          f'       {3*i}        '
          f'                R${valor_da_divida*(1.05 + 0.05*i)/(3*i):.2f}')

'''

'''
42.Faça um programa que leia uma quantidade indeterminada de números positivos 
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
[76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

inter_0_25 = 0
inter_26_50 = 0
inter_51_75 = 0
inter_76_100 = 0

while True:
    num = int(input('Entre com valores: '))
    if num < 0:
        break

    if num <= 25:
        inter_0_25 += 1
        
    if 26 <= num <= 50:
        inter_26_50 += 1
        
    if 51 <= num <= 75:
        inter_51_75 += 1
    
    if 76 <= num <= 100:
        inter_76_100 += 1
        
print(f'{inter_0_25=}')
print(f'{inter_26_50=}')
print(f'{inter_51_75=}')
print(f'{inter_76_100=}')

'''

'''
43.
O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total 
geral do pedido. Considere que o cliente deve informar quando o pedido deve 
ser encerrado.

print('Especificação   Código  Preço',
      'Cachorro Quente 100     R$ 1,20',
      'Bauru Simples   101     R$ 1,30',
      'Bauru com ovo   102     R$ 1,50',
      'Hambúrguer      103     R$ 1,20',
      'Cheeseburguer   104     R$ 1,30',
      'Refrigerante    105     R$ 1,00', sep='\n')
valor_total = 0
while True:
    cod = abs(int(input('Entre com o codigo do pedido ou 0 para sair: ')))
    if not cod:
        break
    
    quantidade = abs(int(input('Quantidade: ')))
    match cod:
        case 100: valor_total += 1.20*quantidade        
        case 101: valor_total += 1.30*quantidade        
        case 102: valor_total += 1.50*quantidade        
        case 103: valor_total += 1.20*quantidade        
        case 104: valor_total += 1.30*quantidade        
        case 105: valor_total += 1.00*quantidade        
        case _:print('Codigo erro.')
    
print(f'valor total: {valor_total}')

'''


'''
44.
Em uma eleição presidencial existem quatro candidatos. Os votos são informados 
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o 
conjunto de votos tem-se o valor zero.

print('1 - José',
      '2 - Mario',
      '3 - Luana',
      '4 - Maria',
      '5 - Voto Nulo',
      '6 - Voto Branco', sep='\n')
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0
while True:
    voto = abs(int(input('Entre com o numero do candidato: ')))
    match voto:
        case 0: break
        case 1: voto1 += 1
        case 2: voto2 += 1
        case 3: voto3 += 1
        case 4: voto4 += 1
        case 5: voto5 += 1
        case 6: voto6 += 1
        case _: continue

print(f'1 - José         {voto1=}',
      f'2 - Mario        {voto2=}',
      f'3 - Luana        {voto3=}',
      f'4 - Maria        {voto4=}',
      f'5 - Voto Nulo    {voto5=}',
      f'6 - Voto Branco  {voto6=}',
      f'Percentual de votos brancos'
      f' {(voto6/(voto1+voto2+voto3+voto4+voto5+voto6))*100:.2f}%',
      f'Percentual de votos Nulos'
      f' {(voto5/(voto1+voto2+voto3+voto4+voto5+voto6))*100:.2f}%',
      sep='\n')

'''

'''
45.
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 
questões, o programa deve perguntar ao aluno a resposta de cada questão e ao 
final comparar com o gabarito da prova e assim calcular o total de acertos e a 
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema 
deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos 
os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o 
professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = ''
for i in range(10):
    questao = input(f'Entre com a resposta da questão {i+1}: ').upper()
    gabarito += questao
print(gabarito)

cont = 0
notas = 0
while True:
    acerto = 0
    for i in range(10):
        questao = input(f'Entre com a resposta de questão {i+1}: ').upper()
        if questao == gabarito[i]:
            print('acerto')
            acerto += 1

    print('nota', acerto)
    cont += 1

    if cont == 1:
        maior_acerto = acerto
        menor_acerto = acerto
        notas += acerto
        continue

    if maior_acerto < acerto:
        maior_acerto = acerto

    if menor_acerto > acerto:
        menor_acerto = acerto

    notas += acerto

    mais = input('S para sair. ').upper() or 'N'
    if mais == 'S':
        break

print(f'Maior acerto foi {maior_acerto}\n'
      f'Menor acerto foi {menor_acerto}\n'
      f'Media das notas foi {notas/cont}\n'
      f'Total de alunos foi {cont}')
      
'''

'''
46.
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são 
eliminados. O seu resultado fica sendo a média dos três valores restantes. Você
deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe a média dos saltos conforme a descrição 
acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na 
ordem da execução, portanto não são ordenados. O programa deve ser encerrado 
quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m

dados = {}  # dicionarios de python achei melhor que lista salvo atleta/media
while True:
    atleta = input('Entre com o nome do atleta: ').capitalize()

    if not atleta:
        break
    soma = 0
    for i in range(5):
        salto = abs(float(input(f'{i+1} salto:')))
        if not i:
            melhor = salto
            pior = salto
            soma += salto
            continue

        if salto > melhor:
            melhor = salto

        if salto < pior:
            pior = salto

        soma += salto

    print(f'Melhor Salto {melhor}\n'
          f'Pior salto {pior}\n'
          f'Média {(soma-(melhor+pior))/3:.2f}')
    dados[atleta] = (soma-(melhor+pior))/3

print('Resultado final:\n',dados)

'''

'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A 
melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos 
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a 
sua média, conforme a descrição acima informada (retirar o melhor e o pior salto
e depois calcular a média com as notas restantes). As notas não são informados 
ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

atleta = input('Entre com o nome do atleta: ').capitalize()

for i in range(7):
    nota = abs(float(input('Nota: ')))

    if not i:
        maior = nota
        menor = nota
        soma = nota
        continue

    soma += nota

    if nota < menor:
        menor = nota

    if nota > maior:
        maior = nota

print('Resultado final:\n'
      f'Atleta: {atleta}\n'
      f'Melhor nota: {maior}\n'
      f'Pior nota: {menor}\n'
      f'Média: {(soma-(maior+menor))/5:.2f}')
      
'''

'''
48.
Faça um programa que peça um numero inteiro positivo e em seguida mostre 
este numero invertido.
Exemplo:
  12376489
  => 98467321

num = input('Entre com um numero inteiro: ')

if num.isdigit():
    print(num[::-1])
else:
    print('Não é digito.')

'''

'''
49.
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.

a = 1
b = 1
soma = 0
n = abs(int(input('Entre com o n-esimo termo: ')))
for i in range(n):
    print(f'{a}/{b} + ', end=' ')
    soma += a/b
    a += 1
    b += 2

print(f'\n {soma:.2f}')

'''

'''
50.
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o 
valor de H com N termos.
n = abs(int(input('Entre com o n-esimo termo: ')))
h = 0
for i in range(1, n+1):
    h += 1/n

print(h)
'''

'''
51.
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série

m = 1
soma = 0
n = abs(int(input('Entre com o n-esimo termo: ')))
for i in range(1, n+1):
    soma += i/m
    m += 2

print(f'\n {soma:.2f}')
'''
