'''
Nome: Maykoll Rocha
dia: 16/11/2022
um lista de vetor que era em C no início agora vou fazela en python
'''
import random

'''
1. Faça uma solução para computar a nota de 10 alunos. Ao término, 
mostrar as notas cujo valor tenha sido superior à média de notas da turma 

notas = [float(random.uniform(0, 10)) for _ in range(10)]

media = sum(notas)/10
repo = []
for i in notas:
    if i >= media:
        repo.append(i)

print(media, *repo, sep='\n')

'''

'''
2. Faça uma solução para ler 10 valores inteiros. Em seguida, imprima-os na 
ordem inversa (o último elemento deverá ser o primeiro a ser impresso)

valores = [random.randint(0, 100) for _ in range(10)]

print(*valores, sep='-')
for i in range(9, -1, -1):
    print(valores[i], end='-')

'''

'''
3. Inicialize dois vetores de inteiros de mesmo tamanho. Some o conteúdo 
dos dois vetores e armazene o resultado em um terceiro vetor, na 
respectiva posição. Imprima os elementos do terceiro vetor

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
vet = [num1, num2]
print(vet)

'''

'''
4. Inicialize com '\0' um vetor de caracteres de 10 posições. Insira 
caracteres no mesmo e, em seguida, imprima seus elementos apenas se 
valor for vogal

char = []
for i in range(10):
    char.append(input('Entre com letra: '))

for i in char:
    if not i.upper() in "AEIOU":
        print(i, end='-')
        
'''

'''
5. Insira elementos em um vetor de inteiros e peça ao usuário informar um 
número a ser procurado nessa estrutura. Se encontrar, mostre o número e 
o índice onde o mesmo se encontra

nums = [random.randint(0, 10) for _ in range(10)]

procura = abs(int(input('Entre com o valor a ser procurado: ')))

for i in range(len(nums)):
    if procura == nums[i]:
        print(f'{i} é o indice e o número é {nums[i]}.')
'''

'''
6. Adicionalmente ao exercício anterior, remova o elemento da estrutura, 
fazendo a sobreposição de elementos

nums = [random.randint(0, 10) for _ in range(10)]
print(*nums, sep='-')
procura = abs(int(input('Entre com o valor a ser removido: ')))
repo = []
for i in range(len(nums)):
    if not procura == nums[i]:
        repo.append(nums[i])

print(*repo, sep='-')

'''

'''
7. Faça uma solução para exibir um menu ao usuário, enquanto a opção for 
diferente de “sair”
As opções devem incluir as operações: inserir, pesquisar, excluir, imprimir e sair 
Inserir
Insere um inteiro em um vetor de 5 posições
Pesquisar
Pesquisa um elemento no vetor 
Excluir
Remove um elemento do vetor
Imprimir
Mostra todos os elementos do vetor
Sair
Encerra o programa

A solução deve ser consistente:
-Não inserir mais de 5 itens
-Não pesquisar, se vetor é vazio
-Não excluir, se vetor é vazio
-Não imprimir, se vetor é vazio
-Antes de excluir, pesquisar o item
Implemente e teste cada funcionalidade 
antes de implementar as demais

op = ' '
vet = []
while op.lower() != 'sair':
    print(*vet, sep='-')
    op = input('[I]nserir\n[P]esquisar\n[E]xcluir\n[I]mprimir\n[S]air')
    match op[0].lower():
        case 'i':
            if len(vet) < 6:
                vet.append(int(input('Entre com um valor: ')))
            else:
                print('Vetor cheio.')
        case 'p':
            if len(vet):
                proc = int(input('Procura no vetor: '))

                for i in range(0, len(vet)):
                    if proc == vet[i]:
                        print(f'Achei o {vet[i]} no indice {i}. ')
                        break
                else:
                    print('Não existe.')
            else:
                print('Vazio.')
        case 'e':
            if len(vet):
                excluir = int(input('Procura numero a ser excluido: '))
                repo = []
                for i in range(0, len(vet)):
                    if not excluir == vet[i]:
                        repo.append(vet[i])
                vet.clear()
                vet = repo.copy()
                repo.clear()
            else:
                print('Vazio.')
        case 'i':
            if len(vet):
                for i in vet:
                    print(i, sep='-')
            else:
                print('Vazio.')
        case 's':
            break

'''
