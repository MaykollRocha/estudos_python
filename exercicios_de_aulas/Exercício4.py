"""
Exercício 4
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite seu nome: ") or None
idade = int(input("Digite sua idade: ")) or 0

if nome and idade:
    print(f"Nome: {nome}\n Nome invertido: {nome[::-1]}")
    if ' ' in nome:
        print("Tem espaço no nome.")
    else:
        print("Tem espaço no nome.")
    print(f"Seu nome tem {len(nome)} letras")
    print(f'A primeira letra é {nome[0]} e a ultima letra é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")
