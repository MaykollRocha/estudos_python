'''
Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. 
Caso o usuário digite um número fora desse intervalo, deverá aparecer
uma mensagem informando que não existe mês com esse número.

num = abs(int(input('Entre com um numero de 1-12 para representar'
                    'o mes do ano:')))
match num:
    case 1: print("Janeiro.")
    case 2: print('Fevereiro.')
    case 3: print('Março.')
    case 4: print('Abril.')
    case 5: print('Maio.')
    case 6: print('Junho.')
    case 7: print('Julho.')
    case 8: print('Agosto.')
    case 9: print('Setembro.')
    case 10: print('Outubro.')
    case 11: print('Novembro.')
    case 12: print('Dezembro.')
    case _: print('Invalido.')
    
'''


'''
Faça um algoritmo/programa em C que simule uma calculadora com as quatro 
operações básicas (adição, subtração, multiplicação e divisão).
Deve ser solicitado ao usuário a entrada dos dois operandos e da operação
a ser executada, na forma de um menu. Dependendo da operação escolhida,
deve ser executada a operação solicitada e ser esccrito o seu resultado. 

op = input('Entre com o operador\n+-*/\n')
if op in '+-*/':
    num1 = float(input('Entre com o Número: '))
    num2 = float(input('Entre com o Número: '))
    match op:
        case '+': print(f'{num1+num2}')
        case '-': print(f'{num1-num2}')
        case '*': print(f'{num1*num2}')
        case '/': print(f'{num1/num2}')
        case _: print('Provavelmente tem 2 operadores.')
else:
    print('Não é uma opção valida.')
    
'''

'''
Faça um algoritmo/programa em C que verifique se um caractere digitado é
numérico (0 a 9) e, caso contrário, se é uma vogal ou uma consoante, 
ou outro caractere qualquer.

digt = input('Entre com um digito: ')

op = None

if digt.isdecimal():
    op = 1
else:
    if digt.capitalize() in 'AEIOU':
        op = 2
    elif digt.capitalize() in 'QWRTYPSDFGHJKLÇZXCVBNM':
        op = 3

match op:
    case 1: print('É um digito.')
    case 2: print('É uma vogal.')
    case 3: print('É uma consoante')
    case _: print('É outra coisa.')
'''

'''
Ler o pedido de um cliente de fast food, baseado no menu abaixo, 
e imprimir o preço total e a opção que ele escolher. 
Opção 
(única) 
Promoção | Especificação| Preço (R$) 
1 |Big Super Sanduba |2 hambúrgueres, queijo, batata fritas e refrigerante|5,00 
2 |Quase Super Sanduba| 1 hambúrguer, batata fritas e refrigerante |3,00 
3 |Mirradus Sanduba |1 misto quente e refrigerante 1,50
op = int(input('Entre com a opção 1-3 de lanche: '))

match op:
    case 1: print('Big Super Sanduba | 2 hambúrgueres, queijo,'
                  'batata fritas e refrigerante | 5,00')
    case 2: print('Quase Super Sanduba | 1 hambúrguer, batata' 
                  'fritas e refrigerante | 3,00 ')
    case 3: print('Mirradus Sanduba | 1 misto quente e refrigerante | 1,50')
    case _: print('Não é uma opção valida.')
'''

'''
 Criar um algoritmo para ler o preço e a categoria de um produto. Calcular
 e mostrar o reajuste de acordo com a categoria. Se for: A = 50%, B = 25% ,
 C=15 % e outras 5%.

preco = abs(float(input('Entre com o preço do produto: ')))
op = input(' A = 50%, B = 25% ,C=15 % e outras 5%').capitalize()

match op:
    case 'A': print(f'O valor do reajuste é {preco*1.5}')
    case 'B': print(f'O valor do reajuste é {preco*1.25}')
    case 'C': print(f'O valor do reajuste é {preco*1.15}')
    case _: print(f'O valor do reajuste é {preco*1.05}')
'''

'''
Criar um algoritmo para ler as letras iniciais de um estado civil
e o sexo da pessoa e mostrar a descrição: casado(a), solteiro(a), 
viúvo(a), divorciado(a), inválido

sexo = input('Entre com o sexo: ')
es_civil = input('Entre com o estado civil: ')

match sexo[0].capitalize():
    case 'M':
        match es_civil[0].capitalize():
            case 'C': print('Casado.')
            case 'D': print('Divorcidado.')
            case 'S': print('Solteiro.')
            case 'V': print('Viuvo.')
            case _: print('Invalido.')
    case 'F':
        match es_civil[0].capitalize():
            case 'C': print('Casada.')
            case 'D': print('Divorcidada.')
            case 'S': print('Solteira.')
            case 'V': print('Viuva.')
            case _: print('Invalido.')
    case _: print('Invalido.')
'''


'''
O cardápio da Lanchonete Bom Apetite é o seguinte:
Código do Lanche Especificação Preço Unitário(R$)
100 Cachorro quente 1,10
101 Bauru simples 1,30
102 Bauru c/ovo 1,50
103 Hamburger 1,10
104 Cheeseburger 1,30
105 Refrigerante 1,00
Escrever um algoritmo que leia o código do item pedido,
a quantidade e calcule o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um item. 

cod = abs(int(input('Entre com o valor de 100-105: ')))
quant = abs(int(input('Entre com a quantidade que vai pedir: ')))
if quant != 0:
    match cod:
        case 100: print(f'O {quant} Cachorros quente total:R${1.10*quant:.2f}')
        case 101: print(f'O {quant} Bauru simples total:R${1.30*quant:.2f}')
        case 102: print(f'O {quant} Bauru c/ovo total:R${1.50*quant:.2f}')
        case 103: print(f'O {quant} Hamburger total:R${1.10*quant:.2f}')
        case 104: print(f'O {quant} Cheeseburger total:R${1.30*quant:.2f}')
        case 105: print(f'O {quant} Refrigerante total:R${1.00*quant:.2f}')
else:
    print('Sem quantidade é == a sem pedidos.')
'''
