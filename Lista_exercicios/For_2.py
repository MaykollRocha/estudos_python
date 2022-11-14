'''
1. Imprima todos os números de 1 a 100
for i in range(1, 101, 1):
    print(i)

'''

'''
2. Imprima todos os números de 100 a 1.

for i in range(100, 0, -1):
    print(i)

'''

'''
3. Imprima todos os múltiplos de 5 no intervalo de 1 a 500



'''

'''
4. Apresente como resultado a soma dos cem primeiros números naturais.

soma = 0
for i in range(1, 101):
    soma += i
print(soma)

'''

'''
5. Apresente os quadrados dos números inteiros existentes na faixa de valores
de 15 a 200.
# caso ela queria os numeros que são quadrados perfeitos como pensei:
for i in range(15, 200):
    if i**(1/2) == int(i**(1/2)):
        print(i)

#caso ela queria todos os quadrados desses números:

for i in range(15, 201):
    print(f'{i}² = {i*i} ')
'''

'''
6. Apresente todos os valores numéricos inteiros ímpares situados na
faixa de 0 a 20.

for i in range(21):
    if i % 2:
        print(i)

'''

'''
7. Apresente todos os números pares no intervalo de 600 a 1.

for i in range(600, 0, -1):
    if not i % 2:
        print(i)

'''

'''
8. Apresente o somatório dos valores pares existentes na faixa de 1 a 500

soma = 0
for i in range(1, 501):
    if not i % 2:
        soma += i

print(soma)

'''

'''
9. Apresente todos os valores numéricos divisíveis por 4 e menores que 200.

for i in range(1, 201):
    if not i % 4:
        print(i)

'''

'''
10. Calcule e mostre a média aritmética dos números entre 13 e 73.

media_aritmetica = 0
cont = 0
for i in range(13, 74):
    media_aritmetica += i
    cont += 1
print(media_aritmetica/cont)

'''

'''
11. Leia 4 números e escreva o cubo e a raiz cúbica de cada número.

for i in range(4):
    n = int(input('Entre com um número: '))
    print(f'{n}³  = {n**2}\n³ \|{n} = {n**(1/3)} ')

'''

'''
12. Leia 5 números e escreva o quadrado de cada número.

for i in range(5):
    n = int(input('Entre com um número: '))
    print(f'{n}² = {n**2}')

'''

'''
13. Leia 5 valores, um de cada vez, e conte quantos destes valores são
negativos, escrevendo esta informação.

cont = 0
for i in range(5):
    n = int(input('Entre com um número: '))
    if n < 0:
        cont += 1

print(f'Apareceram {cont} numeros negativos.')

'''

'''
14. Leia 5 números e escreva o maior e o menor.

maior = 0
menor = 1000
for i in range(5):
    n = int(input('Entre com um número: '))

    if maior < n:
        maior = n
    elif menor > n:
        menor = n

print(f'Maior:{maior} e Menor: {menor}')

'''

'''
15. Leia 10 números e escreva a metade de cada um deles.

for i in range(5):
    n = int(input('Entre com um número: '))
    print(f'{n}/2 = {n/2}')

'''

'''
16. Leia 15 números e escreva a raiz quadrada de cada número.

for i in range(15):
    n = int(input('Entre com um número: '))
    print(f'raiz({n}) = {n**(1/2)}')

'''

'''
17. Receba 20 números e imprima a soma dos números cujos quadrados são menores
do que 225.

soma = 0
for i in range(20):
    n = int(input('Entre com um número: '))
    if n**2 < 225:
        soma += n

print(soma)

'''

'''
18. Leia o nome, a idade e o sexo de 20 pessoas. Escreva o nome se a pessoa for
do sexo masculino e tiver mais de 21 anos.

aux_homens_21 = ''
for i in range(20):
    nome = input('Entre com um nome: ').capitalize()
    idade = abs(int(input('Entre com a idade: ')))
    sexo = input('M para masculino e F para feminino: ').upper()

    if sexo in 'MN' and idade > 21:
        aux_homens_21 += f'{nome} -'

print(aux_homens_21)

'''

