# Завдання 3
# Історія дій: Створіть клас Calculator, який
# використовує стек для зберігання операцій та
# операндів. Методи класу можуть виконувати операції,
# зберігаючи їх у стеці для подальшого відновлення
# історії обчислень.

class OperatorOverloadMeta(type):
    def new(cls, name, bases, dct):
         dct["add"] = lambda self, other: self.add(other)
         dct["sub"] = lambda self, other: self.sub(other)
         dct["mul"] = lambda self, other: self.mul(other)
         dct["truediv"] = lambda self, other: self.truediv(other)
         return super().new(cls, name, bases, dct)


class MyClass(metaclass=OperatorOverloadMeta):
    def init(self, value):
        self.value = value

    def add(self, other):
        return self.value + other.value if isinstance(other, MyClass) else self.value + other
    def sub(self, other):
        return self.value - other.value if isinstance(other, MyClass) else self.value - other
    def mul(self, other):
        return self.value * other.value if isinstance(other, MyClass) else self.value * other
    def truediv(self, other):
        return self.value / other.value if isinstance(other, MyClass) else self.value / other

obj1 = MyClass(10)
obj2 = MyClass(2)
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 / obj2)


