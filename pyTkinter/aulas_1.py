
from tkinter.ttk import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk

janela = Tk()

tab_control = ttk.Notebook(janela)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Registro de inferior')
tab_control.add(tab2, text='Segundo')

tab_control.pack(expand=1, fill='both')

# como é py3 Tk é maiuculo

# Titulo da janela
janela.title('Registro.')
# LarguraXcomprimento da janela
janela.geometry('500x500')
# mudar cores
# janela.config(bg='gray')
# alterar incone
#janela.iconphoto(False,PhotoImage(file='File nome(png)'))

# não altera o tamanho da jabela
#janela.resizable(width=False, height=True)

# cont = 0

# def executa():
#     global cont

#     texto_1 = 'par'
#     texto_2 = 'Impar'

#     if not cont % 2:
#         label_texto['text'] = texto_1
#     else:
#         label_texto['text'] = texto_2

#     cont += 1


def obter():
    res = messagebox.askyesno('confirmação', 'Conteúdo da mensagem')
    if res:
        nome = entra_nome.get()
        idade = entra_idade.get()
        pais = combo.get()

        texto.insert(
            INSERT,
            f'{nome.capitalize()} {idade} {pais} {doador.get()} {sexo.get()}\n'
        )

        entra_nome.delete(0, END)
        entra_idade.delete(0, END)
        bar['value'] = spli.get()


# criar um label
# label = Label(janela, width=30, text='Primeira Calculadora')
# um é com place
# label.place(x=10, y = 10)
# Centraliza totalmente  side escolhe o lado
# label.pack()
# coloca e colunas e linhas
# mudar estilo de letra padrões Font, fg=(cor da letra ) bg Fundo do label
Label_nome = Label(tab1, width=15, height=2, text='Nome', font='Arial 10')
Label_nome.grid(row=0, column=0)

Label_idade = Label(tab1, width=15, height=2, text='idade', font='Arial 10')
Label_idade.grid(row=1, column=0)

# Para desabilitar so colocar state='disable'
entra_nome = Entry(tab1, width=10, font='Arial 10')
entra_nome.grid(row=0, column=1)

entra_idade = Entry(tab1, width=10, font='Arial 10')
entra_idade.grid(row=1, column=1)

# Check box para pais apartir de agora
Label_num = Label(tab1, width=15, height=2, text='Pais', font='Arial 10')
Label_num.grid(row=2, column=0)

combo = Combobox(tab1)
combo['value'] = ('Brasil', 'Argentina', 'Portugal', 'Estados Unidos')
combo.current(0)
combo.grid(row=2, column=1)

# checkbooton
doador = StringVar()
doador.set(True)
chek = Checkbutton(tab1,
                   text='doador?',
                   var=doador,
                   onvalue='Doador',
                   offvalue='Não Doador')
chek.grid(row=3, column=0)

# parte para registro de valores
texto = scrolledtext.ScrolledText(tab1, width=50, height=10)
texto.grid(row=5, column=1)
texto.insert(INSERT, 'Nome Idade Cidade Doador Sexo\n')

botao = Button(tab1,
               width=10,
               height=2,
               text='click',
               relief='solid',
               command=obter)
botao.grid(row=1, column=2)

#radio Button
sexo = StringVar()

rad1 = Radiobutton(tab1, text='Masculino', value='Masculino', variable=sexo)
rad1.grid(row=4, column=0)

rad2 = Radiobutton(tab1, text='Feminino', value='Feminino', variable=sexo)
rad2.grid(row=4, column=1)

#numero de inscritos você aumenta por conta
var = IntVar()
var.set(0)
spli = Spinbox(tab1, from_=0, to=100, width=10, textvariable=var)
spli.grid(row=0, column=2)

#barras de progresso

style = ttk.Style()
style.theme_use('default')
style.configure("red.Horizontal.TProgressbar", background='red')

bar = Progressbar(tab1, length=200, style='red.Horizontal.TProgressbar')
bar['value'] = spli.get()
bar.grid(column=1, row=3)

#tab2

def calcula():
  try



valor = Button(tab2, text='')
valor.grid(row=0, column=0)

texto2 = scrolledtext.ScrolledText(tab2, width=20, height=1)
texto2.place(x=0, y=0)
texto2.insert(INSERT, '')

valor1 = Button(tab2, text='1')
valor1.grid(row=1, column=0)
valor2 = Button(tab2, text='2')
valor2.grid(row=1, column=1)
valor3 = Button(tab2, text='3')
valor3.grid(row=1, column=2)
soma = Button(tab2, text='+')
soma.grid(row=1, column=3)
valor4 = Button(tab2, text='4')
valor4.grid(row=2, column=0)
valor5 = Button(tab2, text='5')
valor5.grid(row=2, column=1)
valor6 = Button(tab2, text='6')
valor6.grid(row=2, column=2)
sub = Button(tab2, text='-')
sub.grid(row=2, column=3)
valor7 = Button(tab2, text='7')
valor7.grid(row=3, column=0)
valor8 = Button(tab2, text='8')
valor8.grid(row=3, column=1)
valor9 = Button(tab2, text='9')
valor9.grid(row=3, column=2)
div = Button(tab2, text='/')
div.grid(row=3, column=3)
igual = Button(tab2, text='=')
igual.grid(row=4, column=2)
valor0 = Button(tab2, text='0')
valor0.grid(row=4, column=1)
mult = Button(tab2, text='*')
mult.grid(row=4, column=3)

janela.mainloop()