'''
19. Leia um número n e imprima a soma dos números múltiplos de 5 no intervalo
entre 1 e n. Suponha que n será maior que zero.

n = abs(int(input('Entre com um número: ')))
soma = 0
for i in range(1, n+1):
    if not i % 5:
        soma += i

print(soma)

'''

'''
20. Leia o limite superior de um intervalo e o incremento. Imprimir todos os
números naturais no intervalo de 0 até esse número. Suponha que os dois números
lidos são maiores do que 0. Exemplo:
Limite superior: 20
Incremento:      5
Saída:           0 5 10 15 20


lim_sup = abs(int(input('Entre com o limite superior: ')))
incremento = abs(int(input('Entre com o incremento: ')))
print('Saida: ', end=' ')
for i in range(lim_sup+1):
    if not i % incremento:
        print(i, end=' ')

'''

'''
21. Leia os limites inferior e superior de um intervalo e escreva todos os
números múltiplos de 6 no intervalo fechado. Suponha que os dados digitados
são para um intervalo crescente. Exemplo:
Limite inferior: 5
Limite superior: 13
Saída: 6 12

lim_inf = abs(int(input('Entre com o limite inferior: ')))
lim_sup = abs(int(input('Entre com o limite superior: ')))
print('Saida: ', end=' ')
for i in range(lim_inf, lim_sup+1):
    if not i % 6:
        print(i, end=' ')

'''

'''
22. Leia um número inteiro n da entrada. Em seguida, ler n números da entrada e
imprimir o triplo de cada um.

n_entrada = abs(int(input('Entre com o número de entradas: ')))
for i in range(n_entrada):
    n = float(input('Entre com o número: '))
    print(f'{n:.3f}*3 = {n*3:.3f}')
'''

'''
23. Leia um número inteiro n da entrada. Em seguida, ler n números da entrada
e imprimir o maior deles.

n_entrada = abs(int(input('Entre com o número de entradas: ')))
maior = 0
menor = 10000
for i in range(n_entrada):
    n = float(input('Entre com o número: '))

    if maior < n:
        maior = n
    elif menor > n:
        menor = n

print(f'Maior: {maior:.2f} Menor: {menor:.2f}')

'''

'''
24. Dado o sexo e altura de 5 pessoas, calcular e exibir a maior altura, a média
das alturas femininas, o total de homens.

med_alt = 0
cont_m = 0
for i in range(5):
    sexo = input('Entre com M para masculino e F para feminino: ').upper()
    altura = float(input('Entre com a altura: '))
    if sexo == 'F':
        med_alt += altura

    if sexo == 'M':
        cont_m += 1

print(f'A media de altura feminina é {med_alt/(5-cont_m):.3f}'
      f'O total de homens foi {cont_m}')

'''

'''
25. Sabendo que a Unidade Aritmética e Lógica calcula o produto através de somas
sucessivas, calcule o produto de dois números inteiros lidos. Suponha que os
números lidos sejam positivos e que o multiplicando seja menor do que o
multiplicador.

num_1 = abs(int(input('Entre com um número: ')))
num_2 = abs(int(input('Entre com um outro número: ')))
prod = 0
for i in range(num_2):
    prod += num_1
print(f'{num_1}*{num_2} = {prod}')

'''

'''
26. Imprima os 10 primeiros termos da série de Fibonacci. Os dois primeiros
termos da série são 1 e 1 e cada termo seguinte é gerado a partir da soma dos
dois anteriores.
Exemplo: o terceiro termo é 2 (1 +1) e o quarto é 3 (1 +2).



'''

'''
27. A série de Ricc difere da série de Fibonacci porque os dois primeiros termos
são fornecidos pelo usuário. Os demais termos são gerados da mesma forma que a
série de Fibonacci. Imprima os n primeiros termos da série de Ricci e a soma dos
termos impressos, sabendo-se que para imprimir essa série são necessários pelos
menos três termos.

fn = abs(int(input('Entre com o primeiro termo: ')))
fn2 = abs(int(input('Entre com o segundo termo: ')))
n = abs(int(input('Entre com o numero de termos a procurar: ')))
for i in range(3, n+1):
    print(f'O termo {i} é {fn2+fn}')
    aux = fn2
    fn2 += fn
    fn = aux

'''

