primeiro_valor = int(input("Entre com o primeiro valor: "))
segundo_valor = int(input("Entre com o segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior',
          f'que o segundo {segundo_valor}.', sep=' ')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor {segundo_valor} é maior que',
          f'o primeiro {primeiro_valor}.', sep=' ')
else:
    print(f'O segundo valor {segundo_valor} é igual ao primeiro.')
