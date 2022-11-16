import os

lista = []
while True:
    escolha = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    match escolha:
        case 'i':
            item = input('Entre com o intem: ')
            lista.append(item)
            os.system('cls')
        case 'a':
            try:
                indice = abs(int(input(f'Escolha o indice 0-{len(lista)-1}: ')))
                apagou = lista.pop(indice)
                print(f'O item removido foi: {apagou}')
                os.system('cls')
            except:
                print('indice invalido.')
                continue
        case 'l':
            print('Lista: ')
            for i, item in enumerate(lista):
                print(i, item)
        case 's':
            break
        case _:
            print('Comoando invalido.')