'''
28. A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos
são fornecidos e a partir daí os termos são gerados com a soma ou subtração dos
dois termos anteriores, ou seja:
 Ai = Ai-1 + Ai-2 para i impar
 Ai = Ai-1 - Ai-2 para i par
Imprima os 10 primeiros termos da série de Fetuccine

fn = abs(int(input('Entre com o primeiro termo: ')))
fn2 = abs(int(input('Entre com o segundo termo: ')))
for i in range(3, 11):
    aux = fn2
    if not i % 2:
        print(f'O termo {i} é {fn2-fn}')
        fn2 -= fn
    else:
        print(f'O termo {i} é {fn2+fn}')
        fn2 += fn
    fn = aux

'''

'''
29. Imprima todos os números inteiros positivos no intervalo aberto entre 10 e
100 de modo que:
     não terminem em zero
     se o dígito da direita for removido, o número restante é divisor do número
    original.
Exemplo:
26: 2 é divisor de 26
88: 8 é divisor de 88

for i in range(10, 101):
    if i % 10:
        if not i % int(i/10):
            print(i)

'''

'''
30. Criar um algoritmo/programa em C que deixe o usuário escolher qual a tabuada
de multiplicar que se deseja imprimir
n = abs(int(input('Entre com o numer da tabuada: ')))

for i in range(1, 11):
    print(f'{n}*{i}={n*i}')
'''

'''
31. Imprimir as tabuadas de multiplicar de 1 até 10
for i in range(1, 11):
    for n in range(1, 11):
        print(f'{i}*{n}={n*i}')
    print('-'*10)

'''

'''
32.
Uma empresa está fazendo a estatística de seus funcionários, ela precisa saber
quantas funcionárias têm com mais de 40 anos para encaminhá-las para exames de
mamografia. Fazer um programa que leia o nome, a idade e o sexo de seus 100
funcionários e imprima o nome se for do sexo feminino e tiver mais de 40 anos.
No final apresente o total de mulheres com mais de 40 anos.

garda_nome = ''
for i in range(100):
    nome = input('Entre com o nome: ').capitalize()
    idade = abs(int(input('Entre com a idade:')))
    sexo = input('M para macho e F para Deusa: ').upper()

    if sexo == 'F' and idade > 40:
        garda_nome += f'{nome} \n'

print('-'*20, 'Lista das deusas', garda_nome, sep='\n')

'''

'''
33.
Faça um programa que mostre a tabuada de multiplicação (de 1 a 10) para os 6
primeiros números primos. Ao mudar de uma base para outra o programa deve
mostrar uma mensagem ao usuário e aguardar que alguma tecla seja pressionada
para então montar a tabuada para a próxima base.

aux = 1
cont = 0
for i in range(1, 100+1):
    for p in range(1, i+1):
        if not i % p and p != 1:
            aux = p
            break

    if aux == i:
        for p in range(1, 11):
            print(f'{i}*{p}={p*i}')
        print("-"*10)
        cont += 1

    if cont == 6:
        break

'''

'''
34. Leia um valor N dado pelo usuário e apresente o valor calculado de H:
H = 1 + 2 + 3 + 4 + ... + N

n = abs(int(input('Entre com um valor: ')))
soma = 0
for i in range(1, n+1):
    soma += i
print(soma)
'''

'''
35. Calcule o peso total que será carregado por um caminhão. O seu programa deve
perguntar ao usuário quantas caixas devem ser transportadas e depois perguntar o
peso de cada caixa para saber qual o peso total a ser transportado.

num_caixa = abs(int(input('Entre com quantas caixas vai se transportadas: ')))
soma = 0
for i in range(1, num_caixa+1):
    peso = abs(float(input(f'Entre com o peso da caisa {i}: ')))
    soma += peso
print('Peso total de: ', soma, 'Kg')

'''

