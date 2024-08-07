# coding=utf-8
"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).
Учитывая корень бинарного дерева, проверьте, является ли оно зеркальным
отражением самого себя (т.е. симметричным относительно своего центра).

Example 1:
Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: true

Example 2:
Input: root = [1, 2, 2, null, 3, null, 3]
Output: false

Constraints:

•  The number of nodes in the tree is in the range [0, 1000].
•  -100 <= Node.val <= 100

https://www.tutorialspoint.com/symmetric-tree-in-python

"""
from typing import Optional

OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


# Definition for a binary tree node.
class TreeNode:
    """TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_node(tree, value):
    """
    Добавления узла в дерево

    :param tree:
    :param value:
    :return:
    """
    curlevel_tree_nodes = []
    curlevel_tree_nodes.append(tree)

    # if curlevel_tree_nodes:  # [use-implicit-booleaness-not-len]
    # while len(curlevel_tree_nodes):
    while curlevel_tree_nodes:  # [use-implicit-booleaness-not-len]
        tree_node = curlevel_tree_nodes[0]
        curlevel_tree_nodes.pop(0)

        if not tree_node.left:
            if value is not None:
                tree_node.left = TreeNode(value)
            else:
                tree_node.left = TreeNode(0)
            break
        curlevel_tree_nodes.append(tree_node.left)

        if not tree_node.right:
            if value is not None:
                tree_node.right = TreeNode(value)
            else:
                tree_node.right = TreeNode(0)
            break
        curlevel_tree_nodes.append(tree_node.right)


def make_tree(values):
    """Функция создания дерева"""
    tree = TreeNode(values[0])
    for value in values[1:]:
        insert_node(tree, value)
    return tree


def in_order_traversal(node):
    """
    Узел посещается после обхода по порядку левого поддерева
    и перед обходом по порядку правого поддерева.

    :param node:
    :return:
    """

    if node is None:
        return
    in_order_traversal(node.left)
    print(node.val, end=", ")
    in_order_traversal(node.right)


def post_order_traversal(node):
    """
    Узел посещается после рекурсивного вызова левого и правого дочерних узлов

    :param node:
    :return:
    """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.val, end=", ")


class Solution:
    """Класс решения"""
    def __init__(self):
        self.out = []

    def is_simmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Функция определения зеркальности дерева

        :param root: корень дерева
        :return: bool: True-дерево зеркально, False-нет
        """
        return self.solve(root, root)

    def solve(self, node1, node2):
        """Функция определения зеркальности узлов"""
        if not node1 and not node2:  # Если оба списка пустые,
            return True  # то списки зеркальные

        if not node1 or not node2:  # Если только один список пустой,
            return False  # списки не зеркальные

        return node1.val == node2.val and \
            self.solve(node1.left, node2.right) and \
            self.solve(node1.right, node2.left)


def main():
    """Function main()"""
    # tree1 = make_tree([1, 2, 2, 3, 4, 4, 3])
    root = [1, 2, 2, 3, 4, 4, 3]
    print(f"Input: root = {root}")
    tree1 = make_tree(root)
    ob = Solution()
    print(ob.is_simmetric(tree1))

    root = [1, 2, 2, None, 3, None, 3]
    print(f"Input: root = {root}")
    tree2 = make_tree(root)
    print(ob.is_simmetric(tree2))

    # in_order_traversal(tree1)


if __name__ == '__main__':
    main()
