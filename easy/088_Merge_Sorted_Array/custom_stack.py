# encoding=utf-8


class Stack:
    """Реализация стека"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def main():
    s= Stack()
    print(s.isEmpty())  # True
    s.push(4)  # [4]
    s.push('dog')  # [4, 'dog']
    print(s.peek())
    s.push(True)  # [4, 'dog', True]
    print(s.size())  # 3
    print(s.isEmpty())  # False
    s.push(8.4)  # [4, 'dog', True, 8.4]
    print(s.pop())  # 8.4
    print(s.pop())  # True
    print(s.size())  # 2

if __name__ == '__main__':
    main()
