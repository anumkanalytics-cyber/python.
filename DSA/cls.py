class Stack:

    def __init__(self):
        self.items = []#internal list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("stack (top > bottom:)", self.items[::-1])

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("after pushing 10, 20, 30,")
s.display()
print("top element", s.peek())
print("popped element", s.pop())
print("After element")
s.display()
print("total size", s.size())
print("is stack emplty?", s.is_empty())

        