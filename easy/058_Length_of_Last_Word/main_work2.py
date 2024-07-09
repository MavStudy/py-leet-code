# coding=utf-8
"""
58. Length of LastWord

Given a string s consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

-  1 <= s.length <= 10^4
-  s consists of only English letters and spaces ' '.
-  There will be at least one word in s.


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
    def length_of_last_word(self, s: str) -> int:
        """

        :param s: a string s consisting of words and spaces.
        :return: the length of the last word in the string. A word is
                 a maximal substring consisting of non-space characters only.
        """
        word = s.rstrip().split()[-1]
        return len(word)


def call_check(s: str):
    """
    Function for check work method Solution.length_of_last_word()

    :param s:  a string s consisting of words and spaces
    :return: return the length of the last word in the string. A word is
             a maximal substring consisting of non-space characters only.
    """
    obj = Solution()
    print(f"Input: {s = }")
    print(OUTPUT, end='')
    result = obj.length_of_last_word(s)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check("Hello World")
    separator()
    call_check("   fly me   to   the moon  ")
    separator()
    call_check("luffy is still joyboy")
    separator()


if __name__ == '__main__':
    main()
