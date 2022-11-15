"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'Perfume'
armazem = '*'*len(palavra_secreta)
vezes = 5
while vezes != 0:
    print(armazem)
    aux = armazem
    armazem = ''
    letra = input(f'Entre com uma letra(mais {vezes}X): ')

    if len(letra) == 1:
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if letra == palavra_secreta[i]:
                    armazem += letra
                elif '*' != aux[i]:
                    armazem += aux[i]
                else:
                    armazem += '*'
        else:
            print('Não tem essa letra. ')
            letra -= 1
            armazem = aux
    else:
        print('É apenas uma letra.  ')
        armazem = aux

    if armazem == palavra_secreta:
        print(f'Parabens você ganhou.A palavra era mesmo {armazem} ')
        break
else:
    print(f'Perdeu a palavra era {palavra_secreta}')
