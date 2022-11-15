"""
#Exercício 1:

def seqNumeros():
    for i in range(1,21):
        if i%2==0:
            print("%i é par meu cosagrado."%(i))
"""

"""
#Exercício 2:

def stringMaiuscula(txt):
    return txt.upper()

txt = input("Entre com a string: ")
txt = stringMaiuscula(txt)

print(txt)
"""

"""
#Exercício 3:

def adicinaLista(list):
    list.append(5)
    list.append(6)

list_lista = [1,2,3,4]
adicinaLista(list_lista)
print(list_lista)

"""

"""
#Exercício 4:

def printArg(arq,*lista_arg):
    print(arq)
    
    for i in lista_arg:
        print(i)
        
printArg("oi bonote","Tu é gostosa demais")
"""

"""
#Exercício 5:

a = int(input("Entre com os valores de : "))
b = int(input("Entre com os valores de : "))
x = lambda a,b: a+b
print(x(a,b))

"""


"""
#Exercício 6:

total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)#mostra 30 pq o total local tem prioridade aqui dentro
    return total;

soma( 10, 20 );
print ("Fora da função o total é: ", total)#retorna 0 pq o total global não muda
"""

"""
#Exercio 7:

Celsius = [39.2, 36.5, 37.3, 37.8,0]
Fahrenheit = map(lambda Celsius: Celsius*9/4 +32,Celsius)
print (list(Fahrenheit))

"""

"""
#Exercício 8:
print(dir(dict))

"""
"""
# Exercício 9


"""
import pandas as pd
print(dir(pd))

import pandas as pd
file_name = "binary.csv"

def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
retornaArq(file_name) 