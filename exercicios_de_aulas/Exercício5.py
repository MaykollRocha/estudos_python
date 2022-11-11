"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numero_int = input("Entre com um número inteiro: ")
if numero_int.isdigit():
    convet = int(numero_int)
    if convet % 2 == 0:
        print(f"O numero {convet} é par.")
    else:
        print(f"O numero {convet} não é par.")
else:
    print("Não é um numero Real.")

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

horas = input("Que horas são? ")


if horas.isdigit():
    horas = abs(int(horas))
    if horas >= 0 and horas <= 23:
        if horas >= 0 and horas <= 11:
            print("Bom dia.")
        elif horas >= 12 and horas <= 17:
            print("Boa tarde.")
        else:
            print("Boa noite.")
    else:
        print("Não é um valor valido pra horas.")
else:
    print("Não é horas.")

"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

first_name = input("Entre com seu primeiro nome: ")
num_letras = len(first_name)

if num_letras <= 4:
    print("Seu nome é muito curto.")
elif num_letras >= 5 and num_letras <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

"""
