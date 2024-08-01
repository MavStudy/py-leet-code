# coding=utf-8
# Реализация банарного дерева на Python | Структуры данных
# Обучающий курс: https://stepic.org/a/134212
# Инфо-сайт: https://proproprogs.ru/structure_data
# Пример реализации бинарного дерева на языке Python. Добавление/удаление
# вершин дерева, обход дерева в глубину и ширину


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None  # фактически, листовая вершина


class Tree:
    def __init__(self):
        self.root = None  # изначально бинарное дерево создаётся пустым

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:  # если value равно значению в текущей вершине
            return node, parent, True  # True - нашли то значение, которое
            # хотели добавить

        if value < node.data:  # если значение меньше хранимого в текущем узле
            if node.left:
                return self.__find(node.left, node, value)
        else:  # if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False  # не нашли вершину с соответствующим
        # значением value

    def append(self, obj: Node):
        if self.root is None:  # Если бинарное дерево пустое(нет объектов),
            self.root = obj  # тогда новая вершина добавляется как корневая
            return obj

        # необходимо найти вершину, к которой затем добавим новую вершину
        s, p, fl_find = self.__find(
            self.root,  # корень
            None,  # родительская вершина-её нет у корня
            obj.data  # данные в объекте obj, т.е. те данные, относительно
            # которых будем искать вершину для прикрепления
        )

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj  # возвращаем объект, который добавили

    def show_tree(self, node):
        """Алгоритм обхода в глубину"""
        if node is None:
            return

        self.show_tree(node.left)  # если поменять местами node.left и
        print(node.data)
        self.show_tree(node.right)  # node.right, то будет убывающая
        # последовательность

    def show_wide_tree(self, node):
        """Алгоритм отображения бираного дерева в ширину"""
        if node is None:
            return

        v = [node]  # список вершин для текущего уровня
        while v:  # пока эти вершины существуют
            vn = []  # новый список для вершин следующего уровня
            for x in v:  # перебираем вершины текущего уровня
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()  # перенос курсора на следующую строку
            v = vn

    def __del_leaf(self, s, p):
        """Функция удаления листовой вершины"""
        if p.left == s:  # если вершина s подцеплена к левой ветви
            p.left = None
        elif p.right == s:  # а если s подцеплена к правой ветви
            p.right = None

    def __del_one_child(self, s, p):
        """Функция удаления вершины, имеющий одного потомка"""
        # удаляемая вершина подцеплена к левой ветви
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        # удаляемая вершина подцеплена к правой ветви
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        """Функция удаления вершины со значением key"""
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:  # вершина со значением key не была найдена, поэтому
            return None  # удалять нечего

        # 1-я ситуация - удаляемая вершина s листовая
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)  # s-удаляемая вершина, p-родительская вершина
        # 2-я ситуаця - удаляем вершину либо с левым, либо с правым потомком
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        # 3-я ситуация - удаляем вершину с двумя потомками
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


def main():
    v = [10, 5, 7, 16, 13, 2, 20]
    # v = [20, 5, 24, 2, 16, 11, 18]

    t = Tree()
    for x in v:
        t.append(Node(x))

    t.show_tree(t.root)
    print('-' * 60)
    # t.del_node(5)
    # t.show_tree(t.root)
    # print('-' * 60)
    t.show_wide_tree(t.root)
    print('-' * 60)


if __name__ == '__main__':
    main()
