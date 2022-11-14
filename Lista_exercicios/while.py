'''
1. Elaborar um algoritmo que leia números enquanto forem positivos
e imprima quantos números foram digitados.
num = 1
cont = -1  # comecei em -1 por conta que no laço ele vira zero no incio
while num > 0:
    cont += 1
    try:
        num = int(input('Entre com um numero quando negativo sai: '))
    except:
        print('não é um numero.')
        cont -= 1
        num = 1

print(f'Foram digitados {cont} numeros')
'''

'''
2. Elaborar um algoritmo que leia números enquanto forem positivos
e imprima a média dos números digitados
num = 0
cont = -1
soma = 0
while num >= 0:
    soma += num
    cont += 1
    try:
        num = int(input('Entre com um numero quando negativo sai: '))
    except:
        print('não é um numero.')
        cont -= 1
        num = 0

print(f'Média de {soma/cont} numeros')

'''

'''
3. Elaborar um algoritmo que leia números e imprima no final quantos
números entre 100 e 200 foram digitados. Quando o valor 0 (zero) for
lido, o algoritmo deve parar a sua execução.
num = -1
cont = 0
soma = 0
while num != 0:
    if 100 < num < 200:
        cont += 1
    try:
        num = int(input('Entre com um numero 0 para sai: '))
    except:
        print('não é um numero.')
        num = -1

print(f'Numeros ente 100 e 200 foram {cont} numeros')
'''

'''
4. Elaborar um algoritmo que leia várias profissões e imprima quantos
são dentistas. Considere as seguintes variações de digitação da
palavra: DENTISTA, dentista e Dentista.(com capitalize tirnase desnecessario
checar variação)
profissao = ' '
cont = 0
while profissao != 'Sair':
    if profissao == 'Dentista':
        cont += 1

    profissao = input(
        'Entre com profissões, digite Sair para sair: ').capitalize()

print(f'Tivemos {cont} Dentista durante o programa.')
'''

'''
5. Elaborar um algoritmo que leia vários números positivos e
imprimir o quadrado de cada número até entrar um número múltiplo
de 6 que deverá ter seu quadrado impresso também.
num = 1.3

while num % 6 != 0:
    try:
        num = abs(float(input('Entre com um número: ')))
        print('O numero ao quadrado é ', num**2)
    except:
        print('Entrou com um valor errado.')
        num = 1.3
'''

'''
6. Elaborar um algoritmo que leia vários números até entrar o número -999.
Para cada número imprimir seus divisores.

num = 0
while num != -999:
    try:
        num = int(input('Entre com um numero: '))
        if num != -999:
            cont = 1
            print('Divisivel por: ')
            while cont <= num:
                if num % cont == 0:
                    print(f' {cont},', end=' ')
                cont += 1
            print('.')
    except:
        print('Entrou com algum valor invalido.')
        num = 1

'''


'''
7. Elaborar um algoritmo que calcule e imprima o valor de b^n. O valor de
n deverá ser maior do que 1 e inteiro e o valor de b maior ou igual
a 2 e inteiro

while True:
    try:
        b = abs(int(input('Entre com o valor de b sendo maior que 2: ')))
        if b < 2:
            break

        n = abs(int(input('Entre com o valor de n: ')))

        if n < 1:
            break

        print(f'b^n é {b**n}')
    except:
        print('Algum valor foi digitado errado.')
'''

'''
8. Chico tem 1,50m e cresce dois centímetros por ano, enquanto Juca
tem 1,10m e cresce 3 centímetros por ano. Construir um algoritmo
que calcule e imprima quantos anos serão necessários para que Juca
seja maior que Chico
juca_altura = 1.10
chico_altura = 1.50
anos = 0
while juca_altura < chico_altura:
    juca_altura += 0.03
    chico_altura += 0.02
    anos += 1

print(f'Em {anos} anos Juca sera maior que Chico')
'''

