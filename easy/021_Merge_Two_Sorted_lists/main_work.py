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


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


# Definition for singly-listed list.
class ListNode:
    def __init__(self, val=0, next=None):
        """Метод инициализации"""
        self.val = val
        self.next = next

    def __str__(self):
        """Метод отображения объектов класса"""
        return str(self.val)


class LinkedList:
    """Связанный список"""
    def __init__(self, head=None):
        self.head = ListNode

    def print_list(self):
        while self.head:
            print(self.head)
            self.head =
        print()


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]) -> Optional[ListNode]:

        return []



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
    ll_1 = LinkedList(node1_1)
    ll_1.print_list()

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3
    ll_2 = LinkedList(node2_1)
    ll_2.print_list()


    # obj = Solution()


def main():
    """Function main()"""
    call_method()


if __name__ == '__main__':
    main()
