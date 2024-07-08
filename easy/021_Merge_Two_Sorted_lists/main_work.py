# coding=utf-8
"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Example 2:
Input:st1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

-  The number of nodes in both lists is in the range [0, 50].
-  -100 <= Node.val <= 100
-  Both list1 and list2 are sorted in non-decreasing order.

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
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Class Solution

        :param list1: Optional[ListNode]
        :param list2: Optional[ListNode]
        :return: Optional[ListNode]
        """
        head = tail = ListNode()  # 0-й корневой узел результирующего
        # связанного списка, возвращать будем 1-й !!!
        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if not list1:
            tail.next = list2
        else:
            tail.next = list1

        return head.next  # возврат 1-ого узла


def call_method():
    """
    Function for check

    :return:
    """
    node1_1 = ListNode(1)
    node1_2 = ListNode(2)
    node1_3 = ListNode(4)
    node1_1.next = node1_2
    node1_2.next = node1_3
    # print_list(node1_1)

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3
    # print_list(node2_1)

    obj = Solution()
    print("Input: ")
    print("list1 = ", end='')
    print_list(node1_1)
    print(", ", end='')
    print("list2 = ", end='')
    print_list(node2_1)
    print()
    result = obj.mergeTwoLists(node1_1, node2_1)
    print(OUTPUT, end='')
    print_list(result)
    print()

    separator()

    print("Input: list1 = [], list2 = []")
    result2 = obj.mergeTwoLists(None, None)
    print(OUTPUT, end='')
    print_list(result2)
    print()

    separator()

    print("Input: list1 = [], list2 = ", end='')
    node3_1 = ListNode(0)
    print_list(node3_1)
    print()
    result3 = obj.mergeTwoLists(None, node3_1)
    print(OUTPUT, end='')
    print_list(result3)


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