'''
9. Dado um país A com 5.000.000 de habitantes e uma taxa de natalidade de
3% ao no, e um país B com 7.000.000 de habitantes e uma taxa de natalidade
de 2% ao ano, calcular e imprimir o tempo necessário para que a população
do país A ultrapasse a população do país B

populaçãoA = 5000000
populaçãoB = 7000000
anos = 0
while populaçãoA < populaçãoB:
    populaçãoA += populaçãoA*0.03/1000
    populaçãoB += populaçãoB*0.02/1000
    anos += 1

print(f'Em {anos} anos a população A sera maior que a B.')
'''

'''
10. Uma agência bancária possui vários clientes que podem fazer investimentos
com rendimentos mensais, conforme a tabela abaixo. Faça um algoritmo que leia
o código do cliente, o tipo do investimento e o valor investido, e que calcule
e mostre o rendimento mensal de acordo com o tipo de investimento. A leitura
terminará quando o código do cliente for menor ou igual a 0.

Tipo  Descrição             Rendimento mensal
1     Poupança              1,5%
2     Poupança plus         2%
3     Fundos de renda fixa  4%

while True:
    try:
        cod = int(input('Entre com o numero do cliente: '))
        if cod <= 0:
            break

        tipo_invest = abs(int(input('Entre com o tipo de invstimento:')))
        valor = abs(float(input('Entre com o valor a ser investido: ')))
        match tipo_invest:
            case 1: print(f'O redimento mensal na poupança é {valor*0.015:.2f}')
            case 2: print(f'O redimento mensal na poupança'
                          f'plus é {valor*0.02:.2f}')
            case 3: print(f'O redimento mensal na fundo de renda'
                          f'fixa é {valor*0.04:.2f}')
            case _: print(f'Valor invalido.')
    except:
        print('Entrou com um valor errado.')
        

'''

'''
11. Entrar com nomes enquanto forem diferentes de FIM e imprimir o
primeiro caractere de cada nome.
armazem = ''
while True:
    nome = input('Entre com um nome: ')
    if nome.capitalize()== 'Fim':
        break
    
    if not nome.isdecimal():
        armazem += nome[0]
cont = 0
while cont < len(armazem):
    print(armazem[cont], end='-')
    cont +=1
'''

'''
12. Faça um algoritmo que controle o saldo bancário de um cliente.
O algoritmo lê o valor do saldo anterior e em seguida lê as operações 
realizadas na conta. As operações podem ser as seguintes:
    a. Saque em dinheiro (código = 10)
    b. Depósito (código = 33)
    c. Pagamento de cheque (código = 4)
O algoritmo lê o código das operações e realiza as atualizações na conta,
imprimindo uma mensagem ao usuário caso seu saldo se torne negativo. O 
algoritmo deverá continuar a leitura até que o código da operação seja zero.
Códigos diferentes dos definidos devem ser ignorados. Ao final do processamento
o algoritmo deverá imprimir o saldo atual do cliente.
saldo_atual = float(input('Entre com o saldo: '))
cod = None
while cod != 0:
    if saldo_atual < 0:
        print('Saldo Negativo.')
    cod = abs(int(input('Entre com a função 33-Deposito'
                        '10-Saque e 4-Paga 0-Sair: ')))
    match cod:
        case 10:
            saque = abs(float(input('Quanto vai sacar: ')))
            saldo_atual -= saque
        case 33:
            deposito = abs(float(input('Deposito de: ')))
            saldo_atual += deposito
        case 4:
            pague = abs(float(input('Valor do cheque: ')))
            saldo_atual -= pague

print(f'{saldo_atual=:.2f}')
'''

'''
13. Calcule a média aritmética de vários valores inteiros positivos informados
pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.
num = 0
cont = 0
soma = 0
while True:
    num = int('Entre com um numero negativo para sair: ')
    if num < 0:
        break
    soma += num
    cont += 1

print(f'média de {soma/cont}')
'''

