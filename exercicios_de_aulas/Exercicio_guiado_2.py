ultima_solução = None
num1 = 0
num2 = 0
op = ''

while True:
    print('--MENU--\n + Soma\n - Subtração\n *Multiplicação\n / Divisão\n'
          'S-sair')

    if ultima_solução != None:
        print(f'Ultimo calculo:{num1} {op} {num2} = {ultima_solução}')

    op = input('Entre com a operação que quer fazer: ')

    if op.capitalize() == 'S':
        break

    if op == '+' or op == '-' or op == '*' or op == '/':
        try:
            num1 = float(input('Entre com o primeiro valor: '))
            num2 = float(input('Entre com o segundo valor: '))
        except:
            print('Digitou um não valor.')
            continue

    if op == '+':
        ultima_solução = num1 + num2
    elif op == '-':
        ultima_solução = num1 - num2
    elif op == '*':
        ultima_solução = num1*num2
    elif op == '/':
        ultima_solução = num1/num2
    else:
        print('Operador invalido.')
        ultima_solução = None
