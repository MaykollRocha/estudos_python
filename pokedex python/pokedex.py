from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

pokedex = Tk()
pokedex.title('Pokedex')
pokedex.geometry('500x500')
pokedex.resizable(width=False, height=False)

ttk.Separator(pokedex, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(pokedex, width=540, height=305, bg='white')
main_frame.grid(row=0, column=0)

pokemon = {"Bulbasaur": {"status": ['HP: 300', 'Attack: 300', 'Defence: 300',
                                    'Speed: 300', 'Total: 1.200'],
                         "skills": ['razor leaves', 'Sunbeam'],
                         "type": ['#001', 'Grass/Poison'],
                         "others": ['D:/ogx/python/pokedex python/images/bulbasaur.png', '#49D0B0']
                         },
           "Ivysaur": {"status": ['HP: 400', 'Attack: 400', 'Defence: 400',
                                  'Speed: 400', 'Total: 1.600'],
                       "skills": [' Vine Whip', 'Power Whip'],
                       "type": ['#002', 'Grass/Poison'],
                       "others": ['D:\ogx\python\pokedex python\images\Ivysaur.png', '#49D0B0']
                       },
           "Venusaur": {"status": ['HP: 500', 'Attack: 500', 'Defence: 500',
                                   'Speed: 500', 'Total: 2.000'],
                        "skills": [' Vine Whip', 'Frenzy Plant'],
                        "type": ['#003', 'Grass/Poison'],
                        "others": ['D:\ogx\python\pokedex python\images\Venusaur.png', '#49D0B0']
                        },
           "Charmander": {"status": ['HP: 300', 'Attack: 400', 'Defence: 300',
                                     'Speed: 400', 'Total: 1.400'],
                          "skills": ['Ember', 'Flamethrower'],
                          "type": ['#004', 'Fire'],
                          "others": ['D:\ogx\python\pokedex python\images\Charmander.png', 'red']
                          },
           "Charmeleon": {"status": ['HP: 400', 'Attack: 400', 'Defence: 400',
                                     'Speed: 500', 'Total: 1.700'],
                          "skills": ['Fire Fang', 'Flamethrower'],
                          "type": ['#005', 'Fire'],
                          "others": ['D:\ogx\python\pokedex python\images\Charmeleon.png', 'red']
                          },
           "Charizard": {"status": ['HP: 500', 'Attack: 500', 'Defence: 500',
                                    'Speed: 600', 'Total: 2.100'],
                         "skills": ['Fire Spin', 'Blast Burn'],
                         "type": ['#006', 'Fire/Flay'],
                         "others": ['D:\ogx\python\pokedex python\images\Charizard.png', 'red']
                         },
           "Squirtle": {"status": ['HP: 300', 'Attack: 300', 'Defence: 300',
                                   'Speed: 400', 'Total: 1.300'],
                        "skills": ['Bubble', 'Aqua Tail'],
                        "type": ['#007', 'Water'],
                        "others": ['D:\ogx\python\pokedex python\images\Squirtle.png', 'blue']
                        },
           "Wartortle": {"status": ['HP: 400', 'Attack: 400', 'Defence: 500',
                                    'Speed: 400', 'Total: 1.700'],
                         "skills": ['Water Gun', 'Hydro Pump'],
                         "type": ['#008', 'Water'],
                         "others": ['D:\ogx\python\pokedex python\images\Wartortle.png', 'blue']
                         },
           "Blastoise": {"status": ['HP: 500', 'Attack: 500', 'Defence: 600',
                                    'Speed: 500', 'Total: 2.100'],
                         "skills": ['Water Gun', 'Hydro Cannon'],
                         "type": ['#009', 'Water'],
                         "others": ['D:\ogx\python\pokedex python\images\Blastoise.png', 'blue']
                         },
           "Pikachu": {"status": ['HP: 300', 'Attack: 400', 'Defence: 300',
                                  'Speed: 600', 'Total: 1.600'],
                       "skills": ['Thunder Shock', 'Wild Charge'],
                       "type": ['#025', 'Eletric'],
                       "others": ['D:\ogx\python\pokedex python\images\Pikachu.png', 'yellow']
                       }
           }


def pokedex_en(pok):
    global l_icon_1, pokemon_image

    main_frame['bg'] = pokemon[pok]['others'][1]

    pk_HP['text'] = pokemon[pok]['status'][0]
    pk_Attack['text'] = pokemon[pok]['status'][1]
    pk_Defence['text'] = pokemon[pok]['status'][2]
    pk_Speed['text'] = pokemon[pok]['status'][3]
    pk_Total['text'] = pokemon[pok]['status'][4]

    pk_skill1['text'] = pokemon[pok]["skills"][0]
    pk_skill2['text'] = pokemon[pok]["skills"][1]

    nome['text'] = pok
    nome['bg'] = pokemon[pok]['others'][1]
    tipo['text'] = pokemon[pok]['type'][1]
    num_pokedex['text'] = pokemon[pok]['type'][0]
    num_pokedex['bg'] = pokemon[pok]['others'][1]

    image = pokemon[pok]['others'][0]
    pokemon_image = Image.open(image)
    pokemon_image = pokemon_image.resize((250, 250))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)

    l_icon_1 = Label(main_frame, image=pokemon_image,
                     bg=pokemon[pok]['others'][1])
    l_icon_1.place(x=60, y=50)


