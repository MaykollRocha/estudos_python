'''


'''
import random

'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro
e imprima até a n-ésima linha.


def ensimotemo(n):
    for i in range(1, n+1):
        print(f'{i: >3}'*i)


n = abs(int(input("Entre com o valor: ")))
ensimotemo(n)

'''

'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor
n inteiro imprima até a n-ésima linha.

def imprima(n):
    for i in range(1, n+1):
        print(i, end=' ')

    print()


n = abs(int(input("Entre com o valor: ")))
for p in range(1, n+1):
    imprima(p)

'''


'''
Faça um programa, com uma função que necessite de três argumentos, e que
forneça a soma desses três argumentos.

def resulado(x, y, z): return x+y+z

num = [random.randint(0, 10) for _ in range(3)]

print(resulado(*num))

'''

'''
Faça um programa, com uma função que necessite de um argumento. A função
retorna o valor de caractere 'P', se seu argumento for positivo, e 'N',
se seu argumento for zero ou negativo.

def negativo(num):
    if num <= 0:
        return f'N'
    else:
        return 'P'

print(negativo(random.randint(-100, 100)))

'''

'''
Faça um programa com uma função chamada somaImposto. A função possui dois
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas

def somaImposto(taxaImposto, custo):
    return custo + (custo*taxaImposto/100)


custo = abs(float(input('Entre com o custo do produto: ')))
taxaImposto = abs(float(input('Entre com a taxa do imposto: ')))
print(f'O produto apos os caluclos fica {somaImposto(taxaImposto,custo):.2f}')
'''

'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em
dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão
e uma para a saída. Registre a informação A.M./P.M. como um valor 'A' para A.M.
e 'P' para P.M. Assim, a função para efetuar as conversões terá um parâmetro
formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def converte_horas(horas, minutos):
    if horas - 12 > 0:
        horas -= 12
        periodo = 'P.M.'
    else:
        periodo = 'A.M.'

    return f'{horas}:{minutos} {periodo}'


while True:
    try:
        time = [abs(int(input('Entre com as horas: '))),
                abs(int(input('Entre com as minutos: ')))]
    except:
        print('Valor invalido.')
        continue

    if time[1] > 60 or time[0] > 24:
        print(converte_horas(*time))
    else:
        print('Minutos exedem o padrão')

'''

'''
Faça um programa que use a função valorPagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o
valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor
ao programa que a chamou. O programa deverá então exibir o valor a ser pago na
tela. Após a execução o programa deverá voltar a pedir outro valor de prestação
e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que
conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do
valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar
o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso.

def valorPagamento(valorPrestacao, dias=0):
    if not dias:
        return valorPrestacao
    else:
        return valorPrestacao + valorPrestacao*(0.03 + 0.001*dias)

num_prest = 0
valor_dia = 0
while True:
    try:
        sup = [
            abs(float(input('Entre com a Prestação: '))),
            abs(int(input('Dias de atrasos: ')))
        ]
    except:
        print('Erro.')
        continue

    if sup[0]:
        print('valor da prestação: ', valorPagamento(*sup))
        num_prest += 1
        valor_dia += valorPagamento(*sup)
    else:
        break

print(f'Foram {num_prest} prestações e o valor total {valor_dia:.2f}.')

'''

'''
Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado.

def contDigitos(num):
    cont = 0
    while num > 0:
        num //= 10
        cont += 1
    return cont


num = abs(int(input('Entre com um numero: ')))


print(f'É um numer de {contDigitos(num)} digitos')

'''

'''
Reverso do número. Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -> 721.

def contDigitos(num):
    cont = 0
    while num > 0:
        num //= 10
        cont += 1
    return cont


