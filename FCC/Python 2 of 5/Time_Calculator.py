def add_time(start, duration,week=None):
    tempo,periodo = start.split(' ')
    hora,minutos = (int(i) for i in tempo.split(':'))
    ahora,aminutos = (int(i) for i in duration.split(':'))
    minutos += aminutos

    
    if minutos >= 60:
        ahora += 1
        minutos -= 60
    hora += ahora
    dayspass = 0
    while hora >= 12:
        hora -= 1
        if 'AM' == periodo:
            periodo = 'PM'
        else:
            dayspass += 1
            periodo = 'AM'
        hora -= 11
    if hora == 0:
        hora = 12
    
    new_time = f'{hora}:{minutos:02d} {periodo}'

    if week:
        week =week.capitalize()
        weeks = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
        idex = (weeks.index(week) + dayspass)%7

        new_time += f', {weeks[idex]}'

    if dayspass == 1:
        new_time += ' (next day)'
    elif dayspass:
        new_time += f' ({dayspass} days later)'

    
    return new_time

print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))