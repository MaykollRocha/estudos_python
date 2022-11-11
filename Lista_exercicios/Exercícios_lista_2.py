"""
Estrutura De Decisao
site:https://wiki.python.org.br/EstruturaDeDecisao
nome: Maykoll Rocha
 Todos os exercios feitos por mim baseado no conhecimento que tenho no dia
10 de novembro de 2022.
 Para ver como esta o exercicios so tirar o exercio que quer ver do Docstrings
o enucidos estão todos comentados.
 Alguns codigos foram digitados porem não foram testados caso de errado é pq
eles so estão escritos sem nem ter feito um teste antes bem passivo de erro.
 Durante o programa tentei nunca tratar entradas ou usar if/else/elif pois a
intenção é quem faz exercicio não saber como funciona essas coisa.
 Qualquer problema caso eu esteja vivo ainda algumas redes de contato minha:
instagram: @maykollr
email: <maykoll1412@gmail.com>
email: <rmaykoll_rocha@hotmail.com>
"""

"""
# 1.Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Entre com o número: "))
n2 = int(input("Entre com o número: "))

if n1>n2:
    print(f'O maior é {n1}')
else:
    prinf(f'O maior é {n2}')
"""

"""
# 2.Faça um Programa que peça um valor e mostre
# na tela se o valor é positivo ou negativo.

valor = float(input('Entre com um valor'))

if valor > 0: print("Valor positivo.")
elif valor < 0: print('Valor negativo.')
"""

"""
# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input('Entre com F para feminino e M para masculino: ')

if letra.capitalize() == 'F':
    print('Feminino')
elif letra.capitalize() == 'M':
    print('Masculino')
else:
    print('Sexo Inválido')
"""

"""
# 4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Entre com uma letra: ')
if len(letra)>1:
    if letra.catalize() in 'AEIOU':
        print('É uma vogal.')
    else:
        print('É uma consoante')
else:
    print("só uma letra não uma palavra.")
"""

'''
# 5.Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#       A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#       A mensagem "Reprovado", se a média for menor do que sete;
#       A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = abs(float(input('Entre com a 1 nota:')))
nota2 = abs(float(input('Entre com a 2 nota:')))

if 0<= nota1 <= 10 and 0<= nota2 <= 10:
    mf = (nota1 + nota2)/2
    if mf <= 7:
        print("Reprovou")
    elif mf == 10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print('Algum dos valores é invalido.')
'''

'''
# 6.Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Entre com um valor: '))
n2 = float(input('Entre com um valor: '))
n3 = float(input('Entre com um valor: '))

maior_n1 = n1 > n2 and n1 > n3
maior_n2 = n2 > n1 and n2 > n3
maior_n3 = n3 > n1 and n3 > n2

if maior_n1:
    print(f'O maior é {n1}.')

if maior_n2:
    print(f'O maior é {n2}.')

if maior_n3:
    print(f'O maior é {n3}.')
'''

'''
# 7.Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Entre com um valor: '))
n2 = float(input('Entre com um valor: '))
n3 = float(input('Entre com um valor: '))

maior_n1 = n1 > n2 and n1 > n3
maior_n2 = n2 > n1 and n2 > n3
maior_n3 = n3 > n1 and n3 > n2

menor_n1 = n1 < n2 and n1 < n3
menor_n2 = n2 < n1 and n2 < n3
menor_n3 = n3 < n1 and n3 < n2

if maior_n1:
    print(f'O maior é {n1}.')

if maior_n2:
    print(f'O maior é {n2}.')

if maior_n3:
    print(f'O maior é {n3}.')

if menor_n1:
    print(f'O menor é {n1}.')

if menor_n2:
    print(f'O menor é {n2}.')

if menor_n3:
    print(f'O menor é {n3}.')

'''

'''
# 8.Faça um programa que pergunte o preço de três produtos e informe
# qual produto você deve comprar, sabendo que a decisão é sempre pelo
# mais barato

prod1 = abs(float(input('Entre com o valor do produto: ')))
prod2 = abs(float(input('Entre com o valor do produto: ')))
prod3 = abs(float(input('Entre com o valor do produto: ')))

menor_prod1 = prod1 < prod2 and prod1 < prod3
menor_prod2 = prod2 < prod1 and prod2 < prod3
menor_prod3 = prod3 < prod1 and prod3 < prod2

if menor_prod1:
    print(f'Cpmpre o produto 1.')

if menor_prod2:
    print(f'Cpmpre o produto 2.')

if menor_prod3:
    print(f'Cpmpre o produto 3.')

'''

