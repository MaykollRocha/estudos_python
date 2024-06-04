{
  "nome":"Cacalcular o Tempo",
  "infos": {"atividade":"Build a Time Calculator ProjectCertification Project","dia":"3 de junho de 2024"},
  "descrição":"""Escreva uma função chamada add_time que recebe dois parâmetros obrigatórios e um parâmetro opcional :  
* um horário de início no formato de relógio de 12 horas (terminando em AM ou PM)  
* um tempo de duração que indica o número de horas e minutos  
* (opcional) um dia da semana de início, sem diferenciação de maiúsculas e minúsculas  
A função deve adicionar o tempo de duração ao horário de início e retornar o resultado.  
Se o resultado for no dia seguinte, deve mostrar (próximo dia) após o horário. Se o resultado for mais de um dia depois, deve mostrar (n dias depois) após o horário, onde "n" é o número de dias depois.  
Se a função receber o parâmetro opcional do dia da semana de início, então a saída deve exibir o dia da semana do resultado. O dia da semana na saída deve aparecer após o horário e antes do número de dias depois.  
              """,
  "Código":"""
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
           """,
"imag":"output_BTCP.png",
    "agregamento":"""
                  Para alguém familiarizado com Python, o código pode parecer trivial. No entanto, o objetivo é explorar várias abordagens pouco comuns ou subutilizadas. Foi uma experiência fascinante recriar esse projeto, pois envolveu a exploração de técnicas e métodos que raramente são utilizados ou que, quando utilizados, muitas vezes são negligenciados.  
                  """,
  "link": "https://github.com/MaykollRocha/estudos_python/tree/main/FCC/Python%202%20of%205"

}
