"""
Estrutura Sequencial
site:https://wiki.python.org.br/EstruturaSequencial
nome: Maykoll Rocha
 Todos os exercios feitos por mim baseado no conhecimento que tenho no dia
09 de novembro de 2022.
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
# 1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("Ola mundo")
"""

"""
# 2.Faça um Programa que peça um número e então mostre a mensagem O número 
# informado foi [número].

num = int(input("Entre com o número: "))

print("O Numero informado foi")

"""

"""
# 3.Faça um Programa que peça dois números e imprima a soma.
num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))

print(num1 + num2)
"""

"""
# 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Entre com a primeira nota: "))
n2 = float(input("Entre com a segunda nota: "))
n3 = float(input("Entre com a terceira nota: "))
n4 = float(input("Entre com a quarta nota: "))
mediaF = (n1+n2+n3+n4)/2

print("Média {:.2f}".format(mediaF))

# vou fazer de um modo mais avançado
notas = [float(input(f"Nota{i+1}:")) for i in range(0, 4)]
print(f"Média do semestre foi: {sum(notas)/len(notas)}")

"""
"""
# 5.Faça um Programa que converta metros para centímetros.

metros = int(input("Entre com a medida em metros: "))
print(f"{metros}m são {metros*100}cm")

"""

"""
# 6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r = float(input("Entre com o raio do circulo: "))

area = 3.1415*(r**2)

print(f"A area do circulo é {area:.2f}")
"""

"""
# 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o
# dobro desta área para o usuário.

l = float(input("Entre com a area do quadrado: "))
print(f"O dobro da area é {2*(l*l) :.2f}")

"""

"""
# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
# referido mês.

ganho_p_horas = float(input("Entre com quanto você ganha por hora: "))
horas_p_mes = float(input("Quantas horas trabalha por mes: "))

print(f"Você ganha R${ganho_p_horas*horas_por_mes:.2f} por mes.\n")

"""

"""
# 9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme 
# e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

F = float(input("Entre com a temperatura em Fahrenheit: "))
C = 5 * ((F-32) / 9) 
print(f'A temperatura é de {C:.2f}ºC')
"""

"""
# 10.Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

C = float(input("Entre com a Temperatura em Celcius: "))
F = C*9/5 + 32
print(f'A temperatura é de {F:.2f}ºF')
"""

"""
# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e
# mostre:
# a.o produto do dobro do primeiro com metade do segundo .
# b.a soma do triplo do primeiro com o terceiro.
# c.o terceiro elevado ao cubo.

n1 = int(input("Entre com o 1ªnumero: "))
n2 = int(input("Entre com o 2ªnumero: "))
n3 = float(input("Entre com o 3ªnumero: "))

print(f"a.{(2*n1) * (n2/2)}\n b.{3*n1 + n3}\n c.{n3**3}")

"""

"""
# 12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Entre com a altura: "))
print(f"o peso ideal é {((72.7*altura) - 58):.2f} para Homens.")

"""

""" 
# 13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a.Para homens: (72.7*h) - 58
# b.Para mulheres: (62.1*h) - 44.7

altura = float(input("Entre com a altura: "))
print(f"o peso ideal é {((72.7*altura) - 58):.2f} para Homens.")
print(f"o peso ideal é {((62.1*altura) - 44.7):.2f} para Mulheres.")

"""

"""
# 14.João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
# controlar o rendimento diário de seu trabalho. Toda vez que ele traz um 
# peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
# excedente. João precisa que você faça um programa que leia a variável peso 
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
# de quilos além do limite e na variável multa o valor da multa que João deverá
# pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Peso do peixe: "))
execesso = peso_peixe - 50
multa = execesso*4.00
print(f"O excesso foi de {execesso:.2f}Kg e deve ser pago R${multa:.2f}.")

"""

"""
# 15.Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário
# no referido mês, sabendo-se que são descontados 11% para o Imposto de
# Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#       a.salário bruto.
#       b.quanto pagou ao INSS.
#       c.quanto pagou ao sindicato.
#       d.o salário líquido.
#       e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
#           + Salário Bruto : R$
#           - IR (11%) : R$
#           - INSS (8%) : R$
#           - Sindicato (5%) : R$
#           = Salário Liquido : R$
#       Obs.: Salário Bruto - Descontos = Salário Líquido.
        
ganho_p_horas = float(input("Entre com quanto você ganha por hora: "))
horas_p_mes = float(input("Quantas horas trabalha por mes: "))
salario_bruto = ganho_p_horas*horas_p_mes
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"a.R${salario_bruto:.2f}.\n b.R${inss:.2f}.\n c.R${sindicato:.2f}.")
print(f"d.R${salario_liquido:.2f}.")
print(f"+ R${salario_bruto:.2f}\n- R${ir:.2f}\n- R${inss:.2f}")
print(f"- R${sindicato:.2f}\n= R${salario_liquido:.2f}..")        
        
"""

"""
# 16.Faça um programa para uma loja de tintas. O programa deverá pedir 
# o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe 
# ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total.

area = float(input("Entre com o tamanho da area em m²: "))
latas_1l = area//3
latas_18l = latas_1l//18 + 1

print(f"Quantidade de latas {latas_18l} preço R${latas_18l*80.00}\n")

"""

"""
# 17.Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
# da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
# vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 
# 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os 
#   respectivos preços em 3 situações:
#       a.comprar apenas latas de 18 litros;
#       b.comprar apenas galões de 3,6 litros;
#       c.misturar latas e galões, de forma que 
#       o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, 
# isto é, considere latas cheias.

area = float(input("Entre com o tamanho da area em m²: "))
area = area + area*0.10
latas_1l = area//6 + 1
latas_18l = latas_1l//18
latas_36l = latas_1l//3.6 + 1
rest_litros = latas_1l - latas_18l*18
lasta36l = rest_litros//3.6 + 1
print(f"a.Quantidade de latas {latas_18l} preço R${latas_18l*80.00}\n")
print(f"b.Quantidade de latas {latas_36l} preço R${latas_36l*25.00}\n")
print(f"c.Quantidade de latas {latas_18l+lasta36l} preço",
      f"R${latas_18l*80.00 + lasta36l*25.00 }\n")
      
"""

"""
# 18.Faça um programa que peça o tamanho de um arquivo para 
# download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando
# este link (em minutos).

tam_arq = float(input("Entre com o tamanho do arquivo(mb): "))
veloc_link = float(input("Entre com a velociade do link(Mbps): "))
temp = (tam_arq/veloc_link)/60
print(f"tempo para dowlond é de {temp:.2f}min.")

"""
