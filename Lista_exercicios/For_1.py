'''
nome: Maykoll Rocha
dia: 12/11/2022
Obs: Era uma lista de exercícios de C porem fiz para treinar python e veja no
que deu.
'''


'''
1. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: 1 + 2 + 3 + 4 +... + n.

n = abs(int(input('Entre com um número inteiro: ')))

for i in range(1, n+1, 1):
    print('+', i, end=' ')
    
'''

'''
2. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: -1 -2 -3 - 4 -... - n.

n = abs(int(input('Entre com um número inteiro: ')))

for i in range(1, n+1, 1):
    print(i*-1, end=' ')
    
'''

'''
3. Faça um programa que peça um número inteiro n do usuário e calcule a
seguinte expressão: 1 -2 +3 - 4 +... - n

n = abs(int(input('Entre com um número inteiro: ')))

for i in range(1, n+1, 1):
    if not i % 2:
        print(i*-1, end=' ')
    else:
        print('+', i, end=' ')
        
'''

'''
4. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: -1 +2 -3 +4 -... +n.

n = abs(int(input('Entre com um número inteiro: ')))
for i in range(1, n+1, 1):
    if i % 2:
        print(i*-1, end=' ')
    else:
        print('+', i, end=' ')
        
'''

'''
5. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: 1 + 3 + 5 + 7 +... + n.

n = abs(int(input('Entre com um número inteiro: ')))

for i in range(1, n+1, 2):
    print('+', i, end=' ')
    
'''

'''
6. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: 1 - 3 + 5 - 7 +... - n.

n = abs(int(input('Entre com um número inteiro: ')))
t = 0 #uso pra trocar pq um é positivo outro é negativo porem todos são impars
for i in range(1, n+1, 2):
    if t == 0:
        print('+', i, end=' ')
        t = 1
    else:
        print(i*-1, end=' ')
        t = 0
'''

'''
7. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: 1 + 5 + 9 + 13 +... + n.

n = abs(int(input('Entre com um número inteiro: ')))
t = 0
for i in range(1, n+1, 4):
    print('+', i, end=' ')
    
'''

'''
8. Faça um programa que peça um número inteiro n do usuário e calcule a 
seguinte expressão: -1 - 5 - 9 - 13 -... - n.

n = abs(int(input('Entre com um número inteiro: ')))
t = 0
for i in range(1, n+1, 4):
    print( i*-1, end=' ')
    
'''

'''
9. Faça um programa que peça um número inteiro n do usuário e calcule a seguinte 
expressão: 1 + 11 + 21 + 31 +... + n

n = abs(int(input('Entre com um número inteiro: ')))
t = 0
for i in range(1, n+1, 10):
    print('+', i, end=' ')
    
'''

'''
10. Faça um programa que peça dois números inteiros do usuário, n e dif. A 
partir desses números o seu programa calcula a seguinte expressão:
1 + (1 + dif) + (1 + 2*dif) + (1+3*dif) + (1+4*dif)... + (1+n*dif).

n = abs(int(input('Entre com o números de passos: ')))
dif = abs(int(input('Entre com o valor que sera usado pra multiplicar: ')))
for i in range(0, n+1, 1):
    print(1 + i*dif, '+', end=' ')
    
'''


'''
11. Faça um programa que peça um número inteiro n do usuário. A partir desse 
número o seu programa calcula a soma de 
n termos3^2: 3^2+ 3^2+ 3^2+ ... + 3^2

n = abs(int(input('Entre com o números de passos: ')))
soma = 0
for i in range(1, n+1, 1):
    soma += 3**2

print('A soma dos n termos sera ', soma)
'''

'''
12. Faça um programa que peça um número inteiro n do usuário. A partir desse número o 
seu programa calcula a soma de 
n termos 5^2: 5^2+ 5^2 + 5^2+ ... + 5^2

n = abs(int(input('Entre com o números de passos: ')))
soma = 0
for i in range(1, n+1, 1):
    soma += 5**2

print('A soma dos n termos sera ', soma)

'''

'''
13. Faça um programa que peça um número inteiro n do usuário. A partir desse 
número o seu programa calcula a soma de n termos 
5^3: 5^3+ 5^3+ 5^3+ ... + 5^3

n = abs(int(input('Entre com o números de passos: ')))
soma = 0
for i in range(1, n+1, 1):
    soma += 5**3

print('A soma dos n termos sera ', soma)

'''

