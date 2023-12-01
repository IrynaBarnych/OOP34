# Завдання 3
# Історія дій: Створіть клас Calculator, який
# використовує стек для зберігання операцій та
# операндів. Методи класу можуть виконувати операції,
# зберігаючи їх у стеці для подальшого відновлення
# історії обчислень.

class Calculator:
    def __init__(self):
        self.stack = []

    def perform_operation(self, operator, operand):
        if operator in ('+', '-', '*', '/'):
            self.stack.append((operator, operand))
            self.calculate_result()
            self.print_history()
        else:
            print("Invalid operator")

    def calculate_result(self):
        while len(self.stack) >= 3 and self.stack[-3][0] == 'result':
            operator, operand = self.stack[-2:]
            del self.stack[-3:]

            if operator == '+':
                result = operand[0] + operand[1]
            elif operator == '-':
                result = operand[0] - operand[1]
            elif operator == '*':
                result = operand[0] * operand[1]
            elif operator == '/':
                result = operand[0] / operand[1]

            self.stack.append(('result', result))

    def print_history(self):
        print("History:")
        for entry in self.stack:
            print(entry)
        print()

    def get_history(self):
        return self.stack


# Приклад використання:
calculator = Calculator()

calculator.perform_operation('+', 10)
calculator.perform_operation('*', 2)
calculator.perform_operation('-', 5)
calculator.perform_operation('/', 3)






