from datetime import datetime
from tkinter import *

relogio = Tk()
relogio.title('Relógio')
relogio.geometry('400x150')
relogio.config(bg='black')


def relogi():
    tempo = datetime.now()

    horas.config(text=tempo.strftime("%H:%M:%S"))
    horas.after(200, relogi)
    data.config(text=tempo.strftime("%A") + "   " + str(tempo.day) +
                "/" + str(tempo.strftime("%b")) + "/" + (tempo.strftime("%Y")))


horas = Label(relogio, text='10:10:10',
              font='times 60', bg='black', fg='red')
horas.pack(side='top')
data = Label(relogio, text='diasemna  dia/mes/ano', font='times 15',
             bg='black', fg='red')
data.pack(side='left')

relogi()

relogio.mainloop()
