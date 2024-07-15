# encoding=utf-8
"""
Stack implementation
"""


class Stack:
    """Реализация стека"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """checking the stack for emptiness"""
        # return self.items == []
        return bool(self.items) is False

    def push(self, item):
        """push  item to stack"""
        self.items.append(item)

    def pop(self):
        """pop item from stack"""
        return self.items.pop()

    def peek(self):
        """show the top of the stack"""
        return self.items[len(self.items) - 1]

    def size(self):
        """get size of the stack"""
        return len(self.items)


def main():
    """Main function"""
    s = Stack()
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
