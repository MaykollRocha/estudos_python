from tkinter.ttk import Progressbar
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox, scrolledtext, ttk

janela = Tk()

janela.title('calculadora')
janela.geometry('265x373')
janela.resizable(width=False, height=False)
janela.config(bg='black')

text_print = ''
valor_texto = StringVar()


def calculadora(var):
    global text_print

    if var.isdigit():
        text_print += var
        valor_texto.set(text_print)
    elif not var == '=':
        text_print += var
        valor_texto.set(text_print)
    else:
        resulado = str(eval(text_print))
        valor_texto.set(resulado)
        text_print = resulado


visor = Label(janela,
              textvariable=valor_texto,
              width=24,
              height=3,
              anchor="e",
              bd=0,
              justify=RIGHT,
              font=('arial 14'),
              bg='#37474F',
              fg="white")
visor.grid(row=0, column=0, columnspan=4)

# sticky="ne"
clear = Button(janela,
               width=11,
               height=2,
               text='c',
               font='Arial 14',
               bg='red',
               relief='solid')
clear.grid(row=1, columnspan=2)

botão_1 = Button(janela,
                 width=5,
                 height=2,
                 text='1',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('1'))
botão_1.grid(row=2, column=0)
botão_2 = Button(janela,
                 width=5,
                 height=2,
                 text='2',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('2'))
botão_2.grid(row=2, column=1)
botão_3 = Button(janela,
                 width=5,
                 height=2,
                 text='3',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('3'))
botão_3.grid(row=2, column=2)
botão_4 = Button(janela,
                 width=5,
                 height=2,
                 text='4',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('4'))
botão_4.grid(row=3, column=0)
botão_5 = Button(janela,
                 width=5,
                 height=2,
                 text='5',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('5'))
botão_5.grid(row=3, column=1)
botão_6 = Button(janela,
                 width=5,
                 height=2,
                 text='6',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('6'))
botão_6.grid(row=3, column=2)
botão_7 = Button(janela,
                 width=5,
                 height=2,
                 text='7',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('7'))
botão_7.grid(row=4, column=0)
botão_8 = Button(janela,
                 width=5,
                 height=2,
                 text='8',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('8'))
botão_8.grid(row=4, column=1)
botão_9 = Button(janela,
                 width=5,
                 height=2,
                 text='9',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('9'))
botão_9.grid(row=4, column=2)
botão_0 = Button(janela,
                 width=11,
                 height=2,
                 text='0',
                 font='Arial 14',
                 bg='white',
                 relief='solid',
                 command=lambda: calculadora('0'))
botão_0.grid(row=5, columnspan=2)

botão_ponto = Button(janela,
                     width=5,
                     height=2,
                     text='.',
                     font='Arial 14',
                     bg='white',
                     relief='solid',
                     command=lambda: calculadora('.'))
botão_ponto.grid(row=5, column=2)
# botões de contas +-*/
resto = Button(janela,
               width=5,
               height=2,
               text='%',
               font='Arial 14',
               bg='white',
               relief='solid',
               command=lambda: calculadora('%'))
resto.grid(row=1, column=2)

divir = Button(janela,
               width=5,
               height=2,
               text='/',
               font='Arial 14',
               bg='orange',
               relief='solid',
               command=lambda: calculadora('/'))
divir.grid(row=1, column=3)

botão_soma = Button(janela,
                    width=5,
                    height=2,
                    text='+',
                    font='Arial 14',
                    bg='orange',
                    relief='solid',
                    command=lambda: calculadora('+'))
botão_soma.grid(row=2, column=3)

botão_subtrair = Button(janela,
                        width=5,
                        height=2,
                        text='-',
                        font='Arial 14',
                        bg='orange',
                        relief='solid',
                        command=lambda: calculadora('-'))
botão_subtrair.grid(row=3, column=3)

botão_multi = Button(janela,
                     width=5,
                     height=2,
                     text='*',
                     font='Arial 14',
                     bg='orange',
                     relief='solid',
                     command=lambda: calculadora('*'))
botão_multi.grid(row=4, column=3)

botão_resultado = Button(janela,
                         width=5,
                         height=2,
                         text='=',
                         font='Arial 14',
                         bg='red',
                         relief='solid',
                         command=lambda: calculadora('='))
botão_resultado.grid(row=5, column=3)

janela.mainloop()
