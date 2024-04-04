def generate_expression(target):
    # Функция для генерации всех возможных комбинаций знаков +, -, и пустого места между числами
    def generate_combinations(n, expression=[]):
        if n == 0:
            combinations.append(expression)
            return
        generate_combinations(n - 1, expression + [' '])
        generate_combinations(n - 1, expression + ['+'])
        generate_combinations(n - 1, expression + ['-'])

    numbers = list(range(9, -1, -1))  # Цифры от 9 до 0
    combinations = []
    generate_combinations(len(numbers) - 1)

    for comb in combinations:
        expression = ''.join(str(num) + sign for num, sign in zip(numbers, comb)) + str(numbers[-1])
        expression = expression.replace(' ', '')  # Удаляем пустые промежутки
        if eval(expression) == target:
            return expression

    return "Невозможно найти комбинацию"

target = 200
print(generate_expression(target))