'''
36. Uma empresa compra diversos produtos toda semana. Construa um programa em C
solicite quantos tipos de produtos devem ser adquiridos. Depois, para cada produto,
leia a quantidade (Q) a ser comprada dele e o preço (PR) a ser pago por cada unidade.
Ao final, apresente o total gasto em reais pela empresa.

soma = 0
quant_tipo_prod = abs(int(input('Entre com a quantidade de produtos: ')))
for i in range(1, quant_tipo_prod+1):
    q = abs(int(input(f'Entre com a quantidade desse produto {i}: ')))
    pr = abs(float(input('Quanto por cada unidade foi pago: ')))
    soma += q*pr

print(f'O total gasto foi de R${soma :.2f}.')
'''

'''
37. Escreva um programa em C que receba dez números do usuário e imprima o cubo de
cada número.

for i in range(10):
    num = float(input('Entre com o valor que eu tiro o cubo:'))
    print(f'{num:.3f}³ = {num**2:.3f}')


'''

'''
38. Imprima todos os números pares de 1 até 100 e apresente ao final a soma dos
quadrados desses números pares.
Os números pares são: 2 4 6 8 ... 100
Total da soma dos quadrados: 171700

soma = 0
for i in range(1,101):
    if not i % 2:
        print(i, end=' ')
        soma += i**2
print('\n',soma)
'''

'''
39. Imprima todos os números de 1 até 200 e apresente ao final a soma da metade
desses números

soma = 0
for i in range(1, 201):
    print(i)
    soma += i
print(soma/2)

'''

'''
40. Leia um número inteiro (num) e calcule a soma dos quadrados dos pares
dos números no intervalo de 1 até ele (num).
num = abs(int(input('Entre com o num: ')))
soma = 0
for i in range(1, num + 1):
    if not i%2:
        soma += i**2
print(soma)

'''


'''
41. Solicite ao usuário quantos números inteiros ele quer dar como entrada
(suponha “x” números). Em seguida leia os “x” números e ao término da leitura
imprima quantos são pares e quantos são ímpares.

x = abs(int(input('Entre com quantos números vai entrar: ')))
par = 0
impar = 0
for i in range(x):
    num = float(input('Entre com o número: '))
    if not num % 2:
        par += 1
    else:
        impar += 1

print(f'Fora digitados {par} numros par e {impar} numeros impar.')

'''

'''
42. Desenvolver um programa em C que leia a altura e o sexo (M ou F) de “x”
pessoas. Este programa deverá calcular e mostrar:
a. A menor altura do grupo;
b. A média de altura das mulheres;
c. O número de homens;
d. O sexo da pessoa mais alta.
w
x = abs(int(input('Entre com o numero de pessoas a analisar: ')))
baixa = 10
media_altF = 0
num_boy = 0
alto = 0
sexo_alto = ''
for i in range(x):
    sexo = input('M ou F: ').upper()
    altura = abs(float(input('Entre com a altura: ')))

    if baixa > altura:
        baixa = altura

    if sexo == 'F':
        media_altF += altura

    if sexo == 'M':
        num_boy += 1

    if alto < altura:
        alto = altura
        match sexo:
            case 'F': sexo_alto = 'Feminino'
            case 'M': sexo_alto = 'Masculino'

print(f'a.{baixa}\nb.{media_altF/(x-num_boy)}\nc.{num_boy}\nd.{sexo_alto}')

'''

'''
43. A prefeitura de uma cidade fez uma pesquisa entre seus x habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
a) média do salário da população;
b) média do número de filhos
c) maior salário;
d) percentual de pessoas com salário até R$250,00.

x = abs(int(input('Entre com o número de habitantes: ')))
pessoa_com250 = 0
media_filho = 0
media_salario = 0
maior_salario = 0
for i in range(x):
    salario = abs(float(input('Entre com o slario: ')))
    filhos = abs(int(input('Entre com o número de filhos: ')))

    media_salario += salario
    media_filho += filhos

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 250:
        pessoa_com250 += 1

print(f'a.R${media_salario/x:.2f}\nb.{media_filho/x}\n'
      f'c.R${maior_salario:.2f}\nd.{(pessoa_com250/x)*100:.2f}%')

'''

