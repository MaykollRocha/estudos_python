"""
autor: Maykoll Rocha
email: maykoll1412@gmail.com
 Foi uma lista de 29 exercios de uma materia de laboratorio de programçao 
em C que tive e passei tudo pra python aplicando apenas conhecimentos basicos
que aprende logo no início de qualquer estudo de programação.
"""

"""
# 1. Leia dois números e escreva o maior entre eles

try:
    num1 = float(input("Entre com um numero:"))
    num2 = float(input("Entre com outro numero: "))

    if num1 > num2:
        print("O primeiro numero é mair que o segundo.")
    else:
        print("O segundo é maior que o primeiro.")
except:
    print("Algum valor invalido foi digitado.")
    
"""

"""
# 2. Leia dois números e informe se eles são iguais ou diferentes.
try:
    num1 = float(input("Entre com um numero:"))
    num2 = float(input("Entre com outro numero: "))

    if num1 == num2:
        print("Os numeros são iguais.")
    else:
        print("Os numeros são diferentes.")
except:
    print("Algum valor invalido foi digitado.")
"""

"""
# 3. Leia dois números e imprimi-los em ordem decrescente.

try:
    num1 = float(input("Entre com um numero:"))
    num2 = float(input("Entre com outro numero: "))

    if num1 > num2:
        print(num1, num2 ,sep='-' )
    else:
        print(num2 ,num1 ,sep='-' )
except:
    print("Algum valor invalido foi digitado.")

"""

"""
# 4. Dados 3 números escreva-os em ordem crescente, suponha números diferente

try:
    num1 = float(input("Entre com um numero:"))
    num2 = float(input("Entre com outro numero: "))
    num3 = float(input("Entre com outro numero: "))

    if num1 >= num2 >= num3:
        print(num3, num2, num1, sep='-')
    elif num1 >= num3 >= num2:
        print(num2, num3, num1, sep='-')
    elif num2 >= num1 >= num3:
        print(num3, num1, num2, sep='-')
    elif num2 >= num3 >= num1:
        print(num1, num3, num2, sep='-')
    elif num3 >= num1 >= num2:
        print(num2, num1, num3, sep='-')
    else:
        print(num1, num2, num3, sep='-') 
except:
    print("Algum valor invalido foi digitado.")

"""

"""
# 5. Leia 5 números e escreva o maior e o menor
# modo mais facil, porem requer mais estudo.
try:
    numeros = [float(input("Entre com um numero %i: " % (i))) 
               for i in range(0, 5)]
    print(f"O maior valor é {max(numeros)} e o menor é {min(numeros)}")
except:
    print("Entrou com um valor invalido.")

#modo com so if else e operações logicas
try:
    num1 = float(input("Entre com um numero:"))
    num2 = float(input("Entre com outro numero: "))
    num3 = float(input("Entre com outro numero: "))
    num4 = float(input("Entre com outro numero: "))
    num5 = float(input("Entre com outro numero: "))

    maior_num1 = num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5
    maior_num2 = num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5
    maior_num3 = num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5
    maior_num4 = num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5
    maior_num5 = num5 > num2 and num5 > num3 and num5 > num4 and num5 > num1

    menor_num1 = num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5
    menor_num2 = num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5
    menor_num3 = num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5
    menor_num4 = num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5
    menor_num5 = num5 < num2 and num5 < num3 and num5 < num4 and num5 < num1

    if maior_num1:
        print(f"Maior {num1}.")
    if maior_num2:
        print(f"Maior {num2}.")
    if maior_num3:
        print(f"Maior {num3}.")
    if maior_num4:
        print(f"Maior {num4}.")
    if maior_num5:
        print(f"Maior {num5}.")

    if menor_num1:
        print(f"Menor {num1}.")
    if menor_num2:
        print(f"Menor {num2}.")
    if menor_num3:
        print(f"Menor {num3}.")
    if menor_num4:
        print(f"Menor {num4}.")
    if menor_num5:
        print(f"Menor {num5}.")
except:
    print("Algum valor invalido foi digitado.")
"""

"""
# 6. Leia um número e se ele for 
# maior do que 20, então imprimir a metade do número.

try:
    num = float(input("Entre com um numero: "))
    if num > 20:
        print(f"Ele é maior que 20 e mateade dele é {num/2}.")
except:
    print("Entrou com algum valor invalido.")
"""

