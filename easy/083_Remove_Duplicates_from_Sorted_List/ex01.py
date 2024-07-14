# coding=utf-8
"""
Study linked list

Materials:
https://statisticsglobe.com/delete-node-linked-list-python
"""


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


def print_list(list_head):
    """Print of the list"""
    while list_head:
        print(list_head.val)
        list_head = list_head.next


#
# Step 1: Traverse the linked list to find the node to be deleted.
#         (Пройдитесь по связанному списку, чтобы найти узел, который нужно
#         удалить.)
# Step 2: Update the links to bypass the node to be deleted.
#         (Обновите ссылки, чтобы обойти узел, подлежащий удалению.)
#
# Step 3: Free the memory occupied by the deleted node (In Python garbage
#         collection is done automatically)
#         (Освободите память, занятую удаленным узлом (в Python сборка мусора
#         выполняется автоматически).
#
def delete_node(list_head, val):
    """

    :param list_head:
    :param val:
    :return:
    """
    if list_head is None:
        return list_head

    if list_head == val:
        return list_head.next

    current = list_head
    while current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
            break
        current = current.next

    return list_head


def main():
    """Function main()"""
    # Create a linked list
    separator()
    head = ListNode(10)
    node2 = ListNode(20)
    node3 = ListNode(30)
    head.next = node2
    node2.next = node3
    print_list(head)
    separator()
    # Delete a node with value 20
    head = delete_node(head, 20)

    # Print the updated linked list
    print_list(head)
    separator()


if __name__ == '__main__':
    main()
