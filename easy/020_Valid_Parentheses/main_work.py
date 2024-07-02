"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.


Hint 1
Use a stack of characters.

Hint 2
When you encounter an opening bracket, push it to the top of the stack.

Hint 3
When you encounter a closing bracket, check if the top of the stack was
the opening for it. If yes, pop it from the stack. Otherwise, return false.
"""


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:
    def isValid(self, s: str) -> bool:
        """
        The function of determining the validity of a string

        :param s: The input line consists of parentheses only '()[]{}'
        :return: True if the input string is valid, otherwise False.
        """
        appropriate = {'}': '{', ']': '[', ')': '('}
        stack = list()

        for i in range(len(s)):
            # print(i, s[i])
            type_of_bracket = appropriate.get(s[i], 0)
            if type_of_bracket:  # closing bracket
                if not len(stack):
                    return False
                if stack[-1] == appropriate.get(s[i]):
                    stack.pop()
                else:
                    return False
            else:  # opening bracket
                stack.append(s[i])

        if stack:
            return False
        else:
            return True


def call_method():
    """
    Function for check

    :return:
    """
    obj = Solution()

    s = "{[("
    print(f"Input: {s = }")
    result = obj.isValid(s)
    print(f"Output: {result = }")
    separator()

    s = "()"
    print(f"Input: {s = }")
    result = obj.isValid(s)
    print(f"Output: {result = }")
    separator()

    s = "()[]{}"
    print(f"Input: {s = }")
    result = obj.isValid(s)
    print(f"Output: {result = }")
    separator()

    s = "(]"
    print(f"Input: {s = }")
    result = obj.isValid(s)
    print(f"Output: {result = }")
    separator()

    s = "(])"
    print(f"Input: {s = }")
    result = obj.isValid(s)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()