'''
44. Em uma eleição presidencial, existem quatro candidatos. Os votos são
informados através de código. Os códigos utilizados são:
1,2,3,4 votos para os respectivos candidatos;
5 voto nulo;
6 voto em branco.
Calcule e imprima:
• total de votos para cada candidato;
• total de votos nulos;
• total de votos em branco;
• porcentagem de votos nulos sobre o total de votos;
• porcentagem de votos em branco sobre o total de votos.
Imagine que o programa irá calcular os votos de uma seção com 100 eleitores.

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0
for i in range(100):
    num = abs(int(input('Entre com um número entre 1-6: ')))

    match num:
        case 1: voto1 += 1
        case 2: voto2 += 1
        case 3: voto3 += 1
        case 4: voto4 += 1
        case 5: voto5 += 1
        case 6: voto6 += 1
        case _:
            print('Voto errado vai pro nulo')
            voto5 += 1

print(f'{voto1=}|{voto2=}|{voto3=}|{voto4=}|{voto5=}|{voto6=}\n'
      f'total de votos nulos {(voto5/100)*100:.2f}%\n'
      f'total de votos brancos {(voto6/100)*100:.2f}%')

'''

'''
45. Construa um programa em C que leia a quantidade de dias trabalhados por um
funcionário e o número de horas trabalhadas em cada dia (NH) e mostre como
resultado o total de horas trabalhadas pelo funcionário.

dias = abs(int(input('Entre com o números de dias que trabalho: ')))
total_horas = 0
for i in range(dias):
    nh = abs(int(input(f'Quanta horas trabalho no dia {i+1}: ')))
    total_horas += nh

print(f'{total_horas=}')

'''

'''
46. Leia do usuário um número inteiro >= 0 e escreva o fatorial desse número
(N!). Sabe-se que: N! = 1 x 2 x 3 x 4 x .... x N e que 0! = 1
(fatorial do número zero é igual a 1 por definição)

num = abs(int(input('Entre com o N que vamos tirar o fatorial: ')))

if num != 0:
    prod = 1
    for i in range(1, num+1):
        prod *= i
    print(f'{num}! = {prod}')
else:
    print(f'0! = 1\n(por definição)')

'''

'''
47. Foi realizada uma pesquisa para saber qual a avaliação que os alunos têm
sobre o funcionamento da biblioteca da universidade. Cada aluno respondeu com a
sua idade e a opinião sobre a biblioteca: excelente – 4, bom – 3, regular – 2,
ruim – 1. Leia do usuário quantos alunos vão participar da pesquisa. Em seguida
calcule os seguintes valores:
a) A média das idades das pessoas que responderam excelente;
b) A quantidade de pessoas que responderam ruim;
c) A porcentagem de pessoas que responderam “bom” ou “regular” entre todos os
questionários.

num_alunos = abs(int(input('Entre quantos alunos seram analisados: ')))
media_idade = 0
resposta_ruim = 0
resp_bom_regular = 0
for i in range(num_alunos):
    idade = abs(int(input('Entre com a idade: ')))
    nota = abs(int(input('Entre com a nota de 1-4 para a biblioteca: ')))

    media_idade += idade

    if nota == 1:
        resposta_ruim += 1

    if nota == 3 or nota == 2:
        resp_bom_regular += 1

print(f'a.{media_idade/num_alunos:.2f}\nb.{resposta_ruim=}\n'
      f'c.{resp_bom_regular/num_alunos*100:.2f}%')

'''

