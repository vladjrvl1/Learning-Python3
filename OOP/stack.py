class Stack:
    def __init__(self):
        self.values = []
    
    def push(self, item):
        self.values += [item]

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            value = self.values[-1]
            del self.values[-1]
            return value

    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        return False if self.values else True

    def size(self):
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