'''
# 9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Entre com um valor: '))
n2 = float(input('Entre com um valor: '))
n3 = float(input('Entre com um valor: '))

if n1 >= n2 >= n3:
    print(n1, n2, n3, sep='-')
elif n1 >= n3 >= n2:
    print(n1, n3, n2, sep='-')
elif n2 >= n1 >= n3:
    print(n2, n1, n3, sep='-')
elif n2 >= n3 >= n1:
    print(n2, n3, n1, sep='-')
elif n3 >= n2 >= n1:
    print(n3, n2, n1,sep='-')
else:
    print(n3, n1, n2,sep='-')

'''

'''
# 10.Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

letra = input('Dige M-matutino ou V-Vespertino ou N- Noturno: ')

if len(letra) == 1:
    if letra.capitalize() == 'M':
        print("Bom Dia!")
    elif letra.capitalize() == 'V':
        print("Boa Tarde!")
    elif letra.capitalize() == 'N':
        print("Boa Noite!")
    else:
        print("Valor Inválido!")
else:
    print('É so uma letra.')
'''


'''
# 11.As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará
# os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no salário atual:
#       salários até R$ 280,00 (incluindo) : aumento de 20%
#       salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#       salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#       salários de R$ 1500,00 em diante : aumento de 5% Após o aumento
# ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = abs(float(input('Entre com o valor do salrio: ')))

if salario < 280:
    print(f'Seu saliro era de {salario:.2f} e sera aplicado'
          f'20% de aumento no salario tendo um amento de {salario*0.2:.2f}'
          f'contabilizando ao todo {salario*1.2:.2f}')
elif 280 <= salario < 700:
    print(f'Seu saliro era de {salario:.2f} e sera aplicado'
          f'15% de aumento no salario tendo um amento de {salario*0.15:.2f}'
          f'contabilizando ao todo {salario*1.15:.2f}')
elif 700 <= salario < 1500:
    print(f'Seu saliro era de {salario:.2f} e sera aplicado'
          f'10% de aumento no salario tendo um amento de {salario*0.1:.2f}'
          f'contabilizando ao todo {salario*1.1:.2f}')
elif 1500 <= salario:
    print(f'Seu saliro era de {salario:.2f} e sera aplicado'
          f'5% de aumento no salario tendo um amento de {salario*0.05:.2f}'
          f'contabilizando ao todo {salario*1.05:.2f}')
'''

'''
# 12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que
# os descontos são do Imposto de Renda, que depende do salário bruto (conforme
# tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário
# Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
# pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no
# mês.
# Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações,dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

hora_trampo = abs(float(input('Entre com as Horas trabalhadas:')))
ganho_hora = abs(float(input('Ganho por hora: ')))
salario_bruto = hora_trampo*ganho_hora

ir = 0
aux = 0
if 900 < salario_bruto <= 1500:
    aux = 5
    ir += salario_bruto*0.05
elif 1500 < salario_bruto <= 2500:
    aux = 10
    ir += salario_bruto*0.1
elif 2500 <= salario_bruto:
    aux = 20
    ir += salario_bruto*0.2

inss = salario_bruto*0.10
fgts = salario_bruto*0.11
sindicato = salario_bruto*0.03
salrio_liquido = salario_bruto - (inss+ir+sindicato)

print(
    f'Salário Bruto:({hora_trampo}*{ganho_hora}) : R${salario_bruto:.2f}',
    f'(-) IR ( {aux}% )             : R${ir:.2f} ',
    f'(-) SINDICATO ( 3%)        : R${sindicato:.2f}',
    f'(-) INSS ( 10%)            : R${inss:.2f}',
    f'FGTS (11%)                 : R${fgts:.2f}',
    f'Total de descontos         : R${ir+sindicato+inss:.2f}',
    f'Salário Liquido            : R${salrio_liquido:.2f}',
    sep='\n')

'''

'''
# 13.Faça um Programa que leia um número e exiba o dia correspondente da
# semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
# valor inválido.

n = abs(int('Entre com um digito de 1-7 pro dia da semana'))

if n == 1:
    print('Domingo')
elif n == 2:
    print('Segunda-Feira')
elif n == 3:
    print('Terça-Feira')
elif n == 4:
    print('Quarta-Feira')
elif n == 5:
    print('Quinta-Feira')
elif n == 6:
    print('Sexta-Feira')
elif n == 4:
    print('Sábado')
else:
    print('Valor inválido.')

'''

