# coding=utf-8
"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the
nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example: x = 8
Input: 2
Output: Explanation: The square root of 8 is 2.82842..., and since we round it
down to the nearest integer, 2 is returned.


Constraints:

-  0 <= x <= 2^31 - 1

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
    def mySqrt(self, x: int) -> int:
        """

        :param x: a non-negative integer
        :return: the square root of x rounded down to the nearest integer.
                 The returned integer should be non-negative as well.
        """
        cur_num = low = 0
        while low <= x:
            guess = low
            x_power = low * low
            if x_power == x:
                return guess
            if x_power > x:
                return cur_num
            cur_num = low
            low += 1

        return cur_num


def call_check(x: int):
    """
    :param x:
    """
    obj = Solution()
    print(f"Input: {x = }")
    print(OUTPUT, end='')
    result = obj.mySqrt(x)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check(0)
    separator()
    call_check(1)
    separator()
    call_check(4)
    separator()
    call_check(8)
    separator()


if __name__ == '__main__':
    main()