'''
14. Faça um programa que peça um número inteiro n do usuário. A partir desse
número o seu programa calcula a soma de n termos 2^3: 2^3+ 2^3+ 2^3+ ... + 2^3

n = abs(int(input('Entre com o números de passos: ')))
soma = 0
for i in range(1, n+1, 1):
    soma += 2**3

print('A soma dos n termos sera ', soma)

'''

'''
15. Faça um programa que peça dois números inteiros do usuário, n e exp. A
partir desses números o seu programa calcula a soma de
n termos 3^exp: 3^exp + 3^exp + 3^exp + ... + 3^exp

n = abs(int(input('Entre com o números de passos: ')))
exp = abs(int(input('Entre com o valor do expoente: ')))
soma = 0
for i in range(1, n+1, 1):
    soma += 3**exp

print('A soma dos n termos sera ', soma)


'''

'''
16. Faça um programa que peça dois números inteiros do usuário, n e expoente.
A partir desses números o seu programa calcula a soma de n termos 
5^exp: 5^exp + 5^exp + 5^exp + ... + 5^exp.

n = abs(int(input('Entre com o números de passos: ')))
exp = abs(int(input('Entre com o valor do expoente: ')))
soma = 0
for i in range(n+1):
    soma += 5**exp

print('A soma dos n termos sera ', soma)

'''

'''
17. Faça um programa que peça dois números inteiros do usuário, n e exp. 
A partir desses números o seu programa calcula a soma de n termos 
2exp: 2exp + 2exp + 2exp + ... + 2exp.

n = abs(int(input('Entre com o números de passos: ')))
exp = abs(int(input('Entre com o valor do expoente: ')))
soma = 0
for i in range(n+1):
    soma += 2**exp

print('A soma dos n termos sera ', soma)

'''

'''
18. Faça um programa que peça dois números inteiros do usuário, n e exp. A partir
desses números o seu programa calcula a soma de n termos 22exp: 22exp + 22exp 
+ 22exp +... + 22exp.

n = abs(int(input('Entre com o números de passos: ')))
exp = abs(int(input('Entre com o valor do expoente: ')))
soma = 0
for i in range(n+1):
    soma += 2**(2*exp)

print('A soma dos n termos sera ', soma)

'''


'''
19. Faça um programa que peça três números inteiros do usuário, n, exp e base.
A partir desses números o seu programa calcula a soma de n termos baseexp: 
baseexp + baseexp + baseexp + ... + baseexp +.

n = abs(int(input('Entre com o números de passos: ')))
exp = abs(int(input('Entre com o valor do expoente: ')))
base = abs(int(input('Entre com o valor da base: ')))
soma = 0
for i in range(n):
    soma += base**exp

print('A soma dos n termos sera ', soma)

'''

'''
20. Faça um programa que leia um número inteiro n do usuário e imprima na tela a seguinte 
seqüência: n n-1 n-2 ...1

n = abs(int(input('Entre com um numero: ')))

for i in range (0, n):
    print(n-i, end=' ')
    
'''

'''
21. Faça um programa que leia um número inteiro n do usuário e imprima na tela
a seguinte seqüência: 1^2 2^2 3^2 4^2 ... n^2

n = abs(int(input('Entre com um numero: ')))

for i in range(1, n):
    print(i**2, end=' ')
    
'''

'''
22. Faça um programa que leia um número inteiro n do usuário e imprima na tela a seguinte 
seqüência: 1^3 2^3 3^3 4^3 ... n^3

n = abs(int(input('Entre com um numero: ')))
for i in range(1, n+1):
    print(i**3, end=' ')   
    
'''

'''
23. Faça um programa que peça um número inteiro n do usuário e calcule o 
fatorial de n.

n = abs(int(input('Entre com um numero: ')))
fat = 1
for i in range(0, n):
    fat *= (n-i)
print(fat)

'''

'''
24. Faça um programa que peça um número inteiro n do usuário e calcule 
a seguinte expressão: 1 * 3 * 5 * 7 * 9 * ... * n

n = abs(int(input('Entre com o valor de n: ')))
calc = 1
for i in range(1, n+1, 2):
    calc *= i

print(calc)

'''

'''
25. Faça um programa que peça um número inteiro n do usuário e imprima na tela a 
seguinte seqüência:: 1 3 5 7 9 ... n

n = abs(int(input('Entre com o valor de n: ')))
for i in range(1, n+1, 2):
    print(i, end = ' ')
    
'''