'''
# 14.Faça um programa que lê as duas notas parciais obtidas por um aluno
# numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Média de Aproveitamento  Conceito
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
# ou “REPROVADO” se o conceito for D ou E.

n1 = abs(float(input('Entre com a nota da primeiro prova: ')))
n2 = abs(float(input('Entre com a nota da segunda prova: ')))
if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    mf = (n1+n2)/2
    if 10 <= mf:
        print(f'A sua nota é A e você foi Aprovado.')
    elif 7.5 < mf <= 9:
        print(f'A sua nota é B e você foi Aprovado.')
    elif 6 < mf <= 7.5:
        print(f'A sua nota é C e você foi Aprovado.')
    elif 4 < mf <= 6:
        print(f'A sua nota é D e você foi Reprovado.')
    else:
        print(f'A sua nota é E e você foi Reprovado.')
else:
    print("Algumas das notas se encontra fora de uma nota normal.")

'''

'''
# 15.Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois
# lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
lad1 = abs(float(input('Entre com um lado: ')))
lad2 = abs(float(input('Entre com outro lado: ')))
lad3 = abs(float(input('Entre com outro lado: ')))

e_triangulo = lad1**2 + lad2**2 >= lad3**2 and \
                lad1**2 + lad3**2 >= lad2**2 and \
                lad3**2 + lad2**2 >= lad1**2

if e_triangulo:
    if lad1==lad2==lad3:
        print("Triangulo equilatero.")
    elif lad1 == lad2 or lad2 == lad3 or lad3 == lad1:
        print("Triangulo Isoseles.")
    else:
        print('Triangulo Escaleno.')
else:
    print('Não é triangulo.')
'''

'''
# 16.Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
# fazer as consistências, informando ao usuário nas seguintes situações:
#   a.Se o usuário informar o valor de A igual a zero, a equação não
# é do segundo grau e o programa não deve fazer pedir os demais
# valores, sendo encerrado;
#   b.Se o delta calculado for negativo, a equação não possui
#       raizes reais. Informe ao usuário e encerre o programa;
#   c.Se o delta calculado for igual a zero a equação possui
#       apenas uma raiz real; informe-a ao usuário;
#   d.Se o delta for positivo, a equação possui duas raiz reais;
#   informe-as ao usuário;

print('ax²+bx+c')
a = int(input("Entre com o valor de a: "))
if not a == 0:
    b = int(input('Entre com o valor de b: '))
    c = int(input('Entre com o valor de c: '))
    delta = b**2 - 4*a*c
    if not delta < 0:
        if delta  == 0:
            print('A temos uma unica raiz real: {-b/2*a}')
        else:
            print('Temos 2 raizes reais:',
                  {(-b+((delta)**(1/2)))/(2*a)}, {(-b-((delta)**(1/2)))/(2*a)},)
    else:
        print("Não temos raizes reais.")
else:
    print("Você ira informar uma equação linear.")
'''

'''
# 17.Faça um Programa que peça um número correspondente
# a um determinado ano e em seguida informe se este ano é
# ou não bissexto.
ano = int(input('Entre com o ano: '))

if ano%4==0:
    if ano%100 == 0:
        if ano%400==0:
            bixesto = True
        else:
            bixesto = False
    else:
        bixesto = True
else:
    bixesto = False

if bixesto:
    print("É ano bissexto.")
else:
    print("Não é ano bissexto")
'''

'''
# 18.Faça um Programa que peça uma data no formato dd/mm/aaaa
# e determine se a mesma é uma data válida. (não tratei o ano bissexto
# codigo para implementação caso queira acima)

print('dd/mm/aaaa')
dia = abs(int(input("Entre com o dia: ")))
mes = abs(int(input("Entre com o mes: ")))
ano = abs(int(input("Entre com o ano: ")))

if ano < 10000 and 0 < mes < 13 and dia <= 31:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 \
            or mes == 10 or mes == 12:
        print("A data é valida.")
    else:
        if mes == 2:
            if dia <= 28:
                print("A data é valida.")
            else:
                print("Não é uma data valida")
        else:
            if dia <= 30:
                print("A data é valida.")
            else:
                print("Não é uma data valida")
else:
    print("Não é uma data valida")

'''

