# coding=utf-8
"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

-  1 <= haystack.length, needle.length <= 10^4
-  haystack and needle consist of only lowercase English characters.

"""
OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:  # не прошёл проверку!
    """Класс решения"""
    def str_str(self, haystack: str, needle: str) -> int:
        """
        Function of the Find the Index of the First Occurrence in a String

        :param haystack: стог сена
        :param needle: иголка
        :return: the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack
        """
        return haystack.find(needle)


def call_method():
    """
    Function for check

    :return:
    """
    separator()

    obj = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(f"Input: {haystack = }, {needle = }")
    print(OUTPUT, end='')
    result = obj.str_str(haystack, needle)
    print(result)
    separator()

    haystack = "leetcode"
    needle = "leeto"
    print(f"Input: {haystack = }, {needle = }")
    print(OUTPUT, end='')
    result = obj.str_str(haystack, needle)
    print(result)
    separator()


def main():
    """Function main()"""
    call_method()


if __name__ == '__main__':
    main()
