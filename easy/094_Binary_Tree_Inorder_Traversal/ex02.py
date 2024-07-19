# https://www.w3schools.com/dsa/dsa_data_binarytrees.php
# https://www.w3schools.com/dsa/dsa_algo_binarytrees_inorder.php


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
In-order Traversal does a recursive In-order Traversal of the left subtree, 
visits the root node, and finally, does a recursive In-order Traversal of the 
right subtree. This traversal is mainly used for Binary Search Trees where it 
returns values in ascending order. (При обходе по порядку выполняется 
рекурсивный обход по порядку левого поддерева, посещается корневой узел и, 
наконец, выполняется рекурсивный обход по порядку правого поддерева. Этот обход
в основном используется для бинарных деревьев поиска, где он возвращает 
значения в порядке возрастания.)

What makes this traversal "in" order, is that the node is visited in between 
the recursive function calls. The node is visited after the In-order Traversal
of the left subtree, and before the In-order Traversal of the right subtree.
(Что делает этот обход "упорядоченным", так это то, что узел посещается в 
промежутках между вызовами рекурсивных функций. Узел посещается после обхода по
порядку левого поддерева и перед обходом по порядку правого поддерева.)
"""
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def main():
    root = TreeNode('R')
    nodeA = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')

    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

    # Test
    print("root.right.left.data:", root.right.left.data)

    inOrderTraversal(root)


if __name__ == '__main__':
    main()
"""
C, A, D, R, E, B, G, F, 
"""