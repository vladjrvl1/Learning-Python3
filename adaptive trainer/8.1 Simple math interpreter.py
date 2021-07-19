"""
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a \texttt{ operator }
 ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова: plus, minus, multiply,
 divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000. Оператор может
быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число -− результат вычисления.
"""

expression = input().strip().split()


def math_interpret(expr):
    n1, operator, n2 = int(expr[0]), expr[1], int(expr[2])
    result = None
    if operator == 'plus':
        result = n1 + n2
    elif operator == 'minus':
        result = n1 - n2
    elif operator == 'multiply':
        result = n1 * n2
    elif operator == 'divide':
        result = n1 // n2

    return result


output = math_interpret(expression)
print(str(output))
