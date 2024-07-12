# coding=utf-8
"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
(Вы поднимаетесь по лестнице. Чтобы достичь вершины, требуется n ступенек.)

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top? (Каждый раз вы можете подняться на 1 или 2 ступеньки.
Сколькими различными способами вы можете подняться на вершину?)


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example: n = 3
Input: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""
OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:
    """Класс решения"""
    def climb_stairs(self, n: int) -> int:
        """

        :param n:  steps to reach the top.
        :return: in how many distinct ways can you climb to the top.
        """
        if n == 0:  # если нет ступенек -
            return 0  # возвращаем 0 вариантов
        if n == 1:  # если одна ступенька -
            return 1  # возвращаем только 1 способ
        if n == 2:  # если две ступеньки - возвращаем 2 способа:
            return 2  # 1 -> 1 или сразу 2
        # создание массива из заданного количества ступенек +1
        # в нём будет храниться количество вариантов шагов для очередной
        # ступеньки
        dp = [0] * (n + 1)
        # первую ступеньку можно перешагнуть только одним способом
        dp[1] = 1
        # вторую - уже двумя способами
        dp[2] = 2
        # перебираем все ступеньки, начиная с третьей, потому как пройти
        # первые две, мы уже знаем
        for i in range(3, n + 1):
            # до каждой следующей ступеньки можно добраться одним или двумя
            # шагами с предыдущих
            dp[i] = dp[i - 1] + dp[i - 2]
        # в конце - возвращаем количество вариантов для последней ступеньки
        return dp[n]


def call_check(n: int):
    """
    :param n:
    """
    obj = Solution()
    print(f"Input: {n = }")
    print(OUTPUT, end='')
    result = obj.climb_stairs(n)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check(1)  # 1 ступенька
    separator()
    call_check(2)  # 2 ступеньки
    separator()
    call_check(3)  # 3 ступеньки
    separator()
    call_check(4)  # 4 ступеньки
    separator()
    call_check(5)  # 5 ступенек
    separator()


if __name__ == '__main__':
    main()
