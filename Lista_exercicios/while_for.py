'''
nome: Maykoll Rocha
dia: 14/11/2022
Todos os codigos foi tirado de uma lista de C que fazia durante meu primeiro ano
de progração passarei tudo para python e estara tanto o enunciado quando a 
solução em DOCstrings.

'''

'''
1. Leia 10 valores e encontre o maior e o menor deles. Mostre o resultado.

maior = 0
menor = 1000
for i in range(10):
    num = float(input('Entre com o '))
    
    if maior < num:
        maior = num
        
    if menor > num:
        menor = num

print(f'{maior=} {menor=}')
'''

'''
2. Apresente os resultados da soma e da média aritmética dos valores pares 
situados na faixa numérica de 50 a 70.

soma = 0
for i in range(50, 71, 2):
    soma += i
print(soma/20)

'''

'''
3. Some e conte, separadamente, os números pares e ímpares de 20 números 
inteiros informados pelo usuário. Ao fim, apresentar a soma e a quantidade.

cont_par = 0
cont_impar = 0
soma = 0

for i in range(20):
    num = float(input('Entre com o valores: '))

    soma += num
    if not num % 2:
        cont_par += 1
    else:
        cont_impar += 1

print(f'{soma=} {cont_impar=} {cont_par=}')
'''


'''
4. Elaborar um programa que efetue a leitura de valores positivos inteiros até 
que um valor negativo seja informado. Ao final devem ser apresentados o maior e
o menor valor informados pelo usuário.

maior = 0
menor = 1000
while True:
    num = int(input('Entre com valores: '))

    if num < 0:
        break

    if menor > num:
        menor = num

    if maior < num:
        maior = num

print(f'{maior=} {menor=}')

'''

'''
5. Uma pousada estipulou o preço da diária em R$ 40,00 e mais uma taxa de
serviços diários de:
- R$ 15,00, se o número de dias for menor que 10;
- R$ 8,00, se o número de dias for maior ou igual a 10.
Criar um programa que imprima o nome, o valor da conta de cada cliente e ao 
final o total arrecadado pela pousada

estrato = 'Nome  Conta\n'
total = 0
while True:
    cliente = input('Entre com o cliente ou com nada para sair: ').capitalize()\
        or 1

    if cliente == 1:
        break

    num_day = int(input('Número de dias que vai ficar: '))
    conta = 40*num_day

    if num_day < 10:
        conta += 15
    else:
        conta += 8
    
    total += conta
    estrato += f'{cliente} R${conta:.2f}\n'
print('-'*20, estrato, '-'*20, f'Lucro final R${total:.2f}',sep='\n')
'''

'''
6. Uma fábrica produz e vende vários produtos e para cada um deles tem se o 
nome, quantidade produzida e quantidade vendida. Criar um programa que mostre:
- Para cada produto, nome, quantidade no estoque e uma mensagem se o produto 
tiver menos de 50 itens no estoque.

estoque = 'Nome|Quantidade|Status\n'
while True:
    nome = input('Entre com o nome do produto (ENTER == SAIR): ').capitalize()\
        or 0
    if not nome:
        break

    quantidade = abs(int(input('Quantiade do prosuto: ')))

    quant_vend = abs(int(input('Quantidade de prduto vendida: ')))

    quantidade -= quant_vend

    if quantidade < 50:
        estoque += f'{nome}|{quantidade}|<50\n'
    else:
        estoque += f'{nome}|{quantidade}|OK\n'

print(estoque)
'''

'''
7. Apresentar os resultados das potências de 3, variando do expoente 0 até o
expoente 15. Deve ser considerado que qualquer número elevado a zero é 1, e 
elevado a 1 é ele próprio. 

for i in range(16):
    print(f'3 ao expente {i} == {3**i}')

'''

'''
8. Apresente como resultado o valor de uma potência de uma base B qualquer elevada a 
um expoente E qualquer, ou seja, de B^E, em que B é o valor da base 
e E o valor do expoente. 

while True:
   
    exp = int(input('Entre com espoente (<0 == sair): '))
    if exp < 0:
        break
    
    b = abs(int(input('Entre com a Base: ')))
    
    print(f'{b} ao expoente {exp} == {b**exp}')

'''

