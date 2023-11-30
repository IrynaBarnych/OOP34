#стек - загальне поняття через список
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
print(stack[-1])#peek()
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque

#порожній стек
stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())

from queue import LifoQueue

stack = LifoQueue(maxsize=3)
print(stack.qsize())#кількість елементів
stack.put("a")
stack.put("b")
stack.put("c")

print(stack.full())
print(stack.qsize())#кількість елементів
for i in range(stack.qsize()):
    print(stack.get())

#за допомогою однозв'язного списку
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        return out[:-4]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("стек порожній, неможливо продивитися")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("стек порожній, неможливо видалити")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

stack = Stack()
for i in range(1, 11):
    stack.push(i)
print(stack)
print(stack.pop())
print(stack.peek())
print(stack)

# Стек за допомогою класів

class Stack:
    def __init__(self):
        self.items = []

    def is_emty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_emty():
            return self.items.pop()
        else:
            return "Стек пустий!"

    def peek(self):
        if not self.is_emty():
            return self.items[-1]
        else:
            return "Стек пустий!"
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.pop())
print(stack.peek())

#практика

def chack_brackets(text):
    stack = []
    for char in text:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or not is_matching(stack.pop(), char):
                return False
    return len(stack) == 0
def is_matching(opening, closing):
    return opening == '(' and closing == ')' or \
           opening == '{' and closing == '}' or \
           opening == '[' and closing == ']'

test = ["()", "[[{}]]", "{[}]", "((())"]
for t in test:
    result = chack_brackets(t)
    print(result)
