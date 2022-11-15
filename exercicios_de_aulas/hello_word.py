import time

alfabeto = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.,çãÂá'
frase = 'hello word'
nova = ''
while nova != frase:
    for i in alfabeto:
        print(nova, i, sep='')
        time.sleep(0.01)
        if i == frase[len(nova)]:
            nova += i
            break
