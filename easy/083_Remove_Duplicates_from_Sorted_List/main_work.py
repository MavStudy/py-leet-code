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


def check_method(head: ListNode):
    """
    Function for check

    :return:
    """
    separator()
    obj = Solution()
    print("Input: head = ", end='')
    print_list(head)
    print()
    separator()
    head = obj.deleteDuplicates(head)
    print(OUTPUT, end='')
    print_list(head)
    print()


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
    head1_1 = ListNode(1)
    node1_2 = ListNode(1)
    node1_3 = ListNode(2)
    head1_1.next = node1_2
    node1_2.next = node1_3
    check_method(head1_1)

    head2_1 = ListNode(1)
    head2_2 = ListNode(1)
    head2_3 = ListNode(2)
    head2_4 = ListNode(3)
    head2_5 = ListNode(3)
    head2_1.next = head2_2
    head2_2.next = head2_3
    head2_3.next = head2_4
    head2_4.next = head2_5
    check_method(head2_1)

    head3_1 = ListNode(7)
    check_method(head3_1)

    check_method(None)


if __name__ == '__main__':
    main()
