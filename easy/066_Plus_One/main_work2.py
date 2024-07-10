# coding=utf-8
"""
66. Plus One

You are given a large integer represented as an integer array digits, where
each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
nput: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

-  1 <= digits.length <= 100
-  0 <= digits[i] <= 9
-  digits does not contain any leading 0's.




"""
from typing import List

OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:
    """Класс решения"""
    def plus_one(self, digits: List[int]) -> List[int]:
        """

        :param digits: a large integer represented as an integer array digits,
               where each digits[i] is the ith digit of the integer.
        :return: the resulting array of digits after increment the large
               integer by one.
        """
        adding = False
        for i, digit in enumerate(digits[::-1]):
            # print(i, digit)
            if digit > 8:
                digits[-i - 1] = 0
                adding = True
            else:
                digits[-i - 1] = digit + 1
                adding = False
                break
        if adding:
            digits.insert(0, 1)
        return digits


def call_check(digits: List[int]):
    """

    :param digits: a large integer represented as an integer array digits
    :return:
    """
    obj = Solution()
    print(f"Input: {digits = }")
    print(OUTPUT, end='')
    result = obj.plus_one(digits)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check([1, 2, 3])
    separator()
    call_check([4, 3, 2, 1])
    separator()
    call_check([9])
    separator()
    call_check([9, 9])
    separator()


if __name__ == '__main__':
    main()