'''
26. Faça um programa que peça um número inteiro n do usuário e imprima na tela a 
seguinte seqüência: 1 4 7 10 13 ... n

n = abs(int(input('Entre com o valor de n: ')))
for i in range(1, n+1, 3):
    print(i, end=' ')
    
'''

'''
27. Faça um programa que peça um número inteiro n do usuário e calcule
a seguinte soma: 1 + 2 + 4 + 8 + ... + n. em C seria mais facil como to 
em python meu range não pode respeitar esse metodo de calculo aritmédico ele
ele é apenas geometrico.

n = abs(int(input('Entre com o valor de n: ')))
aux = 1  # para respeita o movimento que ele faz usei uma auxiliar an+1 = an*2
soma = 0
for i in range(n+1):
    if aux == i:
        soma += i
        aux = i*2

print(soma)
'''

'''
28.Faça um programa que peça um número inteiro n do usuário e calcule 
a seguinte soma: 1 + 4 + 16 + 64 + ... + n.

n = abs(int(input('Entre com o valor de n: ')))
aux = 1
soma = 0
for i in range(n+1):
    if aux == i:
        soma += i
        aux = i*4

print(soma)
'''

'''
29. Faça um programa que peça um número inteiro n do usuário e imprima na tela a 
seguinte seqüência: 1 2 4 8 ... n

n = abs(int(input('Entre com o valor de n: ')))
aux = 1
for i in range(n+1):
    if aux == i:
        print(i, end=' ')
        aux = i*2
'''

'''
30. Faça um programa que peça um número inteiro n do usuário e calcule o seguinte 
produto: 1 * 2 * 4 * 8 * ... * n

n = abs(int(input('Entre com o valor de n: ')))
aux = 1 #concertar o passo ja que meu range estra em 1~n
mult = 1
for i in range(1,n+1):
    if aux == i:
        mult *= i
        aux = i*2
    
print(mult)
'''

'''
31. Faça um programa que peça um número inteiro n do usuário e calcule a seguinte 
expressão: 1^2* 3^2* 5^2* 7^2* 9^2* ... * n^2

n = abs(int(input('Entre com o valor de n: ')))
mult = 1
for i in range(1, n+1, 2):
    mult *= (i**2)
print(mult)
'''

'''
32. Faça um programa que peça um número inteiro n do usuário e calcule a
seguinte expressão: 1^2- 3^2+ 5^2- 7^2+ 9^2- ... + n^2.

n = abs(int(input('Entre com o valor de n: ')))
calc = 0
troca = 1
for i in range(1, n+1, 2):
    if troca:
        calc += (i**2)
        troca = 0
    else:
        calc -= (i**2)
        troca = 1
print(calc)

'''

'''
33. Faça um programa que leia 3 números inteiros do usuário, n, dif e exp.
A partir deles, calcula a seguinte expressão:
1exp– (1+dif)exp + (1+2*dif)exp– (1+3*dif)exp+ (1+4*dif)exp- ... + (1+n*dif)exp.

n = abs(int(input('Entre com o números de passos: ')))
dif = abs(int(input('Entre com o valor que sera usado pra multiplicar: ')))
exp = abs(int(input('Entre com o valor que sera usado pra exponencial: ')))
soma = 0
troca = 1
for i in range(n+1):
    if troca:
        soma += (1 + i*dif)**exp
        troca = 0
    else:
        soma -= (1 + i*dif)**exp
        troca = 1

    print((1 + i*dif)**exp)

print(soma)

'''

'''
34. Faça um programa que leia uma seqüência de n números inteiros do usuário 
e imprima na tela o comprimento da maior subseqüência crescente existente nessa
seqüência. 
Ex. de uma seqüência: 1 5 7 -1 4 2 8 9 11 13 15 1 5 3
No exemplo há 5 subseqüências crescentes: (1, 5, 7); (-1, 4);
(2, 8, 9, 11, 13, 15); (1, 5); (3). E o comprimento da maior subseqüência 
crescente existente é igual a 6: (2, 8, 9, 11, 13, 15).

n = abs(int(input('Quantos numeros serão digitados:')))
maior_sec = ''  # registrei em string nossa sequencia
sec_atual = ''  # a ultima sequencia pega durante a programação
ultimo_valor_sec = -999  # o ultimo valor pra ver se vou começar uma nova seq
for i in range(1, n+1):
    num = int(input('Entre com um Numero: '))
    if ultimo_valor_sec > num:
        if len(maior_sec) < len(sec_atual):
            maior_sec = sec_atual

        sec_atual = f'{num}, '
        ultimo_valor_sec = num
    else:
        sec_atual += f'{num}, '
        ultimo_valor_sec = num

if len(maior_sec) < len(sec_atual):
    maior_sec = sec_atual

print(maior_sec)

'''


