# https://www.w3schools.com/dsa/dsa_data_binarytrees.php
# https://www.w3schools.com/dsa/dsa_data_binarytrees_arrayImpl.php
"""
Array Implementation of Binary Trees
(Массивная реализация бинарных деревьев)

To avoid the cost of all the shifts in memory that we get from using Arrays, it
is useful to implement Binary Trees with pointers from one element to the next,
just like Binary Trees are implemented before this point, especially when the
Binary Tree is modified often.
(Чтобы избежать затрат на все изменения в памяти, которые мы получаем при
использовании массивов, полезно реализовать двоичные деревья с указателями от
одного элемента к другому, точно так же, как двоичные деревья были реализованы
до этого момента, особенно когда двоичное дерево часто модифицируется.)

But in case we read from the Binary Tree a lot more than we modify it, an Array
implementation of a Binary Tree can make sense as it needs less memory, it can
be easier to implement, and it can be faster for certain operations due to
cache locality.
(Но в случае, если мы читаем из двоичного дерева намного больше, чем
модифицируем его, реализация двоичного дерева в виде массива может иметь смысл,
поскольку для этого требуется меньше памяти, это может быть проще в реализации
и может быть быстрее для определенных операций из-за локальности кэша.)


Cache Locality is when the fast cache memory in the computer stores parts of
memory that was recently accessed, or when the cache stores parts of memory
that is close to the address that is currently accessed. This happens because
it is likely that the CPU needs something in the next cycle that is close to
what it used in the previous cycle, either close in time or close in space.
(Локальность кэша - это когда в быстрой кэш-памяти компьютера хранятся части
памяти, к которым недавно осуществлялся доступ, или когда в кэше хранятся части
памяти, расположенные близко к адресу, к которому осуществляется доступ в
данный момент. Это происходит потому, что, вероятно, в следующем цикле
процессору потребуется что-то близкое к тому, что он использовал в предыдущем
цикле, либо близкое по времени, либо близкое по пространству.)

Since Array elements are stored contiguously in memory, one element right after
the other, computers are sometimes faster when reading from Arrays because the
next element is already cached, available for fast access in case the CPU needs
it in the next cycle.
(Поскольку элементы массива хранятся в памяти последовательно, один элемент
сразу за другим, компьютеры иногда работают быстрее при чтении из массивов,
поскольку следующий элемент уже кэширован и доступен для быстрого доступа в
случае, если он понадобится центральному процессору в следующем цикле.)
"""

"""
This Binary Tree can be stored in an Array starting with the root node R on 
index 0. The rest of the tree can be built by taking a node stored on index i, 
and storing its left child node on index 2⋅i+1, and its right child node on
index 2⋅i+2.
(Это двоичное дерево может храниться в массиве, начинающемся с корневого узла 
R с индексом 0. Остальную часть дерева можно построить, взяв узел, хранящийся 
в индексе i, и сохранив его левый дочерний узел в индексе 2⋅i+1 и его правый 
дочерний узел по индексу 2⋅i+2.) 
"""
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None,
                     None, None, 'G']


def left_child_index(index):
    return 2 * index + 1


def right_child_index(index):
    return 2 * index + 2


def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None


def main():
    right_child = right_child_index(0)
    left_child_of_right_child = left_child_index(right_child)
    data = get_data(left_child_of_right_child)

    print("root.right.left.data:", data)


if __name__ == '__main__':
    main()
"""
root.right.left.data: E
"""