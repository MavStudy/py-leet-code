"""
13. Roman to Integer
Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II. (Например, римскими цифрами 2 записывается как II, просто
две единицы складываются вместе. 12 записывается как XII, что означает просто
X + II. Число 27 записывается как XXVII, что означает XX + V + II.)

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
romans where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Римские цифры обычно пишутся от наибольшего к наименьшему слева направо. Однако
число, обозначающее четыре, не является IIII. Вместо этого число четыре
записывается как IV. Поскольку единица стоит перед пятью, мы вычитаем ее,
и получается четыре. Тот же принцип применим к числу девять, которое
записывается как IX. Существует шесть случаев, когда используется вычитание.


Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
from collections import deque


def separator():
    print('-' * 50)


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :param s: str
        :return: int
        """
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
        items = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        def oneCharNumber(char: str) -> int:
            """
            :param char:
            :return: int
            """
            nonlocal romans
            if char == 'I':
                return romans['I']
            elif char == 'V':
                return romans['V']
            elif char == 'X':
                return romans['X']
            elif char == 'L':
                return romans['L']
            elif char == 'C':
                return romans['C']
            elif char == 'D':
                return romans['D']
            elif char == 'M':
                return romans['M']

        def twoCharNumber(subStr: str) -> int:
            """
            :param subStr:
            :return: int
            """
            nonlocal items
            if subStr == 'IV':
                return items['IV']
            elif subStr == 'IX':
                return items['IX']
            elif subStr == 'XL':
                return items['XL']
            elif subStr == 'XC':
                return items['XC']
            elif subStr == 'CD':
                return items['CD']
            elif subStr == 'CM':
                return items['CM']

        if len(s) == 1:
            return oneCharNumber(s)

        digits = deque()
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                print(f"{len(s) = }")
                sub_str = s[i] + s[i + 1]
                print(sub_str)
                number = twoCharNumber(sub_str)
                if number is None:
                    digits.appendleft(oneCharNumber(s[i]))
                    i = i + 1
                else:
                    digits.appendleft(number)
                    i = i + 2
            else:
                digits.appendleft(oneCharNumber(s[i]))
                i = i + 1

        return sum(list(digits))


def call_method():
    obj = Solution()

    s = "III"
    print(f"Input: {s = }")
    result = obj.romanToInt(s)
    print(f"Output: {result = }")
    separator()

    s = "LVIII"
    print(f"Input: {s = }")
    result = obj.romanToInt(s)
    print(f"Output: {result = }")
    separator()

    s = "MCMXCIV"
    print(f"Input: {s = }")
    result = obj.romanToInt(s)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()
