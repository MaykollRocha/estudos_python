import sys

# Supoha uma entrada assim como ele é escrito.
cpf_compact = input('Entre com o CPF: ')
cpf = ''  # axiliar para ter fora da compacta
for i in cpf_compact:  # pego cada indice
    if i.isdigit():  # checo se é um digito ele retor 1
        cpf += i     # se não 0 assum tira '.' e o '-'

if cpf[0]*len(cpf) == cpf:
    print('Ele digitou tudo igual.')
    sys.exit()

# Para o primeiro digito pega os os 9 primeiros digitos e multiplica
# valor pra multiplicar: 10  9  8  7  6  5  4  3  2
# indicies dos digitod :  0  1  2  3  4  5  6  7  8
# multiplica pelo valor que ta no indice na variavel CPF

# i é o indice e r é meu multiplicardor gerado pelo range de 10 a 2
for i, mult in enumerate(range(10, 1, -1)):
    soma = mult*int(cpf[i]) if not i else soma + mult*int(cpf[i])
    # Usei uma operação ternaria onde no i = 0 primeiro indice ela so coloca o
    # valor da variavel e nos outros ela pega a variavel e soma com a multiplicaçaõ

soma *= 10  # multiplica por 10
soma %= 11  # modulo de 11
# novamente com o operador ternario se deu > 9 ela vira 0 o primeiro se não deixa 7
resultado_primeiro_digt = 0 if soma > 9 else soma

# Para o segundo digito pega os os 10 primeiros digitos e multiplica
# valor pra multiplicar: 11 10  9  8  7  6  5  4  3  2
# indicies dos digitod :  0  1  2  3  4  5  6  7  8  9
# multiplica pelo valor que ta no indice na variavel CPF
# segue a mesma ladinha do anteior adicionadno o ultimo digito

for i, mult in enumerate(range(11, 1, -1)):
    soma = mult*int(cpf[i]) if not i else soma + mult*int(cpf[i])

soma *= 10
soma %= 11

resultado_segundo_digt = 0 if soma > 9 else soma

# valido os 2 ultimo digitos é igual ao resultado da minha soma
valido = (resultado_primeiro_digt*10 + resultado_segundo_digt) == int(cpf[9:11])

# e pronto se for True é certo se for False ta errado o CPF
if valido:
    print(f'O cpf {cpf_compact} é valido. ')
else:
    print('É falso.')
