# https://www.w3schools.com/dsa/dsa_data_binarytrees.php
# https://www.w3schools.com/dsa/dsa_algo_binarytrees_preorder.php


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
Pre-order Traversal is done by visiting the root node first, then recursively 
do a pre-order traversal of the left subtree, followed by a recursive pre-order
traversal of the right subtree. It's used for creating a copy of the tree, 
prefix notation of an expression tree, etc. (предварительный обход заказа 
выполняется путем первого посещения корневого узла, затем рекурсивного 
предварительного обхода левого поддерева, за которым следует рекурсивный 
предварительный обход правого поддерева. Он используется для создания копии 
дерева, префиксной записи дерева выражений и т.д.)

This traversal is "pre" order because the node is visited "before" the 
recursive pre-order traversal of the left and right subtrees. (Этот обход 
является "предварительным" порядком, поскольку узел посещается "до" 
рекурсивного предварительного обхода левого и правого поддеревьев.)
"""
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)


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

    preOrderTraversal(root)


if __name__ == '__main__':
    main()
"""
R, A, C, D, B, E, F, G, 
"""