"""
# 7. leia um número e escreva se ele é positivo, negativo ou nulo.

try:
    num = float(input("Entre com um numero: "))
    if num>0:
        print("É positivo.")
    elif num < 0:
        print("É negativo.")
    else:
        print("É um numero nulo.")
except:
    print("Entrou com algum valor invalido.")

"""

"""
# 8. Leia um número e escreva se ele é múltiplo de 3 ou não.

try:
    num = float(input("Entre com um numero: "))
    if num%3==0:
        print("Ele é multiplo de 3.")
    else:
        print("Não é multiplo de 3.")
except:
    print("Entrou com algum valor invalido.")
"""

"""
# 9. Leia um número inteiro de 3 algarismos e escreva se o algarismo 
# da casa da centena é par ou ímpar

try:
    num = float(input("Entre com um numero de 3 algorismo: "))
    alg_centena = num//100
    if not alg_centena % 2:
        print("É um numero par.")
    else:
        print("É um numero impar.")
except:
    print("Não é um valor valido.")

"""

"""
# 10. Dada a altura e a base de 3 paredes, elaborar um algoritmo
# que escreva quantas áreas são maiores que 100 m2.

try:
    h1 = float(input("Entre com a altura 1: "))
    b1 = float(input("Entre com a base de 1: "))
    h2 = float(input("Entre com a altura 2: "))
    b2 = float(input("Entre com a base de 2: "))
    h3 = float(input("Entre com a altura 3: "))
    b3 = float(input("Entre com a base de 3: "))

    A1 = h1*b1
    A2 = h2*b2
    A3 = h3*b3

    ta = 0
    if A1 > 100:
        ta += 1

    if A2 > 100:
        ta += 1

    if A3 > 100:
        ta += 1
    print(f"Temos {ta} areas maior que 100")
except:
    print("Alguma coisa invalida foi transcrita.")
"""

"""
# 11. Elaborar um algoritmo que escreva a média final de 5 
# alunos e escreva a maior e a menor nota.

try:
    mf1 = float(input("Entre com a media final do primeiro alunos:"))
    mf2 = float(input("Entre com a media final do Segundo alunos: "))
    mf3 = float(input("Entre com a media final do Terceiro alunos: "))
    mf4 = float(input("Entre com a media final do quarto alunos: "))
    mf5 = float(input("Entre com a media final do quinto alunos: "))

    maior_mf1 = mf1 > mf2 and mf1 > mf3 and mf1 > mf4 and mf1 > mf5
    maior_mf2 = mf2 > mf1 and mf2 > mf3 and mf2 > mf4 and mf2 > mf5
    maior_mf3 = mf3 > mf1 and mf3 > mf2 and mf3 > mf4 and mf3 > mf5
    maior_mf4 = mf4 > mf1 and mf4 > mf2 and mf4 > mf3 and mf4 > mf5
    maior_mf5 = mf5 > mf2 and mf5 > mf3 and mf5 > mf4 and mf5 > mf1

    menor_mf1 = mf1 < mf2 and mf1 < mf3 and mf1 < mf4 and mf1 < mf5
    menor_mf2 = mf2 < mf1 and mf2 < mf3 and mf2 < mf4 and mf2 < mf5
    menor_mf3 = mf3 < mf1 and mf3 < mf2 and mf3 < mf4 and mf3 < mf5
    menor_mf4 = mf4 < mf1 and mf4 < mf2 and mf4 < mf3 and mf4 < mf5
    menor_mf5 = mf5 < mf2 and mf5 < mf3 and mf5 < mf4 and mf5 < mf1

    if maior_mf1:
        print(f"Maior média {mf1}.")
    if maior_mf2:
        print(f"Maior média {mf2}.")
    if maior_mf3:
        print(f"Maior média {mf3}.")
    if maior_mf4:
        print(f"Maior média {mf4}.")
    if maior_mf5:
        print(f"Maior média {mf5}.")

    if menor_mf1:
        print(f"Menor média {mf1}.")
    if menor_num2:
        print(f"Menor média {mf2}.")
    if menor_mf3:
        print(f"Menor média {mf3}.")
    if menor_mf4:
        print(f"Menor média {mf4}.")
    if menor_mf5:
        print(f"Menor média {mf5}.")
except:
    print("Algum valor invalido foi digitado.")
"""