'''
14. Em uma eleição presidencial existem quatro candidatos. Os votos são 
informados por meio de códigos. Os dados utilizados para a contagem dos 
votos obedecem à seguinte codificação:
     1,2,3,4 = voto para os respectivos candidatos;
     5 = voto nulo;
     6 = voto em branco;
Leia o código do candidado em um voto. Calcule e escreva:
     total de votos para cada candidato;
     total de votos nulos;
     total de votos em branco;
Como finalizador do conjunto de votos, tem-se o valor 0.

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
votoN = 0
votoB = 0
cont = 0
while True:
    tipo = abs(int(input('Entre com o voto:')))
    if tipo == 0:
        break

    match tipo:
        case 1: voto1 += 1
        case 2: voto2 += 1
        case 3: voto3 += 1
        case 4: voto4 += 1
        case 5: votoN += 1
        case 6: votoB += 1
    cont += 1

print(f'Votos total:{cont}')
print(f'{voto1=},{voto2=},{voto3=},{voto4=},{votoN=},{votoB=}.')
'''

'''
15. Leia um número não determinado de valores e calcule a média aritmética 
dos valores lidos, a quantidade de valores positivos, a quantidade de valores 
negativos e o percentual de valores negativos e positivos.Mostre os resultados.
num_neg = 0
num_pos = 0
num = None
soma = 0
while num != 0:
    num = float(input('Entre com 0 para sair: '))
    if num > 0:
        num_pos += 1
        soma += num

    if num < 0:
        num_neg += 1
        soma += num

print(f'A media de {soma/(num_pos+num_neg)}')
print(f'Foram {num_pos} numeros positivos'
      f'com uma taxa de {(num_pos/(num_pos+num_neg))*100:.2f}%')
print(f'Foram {num_neg} numeros negativos'
      f'com uma taxa de {(num_neg/(num_pos+num_neg))*100:.2f}%')
      
'''

'''
16. Leia vários números inteiros e calcule o somatório dos números negativos.
O fim da leitura será indicado pelo número 0.

num = None
soma = 0
while num != 0:
    num = float(input('Entre com o numero 0 para sair: '))
    if num < 0:
        soma += num

print(f'A somatoria dos negativos é {soma}.')

'''

'''
17. Leia vários números inteiros e positivos e calcule o produtório dos 
números pares. O fim da leitura será indicado pelo número 0.
num = None
prod = 1
while num != 0:
    num = abs(int(input('Entre com o numero 0 para sair: ')))
    if not num % 2 and num != 0:
        prod *= num

print(f'A somatoria dos negativos é {prod}.')
'''

'''
18. Uma pesquisa foi realizada entre os habitantes de uma região. Foram 
coletados os dados de idade, sexo (M/F) e salário. Informe:
     a) a média de salário do grupo;
     b) maior e menor idade do grupo;
     c) quantidade de mulheres com salário até R$100,00.
Encerre a entrada de dados quando for digitada uma idade negativa.

infa = 0
maior_id = 0
menor_id = 60
infc = 0
cont = 0

while True:
    sexo = input('M para macho e F pra femea: ').capitalize()
    if sexo not in 'MF' or len(sexo) > 1:
        continue

    idade = int(input('Entre com uma idade: '))
    if idade < 0:
        break

    salario = abs(float(input('Entre com o seu suado dinheirinho: ')))
    cont += 1
    infa += salario

    if idade > maior_id:
        maior_id = idade

    if idade < menor_id:
        menor_id = idade

    if sexo == 'F' and salario <= 100:
        infc += 1


print(f'Média de salário: R${infa/cont :.2f}.')
print(f'Maior idade {maior_id} Menor idade {menor_id}.')
print(f'Femea que ganha mais de 100 reias: {infc}')

'''

