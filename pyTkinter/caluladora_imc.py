from tkinter import *
from tkinter import ttk

janela = Tk()

janela.title('IMC Caulator')
janela.geometry('400x400')
janela.resizable(width=False, height=False)


def calcular():
    peso = entre_peso.get()
    alt = entre_altura.get()
    calc = f'{peso}/({alt}*{alt})'

    Resultado['text'] = f'{float(eval(calc)):.2f}'

    if float(eval(calc)) < 18.5:
        text_resultado['text'] = 'Seu IMC é: Abaixo do Peso'
    elif float(eval(calc)) < 25:
        text_resultado['text'] = 'Seu IMC é: Normal'
    elif float(eval(calc)) < 30:
        text_resultado['text'] = 'Seu IMC é: Sobre Peso'
    else:
        text_resultado['text'] = 'Seu IMC é: Obeso'


text = Label(janela, text='CALCULADORA IMC',
             font='Arial 20', fg='blue', justify='center')
text.place(x=60, y=2)

linha = Label(janela, text="", width=400, height=1,
              relief="flat", anchor="nw", font=('Arial 1'), bg='blue', fg='blue')
linha.place(x=0, y=35)

text_peso = Label(janela, text='Insira seu Peso', width=15, height=1,
                  font='Arial 14', fg='blue')
text_peso.place(x=0, y=60)

entre_peso = Entry(janela, width=5, font='Arial 14', bg='grey')
entre_peso.place(x=180, y=60)

text_altura = Label(janela, text='Insira sua Altura', width=15, height=1,
                    font='Arial 14', fg='blue')
text_altura.place(x=0, y=140)

entre_altura = Entry(janela, width=5, font='Arial 14', bg='grey')
entre_altura.place(x=180, y=140)

Resultado = Label(janela, text='vazio', width=4, height=2,
                  font='Arial 28', fg='white', bg='blue')
Resultado.place(x=280, y=60)

text_resultado = Label(janela, text='Seu IMC é: ', width=22, height=2,
                       font='Arial 14', fg='blue')
text_resultado.place(x=70, y=200)

confirma = Button(janela, text='Calcular', width=50, height=2,
                  bg='blue', command=calcular)
confirma.place(x=20, y=300)


janela.mainloop()