'''
# 19.Faça um Programa que leia um número inteiro menor que 1000 e
# imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre
outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311,
111, 25, 20, 10, 21, 11, 1, 7 e 16

num = abs(int(input("Entre com o número: ")))
d = 0
u = 0
c = 0
if num < 1000:
    u = num - ((num//10) * 10)
    if not num - u == 0:
        d = num//10 - ((num//100) * 10)
        if not num - (d*10+u) == 0:
            c = num//100

if d < 0:
    d = 0

if u < 0:
    u = 0


if c != 0:
    if c != 1:
        print(f'{c} centenas', end='')
    else:
        print(f'{c} centena', end='')

    if d == 0 and u == 0:
        print('.')
    elif d == 0 or u == 0:
        print(' e', end=' ')
    else:
        print(',', end=' ')

if d != 0:
    if d != 1:
        print(f'{d} dezenas', end='')
    else:
        print(f'{d} dezena', end='')

    if u == 0:
        print('.')
    elif d != 0:
        print(' e', end=' ')

if u != 0:
    if u != 1:
        print(f'{u} unidades.')
    else:
        print(f'{u} unidade')
'''

'''
# 20.Faça um Programa para leitura de três notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e presentar:
#       a.A mensagem "Aprovado", se a média for maior ou igual a 7, 
#       com a respectiva média alcançada;
#       b.A mensagem "Reprovado", se a média for menor do que 7,
#       com a respectiva média alcançada;
#       c.A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = abs(float("Entre com a nota: "))
n2 = abs(float("Entre com a nota: "))
n3 = abs(float("Entre com a nota: "))

if n1 < 10 and n2 < 10 and n3 < 10:
    mf = (n1+n2+n3)/3
    if mf == 10:
        print("Aprovado com Distinção.")
    elif mf >= 7:
        print("Aprovado.")
    else:
        print("Reprovado.")
else:
    print("Alguma das notas apresentadas não é valida.")
'''

'''
# 21.Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas 
# existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
# duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece 
# três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 
# 5 e quatro notas de 1.

valor = abs(int(input('Quanto será sacado: ')))
if valor != 0:
    notas_100 = valor//100
    if notas_100 != 0:
        print(f"{notas_100} notas de 100", end='')
    valor -= 100*notas_100
    if valor != 0:
        notas_50 = valor//50
        if notas_50 != 0:
            print(f", {notas_50} notas de 50", end='')
        valor -= 50*notas_50
        if valor != 0:
            notas_10 = valor//10
            if notas_10 != 0:
                print(f", {notas_10} notas de 10", end='')
            valor -= 10*notas_10
            if valor != 0:
                notas_5 = valor//5
                if notas_5 != 0:
                    print(f", {notas_5} notas de 5", end='')
                valor -= 5*notas_5
                if valor != 0:
                    notas_1 = valor
                    if notas_1 != 0:
                        print(f"e {notas_1} notas de 1", end='')

print(".")
'''

'''
# 22.Faça um Programa que peça um número inteiro e determine 
# se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input('Entre com um numero: '))

if not num%2:
    print('É um numero par. ')
else:
    print('É numero impar. ')
'''

'''
# 23.Faça um Programa que peça um número e informe se
# o número é inteiro ou decimal. Dica: utilize uma função 
# de arredondamento.

num = float(input('Entre com um número: '))

if num-int(num) == 0:
    print('É um numero inteiro.')
else:
    print('É um número decimal.')
    
'''

'''
# 24.Faça um Programa que leia 2 números e em seguida pergunte 
# ao usuário qual operação ele deseja realizar. O resultado da operação
# deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num1 = float(input('Entre com o numero: '))
num2 = float(input('Entre com o numero: '))
op = input("Qual operação + para soma * para multiplição"
           '- para subtração e / para divisão')

if op == '*':
    result = num1*num2
elif op == '-':
    result = num1-num2
elif op == '+':
    result = num1+num2
elif op == '/':
    result = num1/num2
else:
    result = None

if not result == None:
    if result >= 0:
        print("É positivo.")
    else:
        print('É negativo.')

    if not result % 2:
        print('É um par.')
    else:
        print('É um impar.')

    if result-int(result) == 0:
        print('É um numero inteiro.')
    else:
        print('É um número decimal.')
else:
    print("Não colocou uma operação valida.")

'''

