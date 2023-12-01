# Завдання 1
# Реалізуйте клас стека роботи з цілими значеннями (стек цілих). Стек має бути не фіксованого розміру.
# Реалізуйте набір операцій для роботи зі стеком o розміщення цілого значення у стеку;
# o виштовхування цілого значення зі стеку;
# o підрахунок кількості цілих у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування верхнього цілого в стеку.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def get_top_without_pop(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

stack = Stack()

while True:
    print("\nМеню:")
    print("1. Додати елемент у стек")
    print("2. Виштовхнути елемент зі стеку")
    print("3. Підрахунок кількості елементів у стеці")
    print("4. Перевірка, чи порожній стек")
    print("5. Очищення стеку")
    print("6. Отримання значення верхнього елементу без виштовхування")
    print("7. Вихід")

    choice = input("Введіть номер операції: ")

    if choice == "1":
        item = int(input("Введіть ціле значення для додавання у стек: "))
        stack.push(item)
    elif choice == "2":
        print("Виштовхнутий елемент:", stack.pop())
    elif choice == "3":
        print("Кількість елементів у стеці:", stack.size())
    elif choice == "4":
        print("Чи порожній стек:", stack.is_empty())
    elif choice == "5":
        stack.clear()
        print("Стек очищено.")
    elif choice == "6":
        print("Значення верхнього елементу без виштовхування:", stack.get_top_without_pop())
    elif choice == "7":
        print("Дякую за використання програми. Вихід.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")


