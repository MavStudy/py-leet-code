# coding=utf-8
"""
94. Binary Tree Inorder Traversal
(Обход бинарного дерева по порядку)

Given the root of a binary tree, return the inorder traversal of its nodes'
values. (Учитывая корень двоичного дерева, верните обход значений его узлов
в порядке убывания.)


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:

•  The number of nodes in the tree is in the range [0, 100].
•  -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
(Рекурсивное решение тривиально, не могли бы вы сделать это итеративно?)

"""
from typing import List, Optional

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


class Solution:
    """Класс решения"""
    def __init__(self):
        """__init__ method"""
        self.out = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """

        :param root: the root binary tree
        :return result: return the inorder traversal of its node's values.
                (возвращает обход значений данного узла в порядке убывания)
        """
        if root is None:
            return self.out
        self.inorderTraversal(root.left)
        if root.val is not None:
            self.out.append(root.val)
        self.inorderTraversal(root.right)

        return self.out


def main():
    """Function main()"""
    # root = [1, None, 2, 3]
    root = TreeNode(1)
    nodeA = TreeNode(None)
    nodeB = TreeNode(2)
    nodeC = TreeNode(3)
    root.left = nodeA
    root.right = nodeB
    nodeB.left = nodeC

    obj = Solution()
    result = obj.inorderTraversal(root)
    print(result)

    root2 = TreeNode(None)
    obj2 = Solution()
    result2 = obj2.inorderTraversal(root2)
    print(result2)

    root3 = TreeNode(1)
    obj3 = Solution()
    result3 = obj3.inorderTraversal(root3)
    print(result3)


if __name__ == '__main__':
    main()
