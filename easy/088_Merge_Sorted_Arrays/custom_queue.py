# encoding=utf-8
"""
Queue implementation
"""


class Queue:
    """Реализация очереди"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """checking the queue for emptiness"""
        # return self.items == []
        return bool(self.items) is False

    def enqueue(self, item):
        """queuing an item"""
        self.items.insert(0, item)

    def dequeue(self):
        """removing an item from the queue"""
        return self.items.pop()

    def peek(self):
        """show the top of the queue"""
        return self.items[len(self.items) - 1]

    def size(self):
        """get size of the queue"""
        return len(self.items)


def main():
    """Main function"""
    q = Queue()
    print(q.isEmpty())  # True
    q.enqueue('dog')  # ['dog']
    q.enqueue(4)  # [4, 'dog']
    print(q.peek())  # dog
    print(q.items)  # [4, 'dog']
    q.enqueue(True)  # [True, 4, 'dog']
    print(q.size())  # 3
    print(q.isEmpty())  # False
    q.enqueue(8.4)  # [8.4, True, 4, 'dog']
    print(q.dequeue())  # dog
    print(q.dequeue())  # 4
    print(q.size())  # 2


if __name__ == '__main__':
    main()
