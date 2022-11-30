from tkinter import *
from tkinter import scrolledtext, ttk


def conct(*args):
    resp = ''
    for i in range(len(args)):
        aux = args[i]+(' '*i)
        resp += f'\n{aux:>20}'

    return resp


def multiplicador(mult='', mulx='1', base='10'):
    if mult:
        rest = 0
        resp = ''
        mult = mult[::-1]
        for p in range(len(mult)):
            aux = int(mult[p])*int(mulx) + rest
            rest = aux//int(base)
            resp += f'{aux%int(base)}'

        if rest:
            resp += f'{rest}'

        return resp[::-1]


def resultador(mult='', mulx='', base='10'):

    texto.delete(1.0, END)  # Limpa automatico a cada conta

    # checa de tem algum numero que não é inteiros
    if mult.isdigit() and mulx.isdigit():
        rest_S = []
        for i in range(1, len(mulx)+1):
            rest_S.append(multiplicador(mult, mulx[-i], base))

        soma = 0
        for e, i in enumerate(rest_S):
            soma += (int(i)*(10**e))

        resp_f = multiplicador(str(soma), '1', base)
        mulx = 'X'+mulx
        resp_f = f'{mult:>20}\n{mulx:>20}\n' + '-'*20 + \
            conct(*rest_S) + f"\n{'-'*20}\n{resp_f:>20}"
        return resp_f

    # retorna vazio caso entre com valores errados não digitos
    return ''


window = Tk()
window.geometry('300x300')
window.title('Calculadora de varias bases(2-10)')
window.resizable(height=False, width=False)
window.iconphoto(False, PhotoImage(file='D:.\Metodos\calc.png'))

text_title = Label(window, text='--Multiplicador De Algumas Bases--',
                   font='Arial 14')
text_title.place(x=0, y=0)
text_basic_inf = Label(window, text='Entre com numeros referentes a mesma base\n'
                       'erros pode ser causados caso entre errado.',
                       font='Arial 7', fg='#c0c0c0')
text_basic_inf.place(x=50, y=30)

text_1 = Label(window, text='Multiplicando', font='Arial 10')
text_1.place(x=20, y=70)

text_2 = Label(window, text='Multiplicador', font='Arial 10')
text_2.place(x=20, y=120)

text_3 = Label(window, text='Base', font='Arial 10')
text_3.place(x=20, y=170)

mult = Entry(window, width=10)
mult.place(x=20, y=90)

mulx = Entry(window, width=10)
mulx.place(x=20, y=140)

var = IntVar()
var.set(10)
spli = Spinbox(window, from_=2, to=10, width=10, textvariable=var)
spli.place(x=20, y=190)

texto = scrolledtext.ScrolledText(window, width=20, height=14)
texto.place(x=100, y=60)

buttom = Button(window, width=8, text='Confirmar',
                command=lambda: texto.insert(INSERT, resultador(mult.get(), mulx.get(), spli.get())))
buttom.place(x=20, y=210)

window.mainloop()