'''
48. Construa um programa em C que calcule a área total de uma residência (sala,
cozinha, quartos, etc., sendo todos eles retangulares). O usuário deverá
informar quantos cômodos há na casa e depois entrar com a largura e o
comprimento de cada cômodo.

num_comodos = abs(int(input('Entre com o numero de comodos: ')))
area_total = 0
for i in range(1, num_comodos+1):
    largura = abs(float(input(f'Entre com a largura do comodo {i}: ')))
    comprimento = abs(float(input(f'Entre com a comprimento do comodo {i}: ')))

    area_total += largura*comprimento

print(f'{area_total=}')
'''

'''
49. Leia um valor N inteiro e positivo e calcule e escreva o valor de E.
 E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!

nf = abs(int(input('Entre até que termo termos a soma: ')))
soma = 0
for n in range(nf+1):
    fat = 1
    for i in range(1, n+1):
        fat *= i

    if n == 0:
        fat = 1

    soma += 1/fat

print(soma)

'''

'''
50. Leia 50 valores e encontre o maior e o menor deles. Mostre o resultado

maior = 0
menor = 1000

for i in range(50):
    num = float(input('Entre com um valor: '))
    if maior < num:
        maior = num

    if menor > num:
        menor = num

print(f'{maior=}\n{menor=}')

'''

'''
51. Leia um número n (número de termos de uma progressão aritmética), a1
(o primeiro termo da progressão) e r (a razão da progressão) e escreva os
n termos desta progressão, bem como a soma dos elementos
an = a1 + (n-1).r

a1 = int(input('Entre com o primeiro termo da progessção: '))
n = int(input('Entre até que termo vai a progessção: '))
r = int(input('Entre com a razão da progessção: '))
for i in range(1, n+1):
    print(f'a{i}= {a1 + (i-1)*r}')
'''

'''
52. Leia 20 valores para uma variável n e, para cada um deles, calcule a tabuada
de 1 até n. Mostre a tabuada na forma:
1 x n = n
2 x n = 2n
3 x n = 3n
.......
n x n = n2

n = abs(int(input('Entre com o N de nossos valcaculo: ')))

print('-'*10)
for i in range(1, n+1):
    print(f'{i}*{n} = {i*n}')
print('-'*10)


'''

'''
53. Leia um número n que indica quantos valores devem ser lidos a seguir. Para
cada número lido, mostre em uma linha o valor lido e o respectivo fatorial deste
valor
n = abs(int(input('Quantos numeros seram transcritos: ')))
for i in range(n):
    num = abs(int(input('Entre com o numero: ')))
    fat = 1
    for p in range(1, num+1):
        fat *= p
    print('Seu fatorial é ', fat)
'''

'''
54. Considerando o intervalo de números de 1000 a 1999, escreva aqueles que
divididos por 11 dão resto igual a 5
for i in range(1000, 2000):
    if i % 11 == 5:
        print(i)
'''

'''

55. Leia 500 valores inteiros e positivos e:
a) encontre o maior valor;
b) encontre o menor valor;
c) calcule a média dos números lidos

maior = 0
menor = 1000
media = 0
for i in range(500):
    num = abs(int(input('Entre com o numero inrteiro positivo: ')))

    media += num

    if maior < num:
        maior = num

    if menor > num:
        menor = num

print(f'{maior=} {menor=} {media/500:.3f}')

'''

'''
56. Leia um valor n inteiro e positivo e que calcula a seguinte soma:
S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Você deve escrever cada termo gerado e o valor final de S

n = abs(int(input('Entre até que termo sera digitado: ')))
soma = 0
for i in range(1, n+1):
    print(f'termo {i} é {1/i}')
    soma += 1/i

print(soma)
'''

'''
57. Leia 10 valores, um de cada vez, e conte quantos deles estão no intervalo
[10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

cont_conter = 0
for i in range(10):
    num = abs(int(input('Entre com um valor: ')))
    if 10 <= num <= 20:
        cont_conter += 1

print(f'No intervalos {cont_conter} e fora é {10 - cont_conter}')

'''

'''
58. Escrever um algoritmo que calcula e escreve o produto dos números primos
entre 92 e 1478.

aux = 0
for i in range(92, 1479):
    for p in range(2, i+1):
        if not i % p:
            aux = p
            break

    if i == aux:
        print(i)

'''