'''
# 25.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
#   "Telefonou para a vítima?"
#   "Esteve no local do crime?"
#   "Mora perto da vítima?"
#   "Devia para a vítima?"
#   "Já trabalhou com a vítima?" 
#   O programa deve no final emitir uma 
#   classificação sobre a participação da pessoa no crime. Se a pessoa
#   responder positivamente a 2 questões ela deve ser classificada como
#   "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso 
#   contrário, ele será classificado como "Inocente".

print('Respondas as proximas 5 preguntas com S para sim e N para não.')
perg1 = input("Telefonou para a vítima?")
perg2 = input("Esteve no local do crime?")
perg3 = input("Mora perto da vítima?")
perg4 = input("Devia para a vítima?")
perg5 = input("Já trabalhou com a vítima?")
cont = 0
if perg1.capitalize() == 'S':
    cont += 1
if perg2.capitalize() == 'S':
    cont += 1
if perg3.capitalize() == 'S':
    cont += 1
if perg4.capitalize() == 'S':
    cont += 1
if perg5.capitalize() == 'S':
    cont += 1

if cont == 5:
    print('Assasino.')
elif 3 <= cont <= 4:
    print("Cúmplice.")
elif cont == 2:
    print('Suspeito.')
else:
    print("Inocente.")
    
'''

'''
# 26.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva
# um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma:
# A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro
# da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipo = input("Entre com o tipod de comnustivel G-Gasolina A-Alcool: ")
litro = abs(float(input('Entre com quantos litros vai colocar: ')))

if tipo.capitalize() == 'G':
    if litro <= 20:
        print("Total vai ficar", (litro*2.5)*0.96)
    else:
        print("Total vai ficar", (litro*2.5)*0.94)
elif tipo.capitalize() == 'A':
    if litro <= 20:
        print("Total vai ficar", (litro*1.9)*0.97)
    else:
        print("Total vai ficar", (litro*1.9)*0.95)
else:
    print("Não existe esse tipo.")


'''

'''
# 27.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                         Até 5 Kg           Acima de 5 Kg
#   Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#   Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor 
# total da compra ultrapassar R$ 25,00, receberá ainda um 
# desconto de 10% sobre este total. Escreva um algoritmo para
# ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
# adquiridas e escreva o valor a ser pago pelo cliente.

kgma = abs(float(input('Entre quanto de maça vai comprar: ')))
kgmo = abs(float(input('Entre quanto de morango vai comprar: ')))
pesot = kgma + kgmo
if kgma > 5:
    pma = kgma*1.50
else:
    pma = kgma*1.80
if kgmo > 5:
    pmo = kgmo*2.20
else:
    pmo = kgmo*2.50

pt = pma+pmo

if pt >= 25 or pesot >= 8:
    print(f'O proço total a ser pago é R${pt*0.9:.2f}')
else:
    print(f'O proço total a ser pago é R${pt:.2f}')
    
'''

'''
# 28.O Hipermercado Tabajara está com uma promoção de carnes
# que é imperdível. Confira:
#                             Até 5 Kg           Acima de 5 Kg
#       File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#       Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#       Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas
# um dos tipos de carne da promoção, porém não há limites para a 
# quantidade de carne por cliente. Se compra for feita no cartão 
# Tabajara o cliente receberá ainda um desconto de 5% sobre o total 
# da compra. Escreva um programa que peça o tipo e a quantidade de 
# carne comprada pelo usuário e gere um cupom fiscal, contendo as 
# informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar.

q_carne = input('Entre com qual carne A-Alcata F-File P-Picanha: ')
kg_carne = abs(float('Entre com quantos kg vai compra: '))

if kg_carne > 5:
    if q_carne.capitalize() == 'A': pt = q_carne*6.8 
    if q_carne.capitalize() == 'F': pt = q_carne*5.8 
    if q_carne.capitalize() == 'P': pt = q_carne*7.8 
else:
    if q_carne.capitalize() == 'A': pt = q_carne*5.9 
    if q_carne.capitalize() == 'F': pt = q_carne*4.9
    if q_carne.capitalize() == 'P': pt = q_carne*6.9 

cartao = abs(int(input('Se tiver cartão do mercado digite 1: ')))

if cartao == 1:
    if q_carne.capitalize() == 'A': 
        print(f'Alcatra {q_carne:.2f}kg R${pt*0.95:.2f} no cartão.')
    if q_carne.capitalize() == 'F': 
        print(f'File Duplo {q_carne:.2f}kg R${pt*0.95:.2f} no cartão.')
    if q_carne.capitalize() == 'P':
        print(f'Picanha {q_carne:.2f}kg R${pt*0.95:.2f} no cartão.')
else:
    if q_carne.capitalize() == 'A': 
        print(f'Alcatra {q_carne:.2f}kg R${pt:.2f} no sem cartão.')
    if q_carne.capitalize() == 'F': 
        print(f'File Duplo {q_carne:.2f}kg R${pt:.2f} no sem cartão.')
    if q_carne.capitalize() == 'P':
        print(f'Picanha {q_carne:.2f}kg R${pt:.2f} no sem cartão.')


'''
