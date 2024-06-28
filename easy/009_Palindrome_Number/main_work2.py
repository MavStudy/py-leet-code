"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes
121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.
"""
from collections import deque


def separator():
    print('-' * 50)


def transformation(num: int) -> [int, ...]:
    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)


# Follow up: Could you solve it without converting the integer to a string?
# Продолжение: Не могли бы вы решить эту проблему без преобразования целого
# числа в строку?
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :param x: int
        :return: bool
        """
        if x < 0:
            return False

        nums = transformation(x)
        size = len(nums)
        end = size // 2
        # print(f"{end = }")
        for i in range(end + 1):
            if nums[i] != nums[-1 - i]:
                return False
        return True


def call_method():
    obj = Solution()

    x = 121
    print(f"Input: {x = }")
    result = obj.isPalindrome(x)
    print(f"Output: {result = }")
    separator()

    x = -121
    print(f"Input: {x = }")
    result = obj.isPalindrome(x)
    print(f"Output: {result = }")
    separator()

    x = 1245
    print(f"Input: {x = }")
    result = obj.isPalindrome(x)
    print(f"Output: {result = }")
    separator()

    x = 1001
    print(f"Input: {x = }")
    result = obj.isPalindrome(x)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()