'''
9. 
Uma empresa decidiu fazer um levantamento em relação aos candidatos que se 
apresentarem para preenchimento de vagas no seu quadro de funcionários. Suponha 
que você seja o programador dessa empresa, criar um programa que leia para cada
candidato a idade, o sexo e se tem experiência no serviço (S ou N).Para encerrar 
programa, digite zero para idade. Calcule e escreva:
- O número de candidatos do sexo feminino;
- O número de candidatos do sexo masculino;
- A idade média dos homens que já tem experiência no serviço

cand_M = 0
cand_F = 0
ida_med_M_S = 0
nixo = 0
while True:
    idade = abs(int(input('Entre com a idade (0==sair): ')))
    if not idade:
        break

    sexo = input('Sexo [M]asculino ou [F]eminino: ').upper()
    expe = input('Experiencia [S]im ou [N]ão: ').upper()

    if sexo == 'M':
        cand_M += 1

    if sexo == 'F':
        cand_F += 1

    if sexo == 'M' and expe == 'S':
        ida_med_M_S += idade
        nixo += 1

print(f'a.{cand_F=}\nb.{cand_M=}\nc.{ida_med_M_S/nixo}')

'''

'''
10. 
Faça um programa que leia a idade e a altura de várias pessoas. Calcule e
informe amédia das alturas das pessoas com mais de 50 anos. Para encerrar o 
programa digite zero para idade.

media_altura = 0
pessoa_mais50 = 0
while True:
    idade = abs(int(input('Entre com a idade (0==sair): ')))
    if not idade:
        break

    altura = abs(float(input('Entre com a altura: ')))

    if idade > 50:
        media_altura += altura
        pessoa_mais50 += 1

print(f'A media de altura com pessoas com mais de 50 é '
      f'{media_altura/pessoa_mais50:.2f}.')
      
'''

'''
11. Efetue a leitura de 15 valores numéricos inteiros e no final apresente o 
total do somatório da fatorial de cada valor lido

soma = 0
for i in range(15):
    num = abs(int(input('Entre com um número: ')))
    fat = 1
    for p in range(1, num+1):
        fat *= p
    soma += fat

print(soma)

'''

'''
12. Apresente como resultado o valor do fatorial dos valores ímpares situados
na faixa numérica de 1 a 10

for i in range(1, 11):
    if i % 2:
        fat = 1
        for p in range(1, i+1):
            fat *= p
        print(f'{i}! = {fat}')
        
'''

'''
13.
Efetue o cálculo e apresente o somatório do número de grãos de trigo que se pode 
obter num tabuleiro de xadrez, obedecendo à seguinte regra: colocar um grão de 
trigo no primeiro quadro e nos quadros seguintes o dobro do quadro anterior. 
Ou seja, no primeiro quadro coloca-se 1 grão, no segundo quadro colocam-se 2 
grãos (neste momento têm-se 3 grãos), no terceiro quadro colocam-se 4 grãos 
(tendo neste momento 7 grãos), no quarto colocam-se 8 grãos (tendo-se então 15 
grãos) até atingir o sexagésimo quarto (64) quadro. Utilize variáveis do tipo 
real como acumuladores.

soma = 0
grãos = 1
for i in range(64):
    soma += grãos
    grãos *= 2
print(soma)

'''

'''
14. 
Efetue a leitura sucessiva de valores numéricos e apresente no final o total do 
somatório, a média aritmética e o total de valores lidos. O programa deve fazer 
as leituras dos valores enquanto o usuário estiver fornecendo valores positivos.
Ou seja, o programa deve parar quando o usuário fornecer um valor negativo. Não 
se esqueça que o usuário pode entrar como primeiro número um número negativo, 
portanto, cuidado com a divisão por zero no cálculo da média.


cont = 0
soma = 0
while True:
    num = int(input('Entre com um valor: '))
    if num < 0:
        break

    soma += num
    cont += 1

if cont:
    print(f'Foram digitados {cont} e sua média deu {soma/cont:.2f}. ')
else:
    print('Não teve valores digirados')
    
'''

'''
15. Calcule a área total de uma residência (sala, cozinha, banheiro, quartos, 
área de serviço, quintal, garagem, etc.). O seu algoritmo/programa deve 
solicitar a entrada do nome, a largura e o comprimento de um determinado cômodo.
Em seguida, deve apresentar a área do cômodo lido e também uma mensagem 
solicitando do usuário confirmação de continuar calculando novos cômodos. Caso 
o usuário responda “NAO”, o programa deve apresentar o valor total acumulado da 
área residencial.

area_total = 0
registro_geral = 'Comodo name|Area\n'
while True:
    nome = input('Entre com o nome do comodo: ').capitalize()
    largura = abs(float(input('Entre com a largura do comodo: ')))
    comprimento = abs(float(input('Entre com a comprimento do comodo: ')))
    print(f'{nome} tem area {largura*comprimento}')
    area_total += largura*comprimento
    registro_geral += f'{nome}|{largura*comprimento}\n'
    sair = input('Quer por mais comodos? ').upper()
    if sair == 'NAO':
        registro_geral += '-'*20
        registro_geral += f'\ntudo|{area_total}\n'
        break
print(registro_geral)

'''