'''
9. Escreva um programa que imprima, para um determinado 1 < n < 40, o seguinte
desenho (para n = 5):
#
##
###
####
#####

tam = abs(int(input('Entre com 1~40: ')))

if 1 <= tam <= 40:
    for i in range(1, tam+1):
        print('#'*i)
else:
    print('ERRO')

'''

'''
60. Escreva um programa que imprima, para um determinado 1 < n < 40, o seguinte
desenho (para n = 7):
#
##
###
####
#####
######
#######

tam = abs(int(input('Entre com 1~40: ')))

if 1 <= tam <= 40:
    for i in range(1, tam+1):
        print(' '*(tam-i), '#'*i)
else:
    print('ERRO')

'''

'''
61. Desenvolva um programa que, dado um inteiro h > 5, imprime a árvore de Natal de
altura h, da forma (para h = 5):
            #
           ###
          #####
         #######
        #########
           |||


tam = abs(int(input('Entre com 1~5: ')))

if 1 <= tam <= 5:
    for i in range(tam):
        aux = '#'*(i*2+1)
        print(f' { aux: ^9} ')
    else:
        aux = '|'*3
    print(f'{aux: ^11}')
else:
    print('ERRO')


'''

'''
62. Leia o número de andares de um prédio. Para cada andar do prédio, leia o 
número de pessoas que entraram e saíram do elevador. Considere que o elevador 
está vazio e está subindo, os dados se referem a apenas uma "subida" do elevador
e que o número de pessoas dentro do elevador sempre será maior ou igual a 0. Se 
o número de pessoas, após a entrada e a saída for maior que 15, deve ser 
mostrado o aviso:"EXCESSO DE PASSAGEIROS. DEVEM SAIR X PESSOAS.", no qual X 
representa o número de pessoas que devem sair do elevador naquele instante, de 
modo que seja obedecido o limite de 15 passageiros. Após a entrada de pessoas
no último andar o programa deve mostrar quantas pessoas vão iniciar a
descida do elevador.


andares = abs(int(input('Entre com quantos andates tem o prédio: ')))
x = 0  # Pessoas no elevador
for i in range(andares+1):
    if 0 <= x < 15:
        entrada = abs(int(input(f'Entre com quantas pessaos no andar {i}: ')))
    else:
        print('Elevador lotado.')
        entrada = 0

    if x > 0:
        saida = abs(int(input('Entre quantas pessoas vai sair: ')))

    else:
        print('Elevador vazio.')
        saida = 0

    x += entrada
    x -= saida

print('-'*3, f'Elevador descendo pessoas nele {x}', '-'*3)
for i in range(andares+1, -1, -1):
    if 0 <= x < 15:
        entrada = abs(int(input(f'Entre com quantas pessaos no andar {i}: ')))
    else:
        print('Elevador lotado.')
        entrada = 0

    if x > 0:
        saida = abs(int(input('Entre quantas pessoas vai sair: ')))
    else:
        print('Elevador vazio.')
        saida = 0

    x += entrada
    x -= saida
'''

'''
63. Receba como entrada três números inteiros. Os dois primeiros números 
representam respectivamente o valor inicial e o valor final de um intervalo 
de números. Calcule todos os números inteiros divisíveis pelo terceiro número 
lido, compreendidos no intervalo especificado pelo usuário. Exemplo de saída:
Início do intervalo: 17 
Final do intervalo: 29 
Valor do divisor: 3
Números divisíveis por 3 no intervalo de 17 a 29 são: 18 21 24 27

incio = abs(int(input('Entre com o ínicio do intervalo: ')))
fim = abs(int(input('Entre com o fim do intervalo: ')))
div = abs(int(input('Entre com o divisor do intervalo: ')))
saida = ''
for i in range(incio, fim+1):
    if not i % div:
        saida += f'{i} '

print(
    f'Números divisíveis por {div} no intervalo de {incio} a {fim} são: ', saida)
'''
