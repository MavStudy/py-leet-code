# https://www.w3schools.com/dsa/dsa_data_binarytrees.php
# https://www.w3schools.com/dsa/dsa_algo_binarytrees_postorder.php



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
Post-order Traversal works by recursively doing a Post-order Traversal of the 
left subtree and the right subtree, followed by a visit to the root node. It is
used for deleting a tree, post-fix notation of an expression tree, etc.
(Последующий обход работает путем рекурсивного выполнения последующего обхода 
левого поддерева и правого поддерева с последующим посещением корневого узла. 
Он используется для удаления дерева, постфиксной записи дерева выражений и т.д.)

What makes this traversal "post" is that visiting a node is done "after" the 
left and right child nodes are called recursively. (Что делает этот обход 
"постзаказным", так это то, что посещение узла выполняется "после" рекурсивного
вызова левого и правого дочерних узлов)

"""
def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")


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

    postOrderTraversal(root)


if __name__ == '__main__':
    main()
"""
C, D, A, E, G, F, B, R, 
"""