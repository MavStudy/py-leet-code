# coding=utf-8
"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.


Example 1:
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: true

Example 2:
Input: p = [1, 2], q = [1, null, 2]
Output: false

Example 3:
Input: p = [1, 2, 1], q = 1, 1, 2]
Output: false


Constraints:

•  The number of nodes in the tree is in the range [0, 100].
•  -10^4 <= Node.val <= 10^4

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


class Solution:
    """Класс решения"""
    def __init__(self):
        self.out = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # если связные списки p и q пустые
            return True

        if not p or not q:  # если пустой только один связный список
            return False

        if p.val != q.val:  # если значения в соответствующих узлах связных
            # списков не равны
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # return left == right == True
        return left is True and right is True


def main():
    """Function main()"""
    # p = [1, 2, 3]
    p = TreeNode(1)
    p1_l = TreeNode(2)
    p1_r = TreeNode(3)
    p.left = p1_l
    p.right = p1_r
    # q = [1, 2, 3]
    q = TreeNode(1)
    q1_l = TreeNode(2)
    q1_r = TreeNode(3)
    q.left = q1_l
    q.right = q1_r

    obj = Solution()

    result = obj.isSameTree(p, q)
    print(result)

    # p = [1, 2]
    p = TreeNode(1)
    p1_l = TreeNode(2)
    p.left = p1_l
    # q = [1, null, 2]
    q = TreeNode(1)
    q1_r = TreeNode(2)
    q.right = q1_r

    result = obj.isSameTree(p, q)
    print(result)

    # p = [1, 2, 1]
    p = TreeNode(1)
    p1_l = TreeNode(2)
    p1_r = TreeNode(1)
    p.left = p1_l
    p.right = p1_r
    # q = [1, 1, 2]
    q = TreeNode(1)
    q1_l = TreeNode(1)
    q1_r = TreeNode(2)
    q.left = q1_l
    q.right = q1_r

    result = obj.isSameTree(p, q)
    print(result)


if __name__ == '__main__':
    main()