# status
pk_status = Label(pokedex, text='Status', font='Arial 20',
                  fg='black')
pk_status.place(x=10, y=320)

pk_HP = Label(pokedex, text='HP: ', font='Arial 10',
              fg='black')
pk_HP.place(x=10, y=360)

pk_Attack = Label(pokedex, text='Attack: ', font='Arial 10',
                  fg='black')
pk_Attack.place(x=10, y=380)

pk_Defence = Label(pokedex, text='Defence: ', font='Arial 10',
                   fg='black')
pk_Defence.place(x=10, y=400)

pk_Speed = Label(pokedex, text='Speed: ', font='Arial 10',
                 fg='black')
pk_Speed.place(x=10, y=420)

pk_Total = Label(pokedex, text='Total: ', font='Arial 10',
                 fg='black')
pk_Total.place(x=10, y=440)

# Skill
pk_skill = Label(pokedex, text='Skill', font='Arial 20',
                 fg='black')
pk_skill.place(x=200, y=320)

pk_skill1 = Label(pokedex, text='', font='Arial 10',
                  fg='black')
pk_skill1.place(x=200, y=360)

pk_skill2 = Label(pokedex, text='', font='Arial 10',
                  fg='black')
pk_skill2.place(x=200, y=380)

# Apresentação type e imagen
nome = Label(pokedex, text='NAME', font='Arial 20', bg='white')
nome.place(x=0, y=10)
tipo = Label(pokedex, text='type', font='Arial 10', bg='black', fg='white')
tipo.place(x=0, y=60)

num_pokedex = Label(pokedex, text='#num', font='Arial 12', bg='white')
num_pokedex.place(x=0, y=90)

# pokemons
img_pok_1 = Image.open('D:/ogx/python/pokedex python/images/bulbasaur.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

pokemon_boton = Button(pokedex, image=img_pok_1, text='Bulbasaur', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Bulbasaur'))
pokemon_boton.place(x=340, y=0)

img_pok_2 = Image.open('D:\ogx\python\pokedex python\images\Ivysaur.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2 = ImageTk.PhotoImage(img_pok_2)

pokemon_boton = Button(pokedex, image=img_pok_2, text='Ivysaur', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Ivysaur'))
pokemon_boton.place(x=340, y=50)

img_pok_3 = Image.open('D:\ogx\python\pokedex python\images\Venusaur.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)

pokemon_boton = Button(pokedex, image=img_pok_3, text='Venusaur', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Venusaur'))
pokemon_boton.place(x=340, y=100)

img_pok_4 = Image.open('D:\ogx\python\pokedex python\images\Charmander.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)

pokemon_boton = Button(pokedex, image=img_pok_4, text='Charmander', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Charmander'))
pokemon_boton.place(x=340, y=150)

img_pok_5 = Image.open('D:\ogx\python\pokedex python\images\Charmeleon.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)

pokemon_boton = Button(pokedex, image=img_pok_5, text='Charmeleon', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Charmeleon'))
pokemon_boton.place(x=340, y=200)

img_pok_6 = Image.open('D:\ogx\python\pokedex python\images\Charizard.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)

pokemon_boton = Button(pokedex, image=img_pok_6, text='Charizard', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Charizard'))
pokemon_boton.place(x=340, y=250)

img_pok_7 = Image.open('D:\ogx\python\pokedex python\images\Squirtle.png')
img_pok_7 = img_pok_7.resize((40, 40))
img_pok_7 = ImageTk.PhotoImage(img_pok_7)

pokemon_boton = Button(pokedex, image=img_pok_7, text='Squirtle', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Squirtle'))
pokemon_boton.place(x=340, y=300)

img_pok_8 = Image.open('D:\ogx\python\pokedex python\images\Wartortle.png')
img_pok_8 = img_pok_8.resize((40, 40))
img_pok_8 = ImageTk.PhotoImage(img_pok_8)

pokemon_boton = Button(pokedex, image=img_pok_8, text='Wartortle', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Wartortle'))
pokemon_boton.place(x=340, y=350)

img_pok_9 = Image.open('D:\ogx\python\pokedex python\images\Blastoise.png')
img_pok_9 = img_pok_9.resize((40, 40))
img_pok_9 = ImageTk.PhotoImage(img_pok_9)

pokemon_boton = Button(pokedex, image=img_pok_9, text='Blastoise', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Blastoise'))
pokemon_boton.place(x=340, y=400)

img_pok_25 = Image.open('D:\ogx\python\pokedex python\images\Pikachu.png')
img_pok_25 = img_pok_25.resize((40, 40))
img_pok_25 = ImageTk.PhotoImage(img_pok_25)

pokemon_boton = Button(pokedex, image=img_pok_25, text='Pikachu', width=150,
                       bg='white', fg='black',  compound=LEFT, overrelief=RIDGE,
                       command=lambda: pokedex_en('Pikachu'))
pokemon_boton.place(x=340, y=450)

pokedex.mainloop()
