{
  "nome":"Projeto do Formato Aritmédico",
  "infos": {"atividade":"Build an Arithmetic Formatter Project","dia":"26 de Maio de 2024"},
  "descrição":"""
 """,
  "Código":"""
  def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    lines = ['', '', '', '']  # Lista para armazenar as linhas do problema

    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand1), len(operand2)) + 2  # Largura do campo

        lines[0] += operand1.rjust(width)
        lines[1] += operator + operand2.rjust(width - 1)
        lines[2] += '-' * width

        if show_answers:
            result = str(eval(problem))
            lines[3] += result.rjust(width)

        # Adicionar espaços entre os problemas
        if problem != problems[-1]:
            for i in range(4):
                lines[i] += '    '

    arranged_problems = '\n'.join(lines[0:3])
    if show_answers: arranged_problems = '\n'.join(lines)

    return arranged_problems


# Exemplos de uso:
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
           """,
    "agregamento":"""
                  Foi muito interresente e pretendo apresentar esse trabalho pra algum aluno de matemática ou algo do tipo.
                  """,
  "link": ""

}
