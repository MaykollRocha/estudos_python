{
  "nome":"Build a Probability Calculator Project",
  "infos": {"atividade":"Build a Probability Calculator Project Certification Project","dia":"13 de junho de 2024"},
  "descrição":"""
	Suponha que há um chapéu contendo 5 bolas azuis, 4 bolas vermelhas e 2 bolas verdes. Qual é a probabilidade de que uma extração aleatória de 4 bolas contenha pelo menos 1 bola vermelha e 2 bolas verdes? Embora seja possível calcular a probabilidade usando matemática avançada, uma maneira mais fácil é escrever um programa para realizar um grande número de experimentos para estimar uma probabilidade aproximada.
	Para este projeto, você escreverá um programa para determinar a probabilidade aproximada de desenhar certas bolas aleatoriamente de um chapéu.
              """,
  "Código":"""
  import random
from collections import Counter
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            indices = random.sample(range(len(self.contents)), num_balls)
            drawn_balls = [self.contents[i] for i in sorted(indices, reverse=True)]
            for i in sorted(indices, reverse=True):
                del self.contents[i]
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = Counter(drawn_balls)
        
        # Check if all expected balls are in the drawn balls
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_balls_count[color] < expected_count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    return successful_experiments / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
           """,
"imag":"output_PCP.png",
    "agregamento":"""
                 Um projeto mais experimental, não acho que foi tão relevante quanto os outros mais em consenso de conhecimento gerais fazer uma calculadora de probabilidade é bem legal principalmente para futuros pensamentos de analise de dados em vias reais.
                  """,
  "link": "https://github.com/MaykollRocha/estudos_python/blob/main/FCC/Python%205%20of%205/Probability_Calculator.py"

}
