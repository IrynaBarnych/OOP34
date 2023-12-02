# Завдання 3
# Історія дій: Створіть клас Calculator, який
# використовує стек для зберігання операцій та
# операндів. Методи класу можуть виконувати операції,
# зберігаючи їх у стеці для подальшого відновлення
# історії обчислень.

class Calculator:
    def __init__(self):
        self.stack = []

    def add(self, operand):
        result = sum(operand)
        self.stack.append(('add', operand, result))
        return result

    def sub(self, operand):
        result = operand[0] - operand[1]
        self.stack.append(('sub', operand, result))
        return result

    def mul(self, operand):
        result = operand[0] * operand[1]
        self.stack.append(('mul', operand, result))
        return result

    def truediv(self, operand):
        if operand[1] != 0:
            result = operand[0] / operand[1]
            self.stack.append(('truediv', operand, result))
            return result
        else:
            raise ValueError("Division by zero")

    @property
    def history(self):
        return self.stack


class MyClass:
    calculator = Calculator()

    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.calculator.add((self.value, other.value))

    def sub(self, other):
        return self.calculator.sub((self.value, other.value))

    def mul(self, other):
        return self.calculator.mul((self.value, other.value))

    def truediv(self, other):
        return self.calculator.truediv((self.value, other.value))

    @property
    def history(self):
        return self.calculator.history


obj1 = MyClass(10)
obj2 = MyClass(2)
print(obj1.add(obj2))
print(obj1.sub(obj2))
print(obj1.mul(obj2))
print(obj1.truediv(obj2))

print(obj1.history)
print(obj2.history)