"""
# 12. Leia um número e imprima a raiz quadrada do número caso
# ele seja positivo e o quadrado do número caso ele seja negativo.
try:
    num = float(input("Entre com um número: "))
    if num > 0:
        print(f'{num**(1/2)}')
    else:
        print(f'{num**2}')
except:
    print("Entrou com um valor errado.")
    
"""

"""
# 13. Leia um número e escreva se ele é igual a 5, a 200, a 400, se
# ele está no intervalo entre 500 e 1000 (inclusive), ou se ele está
# fora dos escopos anteriores.

try:
    num = float(input("Entre com um valor: "))
    if num == 5:
        print("Ele é igual a 5")
    elif num == 200:
        print("Ele é igual a 200")
    elif num == 400:
        print("Ele é igual a 400.")
    elif 500 < num < 1000:
        print("Ele esta entre 500 e 1000.")
    else:
        print("Ele não se encontra em nunhuma das opções acima:")
except:
    print("Entrou com algum valor invalido durante o codigo.")

"""

"""
# 14. Leia a idade de uma pessoa e escreva a sua classe eleitoral.
#   a Não eleitor: abaixo de 16 anos
#   b Eleitor Obrigatório: entre 18 e 65 anos
#   c Eleitor Facultativo: entre 16 e 18 anos e maior do que 65 anos

try:
    idade = abs(int(input("Entre com sua idade: ")))
    if idade <= 16:
        print("Não eleitor.")
    elif 18 <= idade <= 65:
        print("Eleitor Obrigatório.")
    else:
        print("Eleitor Facultativo.")
except:
    print("Entrou com algum valor errado.")

"""

"""
# 15. Leia a idade de um nadador e escreva a sua categoria 
# segundo a tabela a seguir:
#       Idade Categoria
#       5 - 7 anos Infantil A
#       8 - 10 anos Infantil B
#       11 - 13 anos Juvenil A
#       14 - 17 anos Juvenil B
#       Maiores de 18 anos Sênior

try:
    idade = abs(int(input("Entre com a idade: ")))
    if 5<=idade<=7:
        print("Infantil A.")
    elif 8<=idade<=10:
        print("Infantil B.")
    elif 11<=idade<=13:
        print("Juvenil A.")
    elif 14<=idade<=17:
        print("Juvenil B.")
    elif idade>=18:
        print("Senior.")
    else:
        print("Não tem idade pra jogar.")
    
except:
    print("Entrou com algum valor invalido.")

"""

"""
# 16. Leia o nome, o sexo e a idade de uma pessoa. Se a pessoa for do sexo
# feminino e tiver menos de 25 anos, escreva o nome e a mensagem “ACEITA”.
# Caso contrário imprimir a mensagem “NÃO ACEITA”
try:
    nome = input("Entre com seu nome: ")
    sexo = input("Entre com M para masculino e F para feminino: ")
    sexo = sexo.capitalize()
    idade = abs(int(input("Entre com a sua idade: ")))

    if sexo[0] == 'F' and idade < 25:
        print("Aceita.")
    else:
        print("Não aceita.")

except:
    print("Entrou com algum dado errado.")
"""

""" 
# 17. Uma empresa paga à sua funcionária R$30,00 por hora, se ela trabalha
# 40 horas ou menos durante a semana. Se ela trabalha mais de 40 horas, 
# ela recebe R$50,00 por horas extras trabalhadas. Elabore um algoritmo 
# que dado o nome e o número de horas trabalhadas pela funcionária,
# forneça o salário semanal.
try:
    nome = input("Entre com o nome do funcinario: ")
    hora_trabalhadas = abs(int(input("Entre quanta horas trabalhou: ")))

    if hora_trabalhadas > 40:
        horas_extra = hora_trabalhadas - 40
        salario_semanal = 40*30 + horas_extra*50
    else:
        salario_semanal = hora_trabalhadas*30

    print(f'O salário de {nome.capitalize()} é de R${salario_semanal:.2f}')
except:
    print("Entrada de algum dado errada.")
"""

