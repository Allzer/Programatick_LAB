def generate_expressions(target):
    def generate_combinations(n, expression=[]):
        if n == 0:
            combinations.append(expression)
            return
        generate_combinations(n - 1, expression + [' '])
        generate_combinations(n - 1, expression + ['+'])
        generate_combinations(n - 1, expression + ['-'])

    def evaluate(expression):
        expression = ''.join(str(num) + sign for num, sign in zip(numbers, expression)) + str(numbers[-1])
        expression = expression.replace(' ', '')
        return eval(expression)

    numbers = list(range(9, -1, -1))
    combinations = []
    generate_combinations(len(numbers) - 1)

    results = []
    for comb in combinations:
        if evaluate(comb) == target:
            results.append(''.join(str(num) + sign for num, sign in zip(numbers, comb)) + str(numbers[-1]))

    return results if results else ["Невозможно найти комбинацию"]

target = 200
expressions = generate_expressions(target)
for expr in expressions:
    print(expr.replace(' ', ''))