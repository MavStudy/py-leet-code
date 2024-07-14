# coding=utf-8
"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1, 1, 2]
Output: [1, 2]

Example 2:
Input: head = [1, 1, 2, 3, 3]
Output: [1, 2, 3]


Constraints:

•  The number of nodes in the list is in the range [0, 300].
•  -100 <= Node.val <= 100
•  The list is guaranteed to be sorted in ascending order.

"""
from typing import Optional

OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


# Definition for singly-listed list.
class ListNode:
    """Класс узла"""
    def __init__(self, val=0, next_node=None):
        """Метод инициализации"""
        self.val = val
        self.next = next_node

    def __str__(self):
        """Метод отображения объектов класса"""
        return str(self.val)


class Solution:
    """Класс решения"""
    def deleteDuplicates(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Class Solution

        :param head: Optional[ListNode]
        :return: Optional[ListNode]
        """
        if not head:
            return None

        current = head
        prev_val = current.val

        while current.next is not None:
            if current.next.val == prev_val:
                current.next = current.next.next
            else:
                prev_val = current.next.val
                current = current.next

        return head  # возврат 1-ого узла


def call_method():
    """
    Function for check

    :return:
    """
    head1_1 = ListNode(1)
    node1_2 = ListNode(1)
    node1_3 = ListNode(2)
    head1_1.next = node1_2
    node1_2.next = node1_3

    separator()
    obj = Solution()
    print("Input: ", end='')
    print_list(head1_1)
    print()
    separator()
    head1_1 = obj.deleteDuplicates(head1_1)
    print(OUTPUT, end='')
    print_list(head1_1)
    print()
    separator()


def print_list(node: ListNode):
    """
    Функция вывода на печать связанного списка.\n
    Хотя у функции есть ссылка на первый узел списка, внутри неё нет
    переменных, ссылающихся на другие узлы. Функция получает ссылку на
    следующий узел, используя значение атрибута next каждого узла.

    :param node: ссылка на первый узел списка.
    :return:
    """
    print("[", end="")  # начало обёртки
    if node is not None:
        while node.next:
            print(node, end=", ")
            node = node.next
        print(node.val, end="")
    print("]", end="")  # конец обёртки


def main():
    """Function main()"""
    call_method()


if __name__ == '__main__':
    main()