"""
# 18. Leia o salário bruto de um funcionário e o valor da prestação e 
# informe se o empréstimo pode ou não ser concedido. O valor máximo
# da prestação não pode ultrapassar 30% do salário bruto.

try:
    salario_bruto = abs(float(input("Entre com o seu salário Bruto: ")))
    valor_do_emprestimo = abs(float(input("Entre com o seu Emprestimo: ")))

    if valor_do_emprestimo < salario_bruto*0.3:
        print("O emprestimo é valido.")
    else:
        print("Emprestimo invalido.")

except:
    print("Entrada de algum valor invalido.")

"""

"""
# 19. Leia os pontos obtidos por 3 jogadores de uma equipe e escreva esses 
# valores em ordem decrescente. Além disso, se a soma dos pontos for 
# maior do que 100, escreva a média aritmética dos pontos; senão, 
# escreva a mensagem “Equipe desclassificada”.

try:
    p1 = abs(float(input("Entre com os pontos do primeiro jogado: ")))
    p2 = abs(float(input("Entre com os pontos do segundo jogado: ")))
    p3 = abs(float(input("Entre com os pontos do terceiro jogado: ")))

    if p1 >= p2 >= p3:
        print(p1, p2, p3, sep='-')
    elif p1 >= p3 >= p2:
        print(p1, p3, p2, sep='-')
    elif p2 >= p1 >= p3:
        print(p2, p1, p3, sep='-')
    elif p2 >= p3 >= p1:
        print(p2, p3, p1, sep='-')
    elif p3 >= p1 >= p2:
        print(p3, p1, p2, sep='-')
    else:
        print(p3, p2, p1, sep='-')

    if (p1+p2+p3) >= 100:
        print(f"A media de pontos é de {(p1+p2+p3)/3:.2f}")
    else:
        print("Equipe ELIMINADA")
except:
    print("Entrada dados errados.")

"""

"""
# 20. Sabendo que um carro do tipo A faz 12 Km com um litro de gasolina, 
# um carro do tipo B faz 9 Km e um do tipo C faz 8 Km, faça um algoritmo
# que leia o percurso em quilômetros, o tipo do carro e informe o 
# consumo estimado de combustível.

try:
    km_percursar = abs(int(input("Quntos KM vai ser percorrido: ")))
    tipo_carro = input("Entre com a letra do tipo do carro: ")
    if tipo_carro.capitalize() == 'A':
        print(f"Consumo estimado de {km_percursar/12}L")
    elif tipo_carro.capitalize() == 'B':
        print(f"Consumo estimado de {km_percursar/9}L")
    else:
        print(f"Consumo estimado de {km_percursar/8}L")
except:
    print("Entrou com o numero errado.")
"""

"""
# 21. O peso ideal de uma pessoa está relacionado com o a altura e sexo
# de uma pessoa. Preparar um algoritmo que leia a altura e o 
# sexo de uma pessoa e escreva o seu peso ideal utilizando as
# seguintes fórmulas:
# M para homens: (72.7 * altura) - 58
# F para mulheres: (62.1 * altura) -44.7

try:
    altura = abs(float(input('Entre com sua altura: ')))
    sexo = input('Entre com M para masculino e F para feminino: ')
    if sexo.capitalize() == 'M':
        print("Seu peso ideal é de", (72.7 * altura) - 58)
    elif sexo.capitalize() == 'F':
        print("Seu peso ideal é de", (62.1 * altura) - 44.7)
    else:
        print("Talvez tenha digitado o sexo biologico errado.")

except:
    print("Entrou com algum dado errado.")

"""