'''
Faça um programa que peça ao usuário um número inteiro n qualquer e imprima na tela 
a seguinte figura composta por asteriscos:
Ex. para n = 4: Ex. para n = 2:
   *
  ***
 ***** 
*******

n = abs(int(input('Entre com o tamanho da arvore: ')))
for i in range(1, n*2, 2):
    ast = '*'*i
    print(f'{ast: ^50}')

'''

'''
36. Faça um programa que peça ao usuário um número inteiro n qualquer e calcule 
o número de fibonacci n, lembrando que o fibonacci de um número é definido da 
seguinte maneira:
fib(n) = fib(n-1) + fib(n-2)
fib(1) = 1
fib(0) = 0

n = abs(int(input('Entre com o tamanho da arvore: ')))
an_1 = 0
an_2 = 1
for i in range(n-2):
    an_3 = an_1 + an_2 
    an_1 = an_2
    an_2 = an_3

print(f'O valor {an_3} pertece ao n = {n}')    
'''

'''
37. Faça um programa que peça ao usuário um número inteiro n qualquer e imprima
na tela a seqüência de fibonacci de 0 até n (ou o 1º inteiro menor que n que
pertencer à seqüência de fibonacci). Ex.: para n = 15 a seqüência que o seu 
programa deve imprimir será 0 1 1 2 3 5 8 13
n = abs(int(input('Entre com o valor ate onde quer ir: ')))
an_1 = 0
an_2 = 1
for i in range(n-2):
    an_3 = an_1 + an_2
    if an_3 > n:
        break
    print(an_3, end=' ')
    an_1 = an_2
    an_2 = an_3

'''

'''
38. Faça um programa que leia do usuário um número inteiro x qualquer e calcule as 
seguintes somatórias:
É MUITA FORMULA VAI TER UM IMG.PNG NO REPOSITORIO SO PRA ISSO.

A.

for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem {((-1)**(n+1))*(1/(2*n)) :.3f}')
    respf += ((-1)**(n+1))*(1/(2*n))
print(f'Resposta final {respf}')
    
B.

for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem {((-1)**(n+1))*(1/(n**2)) :.3f}')
    respf += ((-1)**(n+1))*(1/(n**2))
print(f'Resposta final {respf}')   
C.

for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem {((-1)**n)*(1/(n**2 + 1)) :.3f}')
    respf += ((-1)**n)*(1/(n**2 + 1))
print(f'Resposta final {respf}')   
D.

for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem {((-1)**(n+1))*(4/(3*n - 2)) :.3f}')
    respf += ((-1)**(n+1))*(4/(3*n - 2))
print(f'Resposta final {respf}')    
E.

for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem'
          f' {((-1)**(n+1))*((n**2)/(n**3 + 2)) :.3f}')
    respf += ((-1)**(n+1))*((n**2)/(n**3 + 2))
print(f'Resposta final {respf}')          

F.

calc1 = 1
calc2 = 1
for n in range(1, x+1):
    for p in range(1, n+1):
        calc1 *= 2*p - 1

    for p in range(1, n+1):
        calc2 *= 3*p - 2
    print(f'Para n = {n} na somatoria tem {calc1/calc2 :.3f}')
    respf += calc1/calc2
    calc2 = calc1 = 1
print(f'Resposta final {respf :.2f}')

G.
for n in range(1, x+1):
    print(f'Para n = {n} na somatoria tem'
          f' {((-1)**(n-1))*(1/((n + 1)**(3/4))) :.3f}')
    respf += ((-1)**(n-1))*(1/((n + 1)**(3/4)))

print(f'Resposta final {respf :.2f}')

H.
x = abs(int(input('Entre com um valor x qualquer para somatoria: ')))
respf = 0
fat = 1
for n in range(1, x+1):
    for p in range(1, n+1):
        fat *= p

    print(f'Para n = {n} na somatoria tem {((-1)**n)*(fat/n) :.3f}')
    respf += ((-1)**n)*(fat/n)
    fat = 1
print(f'Resposta final {respf :.2f}')
'''
