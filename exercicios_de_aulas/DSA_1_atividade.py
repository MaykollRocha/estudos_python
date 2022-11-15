"""
#Exercício 1:

dia = input("Entre com que dia é hj: ")
dia = dia.capitalize()
if dia != 'Sabado' or dia != 'Domingo':
    for i in range(0,len(dia)):
        if dia[i] == '-':
            break
        elif i == len(dia)-1:
            dia = dia +'-feira'

if dia == 'Sabado' or dia == 'Domingo':
    print("Foguinha-FI\n")
else:
    print("Bora trampa que quem ganha dinheiro na cama é puta.%s\n"%(dia))    
"""

'''
#Exercício 2:

lista_frutas = ['Pera','Morango','Uva','Maçã','Abacaxi']

for i in range(0,len(lista_frutas)):
    if lista_frutas[i] == 'Morango':
        print("Existe\n")
        break
    elif i == len(lista_frutas)-1:
        print("Não tem nada\n")
             
'''

""" 
#Exercício 3:

tup = (1,'2',3.1415,True)
new_list = []
for i in range(0,len(tup)):
    new_list.append(tup[i]*2)
    
print(new_list)
"""

"""
#Exercício 4:

par_lista = [i for i in range(100,151,2)]
print(par_lista)

for i in range(100,151,2):
    print(i)
"""

"""
#Exercício 5:

temperatura = 40

while temperatura > 35:
    print(temperatura)
    
#não me dava condição de parada no exercicio logo cai em um lanço infinito.
"""

"""
#Exercicio 6:

contador = 0
while contador<100:
    if contador == 23:
        break
    print(contador)
    contador +=1

"""

"""
#Exercio 7:

list_free = []

var_al = 4

while var_al <= 20:
    if var_al%2 == 0:
        list_free.append(var_al)
    
    var_al+=1
    
print(list_free)
"""

"""
#Exercício 8:

nums = [i for i in range(5, 45, 2)]
print(nums)
"""

"""
#Exercio 9:

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

"""


"""
#Exercio 10:

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
cont = 0
for i in range(0,len(frase)):
    if frase[i]=='r':
        cont +=1

print("O numero de vezes que 'r' aparece na frase de Machado de Assis %i.\n" %(cont))
"""