"""
# 22. Para um grupo de 3 pessoas, o supermercado resolveu fazer a 
# seguinte promoção:
#        Compras > R$150 ,00 e <= R$300,00 : desconto de 10%
#        Compras > R$300,00 e <= R$500,00 : desconto de 15%
#        Compras > R$500,00: desconto de 18%.
# Calcule e exiba o total em dinheiro dado em descontos pelo Supermercado.

try:
    pessoa1 = abs(float(input("Entre com o valor da compra: ")))
    pessoa2 = abs(float(input("Entre com o valor da compra: ")))
    pessoa3 = abs(float(input("Entre com o valor da compra: ")))
    descont = 0
    if 150 < pessoa1 <= 300:
        descont += pessoa1*0.10
    elif 300 < pessoa1 <= 500:
        descont += pessoa1*0.15
    elif pessoa1 >500:
        descont += pessoa1*0.18

    if 150 < pessoa2 <= 300:
        descont += pessoa2*0.10
    elif 300 < pessoa2 <= 500:
        descont += pessoa2*0.15
    elif pessoa2 >500:
        descont += pessoa2*0.18

    if 150 < pessoa3 <= 300:
        descont += pessoa3*0.10
    elif 300 < pessoa3 <= 500:
        descont += pessoa3*0.15
    elif pessoa3 >500:
        descont += pessoa3*0.18

    print(f"O desconto total foi de R${descont:.2f}")
except:
    print("Entrou com algum dado no local ou do tipo errado.")
"""

"""
# 23. Um comerciante comprou um produto e quer vendê-lo com um lucro de 
# 45% se o valor da compra for menor do que R$20,00, caso contrário o
# lucro será de 30%. Faça um algoritmo que leia o valor do produto 
# e escreva o valor de venda.

try:
    valor = abs(float(input('Valor do produto: ')))

    if valor < 20:
        print(f'Valor de venda sera de R${valor*1.45:.2f}.')
    else:
        print(f'Valor de venda sera de R${valor*1.3:.2f}.')
except:
    print("Entrou com algum dado no local ou do tipo errado.")

"""

"""
# 24. Um comerciante calcula o valor da venda de produtos tendo 
# em vista a tabela a seguir:
#       VALOR DA COMPRA VALOR DA VENDA
#       Menor que R$10,00 Lucro de 70%
#       Entre R$10,00 e R$30,00 Lucro de 50%
#       Entre R$30,00 e R$50,00 Lucro de 40%
#       Maior que R$50,00 Lucro de 30%

try:
    valor = abs(float(input('Valor do produto: ')))

    if valor < 10:
        print(f'Valor de venda sera de R${valor*1.7:.2f}.')
    elif 10 <= valor < 30:
        print(f'Valor de venda sera de R${valor*1.5:.2f}.')
    elif 30 <= valor < 50:
        print(f'Valor de venda sera de R${valor*1.4:.2f}.')
    else:
        print(f'Valor de venda sera de R${valor*1.3:.2f}.')
except:
    print("Entrou com algum dado no local ou do tipo errado.")
"""

"""
# 25.Elaborar um algoritmo que possa entrar com o nome do produto
# e o valor da compra e imprima o nome do produto e o valor da venda.
# OBS: no exercício não fala nem mostra uma tabela como devemos apresentar
# o valor de venda então usei a do exercício anterior.

try:
    nome = input("Entre com o nome do produto: ").capitalize()
    valor = abs(float(input('Valor do produto: ')))

    if valor < 10:
        print(f'O produto {nome} de venda sera de R${valor*1.7:.2f}.')
    elif 10 <= valor < 30:
        print(f'O produto {nome} de venda sera de R${valor*1.5:.2f}.')
    elif 30 <= valor < 50:
        print(f'O produto {nome} de venda sera de R${valor*1.4:.2f}.')
    else:
        print(f'O produto {nome} de venda sera de R${valor*1.3:.2f}.')
except:
    print("Entrou com algum dado no local ou do tipo errado.")

"""

"""
# 26. Leia três números e escreva o maior, o intermediário e o menor

try:
    n1 = abs(float(input("Entre com o valor: ")))
    n2 = abs(float(input("Entre com o valor: ")))
    n3 = abs(float(input("Entre com o valor: ")))

    if n1 < n2 < n3:
        print(f"Mair{n3} menor{n1} intermediario{n2}.")
    elif n2 < n3 < n1:
        print(f"Mair{n1} menor{n2} intermediario{n3}.")
    elif n3 < n1 < n2:
        print(f"Mair{n2} menor{n3} intermediario{n1}.")
    elif n1 < n3 < n2:
        print(f"Mair{n2} menor{n1} intermediario{n3}.")
    elif n2 < n1 < n3:
        print(f"Mair{n3} menor{n2} intermediario{n1}.")
    elif n3 < n2 < n1:
        print(f"Mair{n1} menor{n3} intermediario{n2}.")
except:
    print("Algo esta errado meu caro.")

"""

