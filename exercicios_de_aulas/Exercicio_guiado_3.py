texto = 'Ah o amor... que nasce não'\
        'sei onde, vem não sei como, e dói não sei porquê.'

# cont = 0
# letra_proc = input('Entre com a letra que quer ver: ')
# cont_letra = 0
#
# while cont < len(texto):
#      if texto[cont].upper() == letra_proc.capitalize():
#         cont_letra += 1
#
#     cont += 1
#
# print(f'A letra {letra_proc} apareceu {cont_letra}X.')

i = 0
mais_aparec = ''
quant_x = 0

while i < len(texto):
    letra = texto[i]
    quant = texto.count(letra)
    i += 1
    if letra == ' ':
        continue

    if quant > quant_x:
        mais_aparec = letra
        quant_x = quant

print(f'A letra {mais_aparec} apareceu {quant_x}X.')
