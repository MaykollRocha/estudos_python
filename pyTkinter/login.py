from tkinter import *
from tkinter import messagebox, ttk

'''
Um Sistema de login sem nada salvo apenas pra ideda e teste 
de um site que me ensinou sobre tal biblioteca.

'''


# configs de tela
login = Tk()

login.title('Tela de login.')
login.geometry('200x250')
login.resizable(width=False, height=False)

# função apos confirmar


def arruma(var) -> str:
    txt = ''

    for i in var.split(' '):
        txt += f'{i.capitalize()} '

    return txt


def logar():
    if not nome.get():
        messagebox.showwarning('Campo Vazio', 'Campo nome vazio')
        nome.delete(0, END)
        senha.delete(0, END)
        return

    if not senha.get():
        messagebox.showwarning('Campo Vazio', 'Campo Senha vazio')
        nome.delete(0, END)
        senha.delete(0, END)
        return

    nome_ = arruma(nome.get())
    senha_ = senha.get()

    if senha_ == '12345':
        messagebox.showinfo('Sucesso Login', f'Welcome {nome_}')
    else:
        messagebox.showinfo('Fail Login', 'Senha errada')
    nome.delete(0, END)
    senha.delete(0, END)


# visual não interagivel
titulo_nome = Label(login, text='Login', justify='center',
                    font='Arial 24', fg='#65cca9')
titulo_nome.place(x=60, y=0)

faixa = Label(login, width='40', bg='#65cca9')
faixa.place(x=0, y=40)

pergunta = Label(login, text='Nome: ', font='Arial 10', fg='#acbfa3')
pergunta.place(x=0, y=70)

pergunta2 = Label(login, text='Senha: ', font='Arial 10', fg='#acbfa3')
pergunta2.place(x=0, y=130)

# interagiveis de Nome, login e confirmação:flat, groove,
# raised, ridge, solid, or sunken

nome = Entry(login, width='17', bg='#dcf4da',
             font='Arial 14', borderwidth='3', relief='ridge')
nome.place(x=4, y=100)

# senha correta 12345
senha = Entry(login, show='*',
              width='17', bg='#dcf4da',
              font='Arial 14', borderwidth='3', relief='ridge')
senha.place(x=4, y=160)

confirme = Button(login, text='Confirmar', font='Arial 10',
                  bg='#65cca9', fg='black', relief='ridge',
                  width=10, height=2, command=logar)
confirme.place(x=50, y=200)


login.mainloop()
