
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '2', '5', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Como diz cachorro-quente em inglês?',
        'Opções': ['hot hot', 'hot dog', 'dog hot', 'dog food'],
        'Resposta': 'hot dog',
    },
    {
        'Pergunta': 'Quantas vogais há na palavra pesqueiro?',
        'Opções': ['5', '2', '3', '4'],
        'Resposta': '5',
    },
    {
        'Pergunta': ' Qual o nome da capital da Inglaterra?',
        'Opções': ['Brasilia', 'Londres', 'Madrid', 'Edimburgo'],
        'Resposta': 'Londres',
    },
    {
        'Pergunta': 'Onde se localiza o osso malar?',
        'Opções': [' coluna', 'perna', 'cabeça', 'braço'],
        'Resposta': 'cabeça',
    },
    {
        'Pergunta': 'Como ficou conhecido o regime de discriminação racial\n'
                    'que separava brancos e negros na África do Sul entre 1948 e 1990?',
        'Opções': ['Escravidão', 'Festa do Chá', 'Homogligerina',  'Apartheid'],
        'Resposta': 'Apartheid',
    },
]


def pegar(perg):
    print('Pergunta:', perg['Pergunta'])
    for i in range(4):
        print(f'{i})', perg['Opções'][i])

    try:
        resp = abs(int(input('Resposta: ')))
    except:
        resp = 5  # para cair no erro caso entra com letras

    if resp < 4 and perg['Opções'][resp] == perg['Resposta']:
        print('acertou')
        return 1
    else:
        print('Errou')
        return 0


pontos = 0
for i in perguntas:
    pontos += pegar(i)

print(f'Acetou {pontos} de {len(perguntas)}.Parabens!!.')
