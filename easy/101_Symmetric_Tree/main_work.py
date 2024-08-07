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
    curlevel_tree_nodes = []
    curlevel_tree_nodes.append(tree)
    while curlevel_tree_nodes:
        tree_node = curlevel_tree_nodes[0]
        curlevel_tree_nodes.pop(0)

        if not tree_node.left:
            if value is not None:
                tree_node.left = TreeNode(value)
            else:
                tree_node.left = TreeNode(0)
            break
        else:
            curlevel_tree_nodes.append(tree_node.left)

        if not tree_node.right:
            if value is not None:
                tree_node.right = TreeNode(value)
            else:
                tree_node.right = TreeNode(0)
            break
        else:
            curlevel_tree_nodes.append(tree_node.right)


def make_tree(values):
    """Функция создания дерева"""
    tree = TreeNode(values[0])
    for value in values[1:]:
        insert_node(tree, value)
    return tree


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.val, end=", ")
    inOrderTraversal(node.right)


def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.val, end=", ")


class Solution:
    """Класс решения"""
    def __init__(self):
        self.out = []

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """

        :param root: корень дерева
        :return: bool: True-дерево зеркально, False-нет
        """
        return self.solve(root, root)

    def solve(self, node1, node2):
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
    print(ob.isSymmetric(tree1))

    root = [1, 2, 2, None, 3, None, 3]
    print(f"Input: root = {root}")
    tree2 = make_tree(root)
    print(ob.isSymmetric(tree2))

    # inOrderTraversal(tree1)


if __name__ == '__main__':
    main()