"""
# 27. Dados 3 lados de um triângulo, elaborar um algoritmo que 
# determine se o triângulo é eqüilátero, isósceles ou escaleno.
#    Eqüilátero: tem os 3 lados iguais
#    Isósceles: tem 2 lados iguais
#    Escaleno: os 3 lados são diferentes.

try:
    l1 = abs(float(input("Entre com o lado do triangulo: ")))
    l2 = abs(float(input("Entre com o lado do triangulo: ")))
    l3 = abs(float(input("Entre com o lado do triangulo: ")))

    if l1 == l2 == l3:
        print("Triangulo equilatero.")
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print("Triangulo Isoceles.")
    else:
        print("Triangulo escaleno.")
except:
    print("Algum dado informado esta errado.")

"""

"""
#Calcule o imposto de renda a ser pago pelo contribuinte, dada as seguintes 
# informações de entrada:   
#    Nome e CPF do Contribuinte;
#    Renda Bruta do Contribuinte;  
#    Número de dependentes do contribuinte;
#    Imposto de Renda Retido na Fonte.    
# De acordo com estes dados são calculados:
# O desconto com dependentes (para cada dependente, abate-se R$2.000,00)
# O valor da alíquota obedece a seguinte tabela:
#       Renda Líquida Anual Alíquota
#       Até R$50.000,00 Isento
#       De R$50.0001,00 até R$100.000,00 10%
#       Acima de R$100.000,00 20%
# Basicamente o programa deverá realizar as seguintes tarefas:
# Ler os dados do contribuinte;
# Calcular o imposto:
#   a. Calcular a Renda Líquida abatendo da renda bruta o desconto
#       com os dependentes,
#   b. Com a Renda Líquida identificar o percentual da alíquota e 
#       calcular o valor do imposto,
#   c. Calcular o valor do imposto a ser pago ou a receber, deduzindo
#       o imposto retido na fonte.
# Escrever os dados fornecidos e calculados, identifique se o 
# imposto é a pagar ou a receber
# obs: a parte do imposto retido na fonte não entendi como não sei muito de lei
# e mesmo pesquisando não consegui compreender essa parte.

try:
    nome = input("Entre com o nome do contribuinte: ")
    cpf = input("Entre com o CPF do contribuinte: ")
    renda_bruta = abs(float(input("Entre com a renda bruta: ")))
    n_dependentes = abs(int(input("Numero de dependentes: ")))
    imps_renda_retido = abs(float(input("Entre com a imposto de renda: ")))

    renda_liquida = renda_bruta - n_dependentes*2000
    aliquota = 0
    if renda_liquida > 50000:
        print("O valor a sera isento")
    elif 50001<= renda_liquida <100000:
        print(f'O valor ser de {renda_liquida*0.1}')
    else:
        print(f'O valor ser de {renda_liquida*0.2}')
except:
    print("Algum dado informado deu erro no programa.")

"""

"""
# 29. O banco BE concederá um crédito especial com juros de 2% aos seus 
# clientes de acordo com o saldo médio no último ano. Fazer um algoritmo
# que leia o saldo médio de um cliente e calcule o valor do crédito de
# acordo com a tabela abaixo. Imprimir uma mensagem informando o saldo
# médio e o valor do crédito.
#       Saldo Médio             Percentual 
#       de 0 a 500,00           Nenhum crédito
#       de 501,00 a 1000,00     30% do valor do saldo médio
#       de 1001,00 a 3000,00    40% do valor do saldo médio
#       acima de 3001           50% do valor do saldo médio


try:
    sal_m = abs(float(input("Entre com o saláeio médio: ")))

    if sal_m <+500:
        print(f"O salario médio é de R${sal_m} não tem crédito pra você.")
    elif 500<sal_m<=1000:
        print(f"O salario médio é de R${sal_m} Credito especial de R${sal_m*0.3}.")
    elif 1000<sal_m<=3000:
        print(f"O salario médio é de R${sal_m} Credito especial de R${sal_m*0.4}.")
    else:
        print(f"O salario médio é de R${sal_m} Credito especial de R${sal_m*0.5}.")
except:
    print("Algum dado foi informado errado.")   

"""