def reverso(num):
    tam = contDigitos(num)
    novo = num
    lista = []
    for i in range(tam-1, -1, -1):
        lista.append(num//(10**i))
        num -= num//(10**i)*(10**i)

    novo = 0
    for i, valor in enumerate(lista):
        novo += valor*(10**i)

    return novo


n = 127
print(f'{n}->{reverso(n)}')

'''

'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança
um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você
tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira
jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você
fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar
jogando os dados até tirar este número novamente. Você perde, no entanto, se
tirar um 7 antes de tirar este Ponto novamente.

def lançaDados():
    return random.randint(1, 6) + random.randint(1, 6)


ganhou_1 = set(7, 11)
perdeu_1 = set(2, 3, 12)

cont = 0
while True:
    resultado = lançaDados()
    print(f'Lance {cont + 1}º foi {resultado}. ')
    if cont == 0:
        if resultado in ganhou_1:
            print('Natural.')
            break
        elif resultado in perdeu_1:
            print("craps")
            break
        else:
            ponto = resultado
            print(f'A gora tem que tirar {ponto} e não pode tirar 7.')
            cont += 1
    else:
        if resultado == 7:
            print('Perdeu')
            break
        elif resultado == ponto:
            print('Ganhou')
            break
        else:
            cont += 1
            continue

'''

'''
Data com mês por extenso. Construa uma função que receba uma data no formato
DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def mes_string(mes):

    match int(mes):
        case 1: return "Janeiro"
        case 2: return 'Fevereiro'
        case 3: return 'Março'
        case 4: return 'Abril'
        case 5: return 'Maio'
        case 6: return 'Junho'
        case 7: return 'Julho'
        case 8: return 'Agosto'
        case 9: return 'Setembro'
        case 10: return 'Outubro'
        case 11: return 'Novembro'
        case 12: return 'Dezembro'


def bixesto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def validarData(dia, mes, ano):
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    print(dia, mes, ano)
    mes_31 = (1, 3, 5, 7, 8, 10, 12)

    if ano > 0 and dia != 0 and dia < 32 and mes < 13 and mes != 0:
        if mes in mes_31:
            return True
        else:
            if mes == 2:
                if dia <= 28:
                    return True
                elif dia == 29 and bixesto(ano):
                    return True
                else:
                    return False
            else:
                if dia <= 30:
                    return True
                else:
                    return False
    else:
        return False


data_string = '20/3/2004'
data = [*data_string.split('/')]
if validarData(*data):

    print(f'{data[0]} de {mes_string(data[1])} de {data[2]}')
else:
    print('Data invalida.')

'''

'''

Embaralha palavra. Construa uma função que receba uma string como parâmetro e
devolva outra string com os carateres embaralhados. Por exemplo: se função
receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra
combinação possível, de forma aleatória. Padronize em sua função que todos os
caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de
como foram digitados.

def embaralhar(txt):
    repo = ''
    for i in range(len(txt)):
        letra = txt[random.randint(0, (len(txt)-1))]
        while letra in repo:
            letra = txt[random.randint(0, (len(txt)-1))]
        else:
            repo += letra
    return repo


txt = input('Texto: ').lower()
print(embaralhar(txt))

'''

'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres '+' , '-' e '| '. Esta função deve receber dois parâmetros, linhas e
colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
máximo é 20. Se valores fora da faixa forem informados, eles devem ser
modificados para valores dentro da faixa de forma elegante.

+----------+
|          |
|          |
+----------+

def retangulo(linha, coluna):
    print('+', '-'*(linha), '+', sep='')
    for i in range(coluna):
        print('|', ' '*(linha), '|', sep='')
    print('+', '-'*(linha), '+', sep='')


linha = abs(int(input('Entre com a linha: ')))
coluna = abs(int(input('Entre com a coluna: ')))

if 1 <= linha <= 20 and 1 <= linha <= 20:
    retangulo(linha, coluna)
else:
    print('Esta fora dos valores permitidos.')

'''

'''

Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com
um número em cada posição e no qual a soma das linhas, colunas e diagonais é a
mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4  8 1 6
1  5  9  3 5 7
6  7  2  4 9 2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos
com as características acima. Dica: produza todas as combinações possíveis e
a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais
simples que usar uma matriz 3x3.



'''


def quadradro_impares(matrix, n):

    def trata_coluna(coluna, esp):
        if coluna == 0:
            coluna += (esp-1)
        else:
            coluna -= 1

        return coluna

    def trata_linha(linha, esp):
        if linha == 0:
            linha += (esp-1)
        else:
            linha -= 1

        return linha

    cubo = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                cubo[0][n//2] = matrix[i][j]
                antl = i
                antc = n//2
            else:
                l = trata_linha(antl, n)
                c = trata_linha(antc, n)
                if cubo[l][c] == 0:
                    cubo[l][c] = matrix[i][j]
                    antl = l
                    antc = c
                else:
                    antl += 1
                    if antl > n-1:
                        antl = 0
                    cubo[antl][antc] = matrix[i][j]

    return cubo


def quadrado_resto4(matrix, n):
    cubo = [[0 for j in range(n)] for i in range(n)]
    matrizB = [[matrix[i][j]
                for j in range(len(matrix)-1, -1, -1)] for i in range(len(matrix)-1, -1, -1)]

    for i in range(n):
        for j in range(n):
            if i == j or i+j == (n-1):
                cubo[i][j] = matrizB[i][j]
            else:
                cubo[i][j] = matrix[i][j]

    return cubo


n = 6

if n % 2:
    matrix = [[(i*n + j) + 1 for j in range(n)] for i in range(n)]
    cubo = quadradro_impares(matrix, n)
elif not n % 4:
    matrix = [[(i*n + j) + 1 for j in range(n)] for i in range(n)]
    cubo = quadrado_resto4(matrix, n)
else:
    print('Medodo Lux.')
    matrixaux = [i + 1 for i in range(n*n)]
    matrix = []
    cont = 1
    for i in range(0, n*n, n*2):
        ma = []
        for j in range(i, n*2*cont, 4):
            if j != 35:
                ma.append([[matrixaux[j], matrixaux[j+1]],
                           [matrixaux[j+2], matrixaux[j+3]]])
        matrix.append(ma.copy())
        cont += 1
    #
    #
    cubo = quadradro_impares(matrix, 3)
    new = []
    set = (4, 6, 8)
    for i in range(len(cubo)):
        for j in range(len(cubo[i])):
            print(j, i)
            if i == 2 and j == 2 or j == 0 and i == 2 or j == 1 and i == 1:
                new.append(
                    [[cubo[i][j][0][0], cubo[i][j][1][1]],
                     [cubo[i][j][0][1], cubo[i][j][1][0]]]
                )
            else:
                new.append(
                    [[cubo[i][j][1][1], cubo[i][j][0][0]],
                     [cubo[i][j][0][1], cubo[i][j][1][0]]]
                )

    for i in new:
        print(*i, sep='\n')
        # print(*cubo, sep='\n')
'''
def diagonal_soma(matrix, soma):
    soma_d = 0
    soma_di = 0
    for i in range(len(matrix)):
        soma_d += matrix[i][i]
        soma_di += matrix[-(i+1)][-(i+1)]

    if soma_d == soma_di == soma:
        return True
    else:
        return False


def coluna_soma(matrix, soma):
    matrizB = [[matrix[j][i]
                for j in range(len(matrix))] for i in range(len(matrix))]

    for i in matrizB:
        if sum(i) != soma:
            return False

    return True


def linhas_soma(matrix, soma):
    aux = 0
    for i in matrix:
        if sum(i) != soma:
            return False

    return True


while True:
    # matrix3x3 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    matrix3x3 = [[random.randint(1, 16) for i in range(4)]for i in range(4)]
    soma = sum(matrix3x3[0])
    if linhas_soma(matrix3x3, soma) and coluna_soma(matrix3x3, soma) and diagonal_soma(matrix3x3, soma):
        print(*matrix3x3, sep='\n')
        break

'''
