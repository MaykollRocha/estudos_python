
from tkinter.ttk import *
from tkinter import *

janela = Tk()  # como é py3 Tk é maiuculo

# Titulo da janela
janela.title('Registro.')
# LarguraXcomprimento da janela
janela.geometry('400x250')
# mudar cores
# janela.config(bg='gray')
# alterar incone
#janela.iconphoto(False,PhotoImage(file='File nome(png)'))

# não altera o tamanho da jabela
janela.resizable(width=False, height=True)

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

    nome = entra_nome.get()
    idade = entra_idade.get()
    pais = combo.get()

    label_texto['text'] += f'\n{nome.capitalize()} {idade} {pais} {doador.get()}'

    entra_nome.delete(0, END)
    entra_idade.delete(0, END)


# criar um label
# label = Label(janela, width=30, text='Primeira Calculadora')
# um é com place
# label.place(x=10, y = 10)
# Centraliza totalmente  side escolhe o lado
# label.pack()
# coloca e colunas e linhas
# mudar estilo de letra padrões Font, fg=(cor da letra ) bg Fundo do label
Label_nome = Label(janela, width=15, height=2, text='Nome', font='Arial 10')
Label_nome.grid(row=0, column=0)

Label_idade = Label(janela, width=15, height=2,
                    text='idade', font='Arial 10')
Label_idade.grid(row=1, column=0)


# Para desabilitar so colocar state='disable'
entra_nome = Entry(janela, width=10, font='Arial 10')
entra_nome.grid(row=0, column=1)

entra_idade = Entry(janela, width=10, font='Arial 10')
entra_idade.grid(row=1, column=1)

# Check box para pais apartir de agora
Label_num = Label(janela, width=15, height=2, text='Pais',
                  font='Arial 10')
Label_num.grid(row=2, column=0)

combo = Combobox(janela)
combo['value'] = ('Brasil', 'Argentina', 'Portugal')
combo.current(0)
combo.grid(row=2, column=1)

# checkbooton
doador = StringVar()
doador.set(True)
chek = Checkbutton(janela, text='doador?', var=doador,
                   onvalue='Doador', offvalue='Não Doador')
chek.grid(row=3, column=0)

# parte para registro de valores
label_texto = Label(janela, width=20, height=10, text='nome idade pais Sexo',
                    font='Arial 10', anchor='n')
label_texto.grid(row=4, column=1)

botao = Button(janela, width=10, height=2, text='click',
               relief='solid', command=obter)
botao.grid(row=1, column=2)


janela.mainloop()
