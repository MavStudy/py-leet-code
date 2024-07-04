"""Изучаем связанные списки - ex03.py"""


class LinkedList:
    """
    Класс LinkedList. Его атрибутами будут целое число, представляющее длину
    списка, и ссылка на первый узел списка. С помощью объектов LinkedList
    удобно манипулировать списками объектов ListNode
    """
    def __init__(self):
        self.length = 0
        self.head = None

    # Класс LinkedList оказывается удобным местом для помещения в него таких
    # функций, как print_backward_nicely, и превращения их в методы этого
    # класса.

    def print_backward(self):
        """
        Переименованный метод print_backward_nicely. Теперь у нас два метода
        print_backward: один в классе Node (помощник), и один в классе
        LinkedList (обертка). Когда метод-обертка вызывает
        self.head.print_backward, он вызывает метод-помощник, поскольку
        self.head ссылается на объект Node.

        :return:
        """
        print("[", end="")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def print_list(self):
        print("[", end="")  # начало обёртки
        last_node = self.head
        while last_node.next:
            print(last_node.val, end=", ")
            last_node = last_node.next
        print(last_node.val, end="")
        print("]")  # конец обёртки

    def add_first(self, val):
        """
        Метод add_first класса LinkedList принимает в качестве аргумента
        данные для узла и помещает новый узел с этими данными в начало списка.

        :param val:
        :return:
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def find(self, val) -> bool:
        """
        Метод find(self, val) для поиска в списке узла с val, ближайшего
        к началу списка.

        :param val: данные в узле
        :return:
        """
        last_node = self.head
        while last_node:
            if val == last_node.val:
                return True
            last_node = last_node.next
        return False

    def last(self):
        """Метод нахождения последнего узла в связанном списке"""
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node

    def append(self, new_val):
        """
        Метод для добавления узла в конец списка.\n
        Для начала новый узел создать. А затем поместить в него данные val.

        :param new_val: данные в узле
        :return:
        """
        # Для начала новый узел создать. А затем поместить в него данные val.
        new_node = ListNode(new_val)

        # После необходимо проверять начиная с начала связного списка, есть ли
        # в текущем узле ссылка на следующий.
        # Если ссылки нет - узел последний. Значит нужно создать ссылку на
        # следующий узел и помещать в него new_node
        if self.head is None:
            self.head = new_node
            return
        # Если ссылка есть - находим последний узел в связанном списке.
        last_node = self.last()
        last_node.next = new_node

    def reverse(self):
        """Reverse a Linked List"""
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


class ListNode:
    """Узел связанного списка"""
    def __init__(self, val=None, next_node=None):
        """
        Параметры инициализирующего метода опциональны. По умолчанию и данные,
        val, и ссылка, next_node получают значения None.

        :param val:
        :param next_node:
        """
        self.val = val
        self.next = next_node

    def __str__(self):
        """
        Метод отображения объектов класса. Строковым представлением узла будет
        строковое представление данных этого узла. Поскольку функции str можно
        передать любое значение, в узле можно будет хранить любое значение.
        :return:
        """
        return str(self.val)

    def print_backward(self):
        """Метод вывода узлов списка в обратном порядке."""
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.val, end=', ')


def main():
    """
    Function main

    :return:
    """
    # для тестирования создадим объект LinkedList, добавив в него три узла
    # и выведем его на печать в обратном порядке.
    ll = LinkedList()

    ll.add_first(1)
    ll.add_first(2)
    ll.add_first(3)
    ll.print_backward()
    ll.print_list()


if __name__ == '__main__':
    main()