'''
16. Uma empresa classifica seus funcionários em três níveis de acordo com um 
índice de produtividade. São eles (1) Excelente, (2) Bom e (3) Regular. Cada 
nível acrescenta um abono ao salário base do funcionário, de acordo com a 
seguinte tabela:
- Excelente: 80% do salário base;
- Bom: 50% do salário base;
- Regular: 30% do salário base
O programa deve ler a matrícula do funcionário, seu salário base e seu nível de 
abono. Calcular e imprimir o salário a ser pago (salário a ser pago é = salário 
base + abono). O programa será encerrado quando for digitado zero para matrícula.

while True:
    cod = abs(int(input('Entre com o cosigo da matricula: ')))
    if not cod:
        break

    salario = float(input('Entre com o salario: '))
    abono = abs(int(input('1-exlente 2-bom 3-ruim: ')))

    match abono:
        case 1: pago = salario*1.8
        case 2: pago = salario*1.5
        case _: pago = salario*1.3

    print(f'{pago=}')
    
'''

'''
17. 
Uma empresa deseja aumentar seus preços em 20%. Faça um programa que leia o 
código, o preço de custo de vários produtos e que calcule o novo preço de cada 
um deles. Calcule também a média de preços com e sem aumento. Mostre o código
e o novo preço de cada produto e, no final, as médias. A entrada de dados deve 
terminar quando for recebido um código de produto menor ou igual a zero.

cont_prod = 0
soma_saum = 0
soma_caum = 0
while True:
    cod = abs(int(input('Entre com o cosigo do produto: ')))
    if not cod:
        break

    cont_prod += 1
    valor = abs(float(input('Entre com o valor do produto: ')))

    soma_caum += valor*1.2
    soma_saum += valor
    print(f'prosuto {cod} com aumento fica {valor*1.2:.2f}.')

print(f'Com aumento: {soma_caum/cont_prod:.2f}|Sem:{soma_saum/cont_prod:.2f}')

'''

'''
18. Faça um programa para: 
a) Ler um valor X e um valor N.
b) Calcular: Y = X - 2X + 4X - 6X + 8X - 10X + … NX

x = abs(float(input('Entre com um valor: ')))
n = abs(int(input('Entre com outro valor para os passos: ')))
y = x
t = 0
for i in range(2, n+1, 2):
    if not t:
        y -= i*x
        t = 1
    else:
        y += i*x
        t = 0
print(y)

'''

'''
19.
Apresente o resultado inteiro da divisão de dois números quaisquer. Para a 
elaboraçãodo programa, não utilizar em hipótese alguma o conceito do operador 
aritmético DIV. A solução deve ser alcançada com a utilização de repetição 
(looping). Ou seja, o programa deve apresentar como resultado (quociente) 
quantas vezes o divisor cabe no dividendo.

divisor = abs(int(input('Entre com o divisor: ')))
dividendo = abs(int(input('Entre com o dividendo: ')))
quociente = 0
while divisor < dividendo:
    quociente += 1
    dividendo -= divisor

print(f'quociente = {quociente}\nresto = {dividendo}')
'''

'''
20. Em uma eleição presidencial existem quatro candidatos. Os votos são 
informados através de códigos. Os dados utilizados para a contagem dos votos 
obedecem à seguinte codificação: 
- 1,2,3,4 = voto para os respectivos candidatos; 
- 5 = voto nulo;
- 6 = voto em branco;
Elabore um algoritmo/programa que leia o código do candidato em um voto. 
Calcule e escreva: 
- total de votos para cada candidato; 
- total de votos nulos; 
- total de votos em branco;
Como finalizador do conjunto de votos, tem-se o valor 0.

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto_Branco = 0
voto_Nulo = 0

while True:
    voto = abs(int(input('Entre com 1-6: ')))

    if voto == 0:
        break

    if voto > 6:
        continue

    match voto:
        case 1: voto1 += 1
        case 2: voto2 += 1
        case 3: voto3 += 1
        case 4: voto4 += 1
        case 5: voto_Nulo += 1
        case 6: voto_Branco += 1

print(f'{voto1=}\n{voto2=}\n{voto3=}\n{voto4=}\n{voto_Nulo=}\n{voto_Branco=}')

'''