'''
19. Uma pesquisa foi realizada sobre algumas características físicas da população de uma 
cidade, a qual coletou os seguintes dados referentes a cada habitante para serem 
analisados:
     sexo (masculino e feminino)
     cor dos olhos (azuis, verdes ou castanhos)
     cor dos cabelos ( louros, castanhos, pretos)
     idade
Determine e escreva:
     a maior idade dos habitantes
     a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 entrada como idade.

dadoA = 0
dadoB = 0
while True:
    sexo = input('Entre com F para feminino e M para masculino: ').capitalize()\
        or 'M'
    if sexo not in 'MF' or len(sexo) > 1:
        continue
    cor_eye = input('Olhos: A - azul V - Verde C-castanho: ').capitalize()\
        or None
    cor_hair = input('Cabelo: L - louiro C-castanho P-pretro: ').capitalize()\
        or None
    idade = int(input('Entre com a idade: '))

    if idade == -1:
        break

    if idade > dadoA:
        dadoA = idade

    if sexo == 'F' and 18 <= idade <= 35 and \
            cor_eye == 'V' and cor_hair == 'C':
        dadoB += 1

print(f'Maior idae {dadoA} e mulheres com certas epecificaçoes {dadoB}.')

'''


'''
20. Leia vários números inteiros positivos e apresente a soma dos números pares.
O fim da leitura será indicado pelo número 0.

soma = 0
while True:
    num = abs(int(input('Entre com os valores: ')))
    if num == 0:
        break
    if not num % 2:
        soma += num

print(f'soma é {soma}.')

'''

'''
21. Leia vários números inteiros e positivos e informe a quantidade de números
múltiplos de 3 (três). O fim da leitura será encerrada quando o usuário
digitar 0 (zero) ou menos.

dado = 0
while True:
    num = int(input('Entre com o numeros: '))
    if num <= 0:
        break

    if not num % 3:
        dado += 1

print(f'Os multiplos de 3 digitados foram {dado}')
'''

'''
22. Leia vários números inteiros e positivos e informe a média dos números 
múltiplos de 4(quatro). O programa será encerrado quando o usuário digitar
0 (zero) ou menos.
soma = 0
cont = 0
while True:
    num = int(input('Entre com os valores: '))

    if num <= 0:
        break

    if not num % 4:
        soma += num
        cont += 1

print(f'Média: {soma/cont:.2f}')
'''

'''
23. Leia a idade e a altura de várias pessoas. Calcule e informe a média das
alturas das pessoas com mais de 50 anos. Para encerrar o programa digite zero
para idade
alturas = 0
cont = 0
while True:
    idade = abs(int(input('Entre com a Idade: ')))
    if idade == 0:
        break
    altura = abs(float(input('Entre com a altura: ')))

    if idade > 50:
        alturas += altura
        cont += 1

print(f'A media das alturas com mais 50 é {alturas/cont:.2f}')
'''

'''
24. Leia uma seqüência de números e imprima o número que for múltiplo de sua posição 
na seqüência. A leitura termina com a entrada 0.
Exemplo: 
Valores lidos:  3  7  8  16
      Posição:  1  2  3  4
    Impressão:  3  16
    
valores_lidos = ''
posissao = ''
impresao = ''
posisao = 0
while True:
    num = abs(int(input('Entre com o valor a ser lido: ')))
    if num == 0:
        break
    posisao += 1

    valores_lidos += f'{num} '
    posissao += f'{posisao} '

    if not num % posisao:
        impresao += f'{num},'

print(valores_lidos, posissao, impresao, sep='\n')
'''

'''
25. Leia o nome e a altura das moças inscritas em um concurso de beleza. A
leitura deve parar quando receber a palavra VAZIO no lugar do nome. Calcule 
e escreva as duas maiores alturas e quais são as moças que as possuem.

nome1 = ''
alt1 = 0
nom2 = ''
alt2 = 0
while True:
    nome = input('Entre com o nome: ') or None

    if nome.upper() == 'VAZIO' or nome == None:
        break

    alt = abs(float(input('Entre com a altura: ')))
    if alt > alt1:
        nome1 = nome
        alt1 = alt
    elif alt > alt2:
        nom2 = nome
        alt2 = alt

print('A maior é', nome1, alt1, 'E a segunda maior é ', nom2, alt2)

'''
