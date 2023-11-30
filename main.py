# Завдання 1
# Реалізуйте клас стека роботи з цілими значеннями (стек цілих). Стек має бути фіксованого розміру.
# Реалізуйте набір операцій для роботи зі стеком o розміщення цілого значення у стеку;
# o виштовхування цілого значення зі стеку;
# o підрахунок кількості цілих у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування верхнього цілого в стеку.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.


class FixedStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Стек повний, неможливо додати значення.")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Стек порожній, неможливо видалити значення.")
        else:
            value = self.stack[self.top]
            self.top -= 1
            return value

    def get_size(self):
        return self.top + 1

    def clear(self):
        self.top = -1
        self.stack = [None] * self.size

    def peek(self):
        if self.is_empty():
            print("Стек порожній, неможливо переглянути значення.")
        else:
            return self.stack[self.top]


# Приклад використання класу FixedStack:
fixed_stack = FixedStack(5)

while True:
    print("\nМеню:")
    print("1. Додати значення у стек")
    print("2. Видалити значення зі стеку")
    print("3. Кількість значень у стеку")
    print("4. Перевірити, чи стек порожній")
    print("5. Перевірити, чи стек повний")
    print("6. Очистити стек")
    print("7. Отримати значення без видалення з верхнього елемента стеку")
    print("0. Вихід")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        value = int(input("Введіть значення: "))
        fixed_stack.push(value)
    elif choice == "2":
        popped_value = fixed_stack.pop()
        print("Видалено значення:", popped_value)
    elif choice == "3":
        print("Кількість значень у стеку:", fixed_stack.get_size())
    elif choice == "4":
        print("Стек порожній:", fixed_stack.is_empty())
    elif choice == "5":
        print("Стек повний:", fixed_stack.is_full())
    elif choice == "6":
        fixed_stack.clear()
        print("Стек очищено.")
    elif choice == "7":
        peeked_value = fixed_stack.peek()
        print("Значення на вершині стеку:", peeked_value)
    elif choice == "0":
        print("Дякую за використання. До побачення!")
        break
    else:
        print("Невірний вибір. Будь ласка, виберіть правильну опцію.")
