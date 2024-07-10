# coding=utf-8
"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

-  1 <= a.length, b.length <= 10^4
-  a and b consist only of '0' or '1' characters.
-  Each string does not contain leading zeros except for the zero itself.


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
    def add_binary(self, a: str, b: str) -> str:
        """
        :param a: binary string
        :param b: binary string
        :return: return their(a and b) sum as a binary string
        """
        a_10 = int("0b" + a, 2)
        b_10 = int("0b" + b, 2)
        result = format(a_10 + b_10, 'b')
        return str(result)


def call_check(a: str, b: str):
    """
    :param a:
    :param b:
    """
    obj = Solution()
    print(f"Input: {a = }, {b = }")
    print(OUTPUT, end='')
    result = obj.add_binary(a, b)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check("11", "1")
    separator()
    call_check("1010", "1011")
    separator()


if __name__ == '__main__':
    main()
