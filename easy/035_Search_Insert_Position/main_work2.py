# coding=utf-8
"""
35. Search Insert Position

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
(Получив отсортированный массив различных целых чисел и целевое значение,
верните индекс, если цель найдена. Если нет, верните индекс в том месте, где он
был бы, если бы он был вставлен по порядку.)

Example 1:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Example 2:
Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Example 3:
Input: nums = [1, 3, 5, 6], target = 7
Output:

Constraints:

-  1 <= nums.length <= 10^4
-  -10^4 <= nums[i] <= 10^4
-  nums contains distinct values sorted in ascending order.
-  -10^4 <= target <= 10^4

"""
from typing import List

OUTPUT = "Output: "


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:  # не прошёл проверку!
    """Класс решения"""
    def search_insert(self, nums: List[int], target: int) -> int:
        """

        :param nums:
        :param target:
        :return:
        """
        low = 0  # нижняя граница поиска
        high = len(nums) - 1  # верхняя граница поиска

        while low <= high:  # пока эта часть не сократиться до 1-го элемента...
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:  # элемент массива найден
                return mid
            if guess > target:  # много
                high = mid - 1
            else:
                low = mid + 1
        return low  # возврат минимальной границы


def call_check(nums: List[int], target: int):
    """
    Function for check work method Solution.search_insert()

    :param nums:  a sorted array of distinct integers
    :param target: a target value
    :return: the index if the target is found. If not, return
             the index where it would be if it were inserted in order.
    """
    obj = Solution()
    print(f"Input: {nums = }, {target = }")
    print(OUTPUT, end='')
    result = obj.search_insert(nums, target)
    print(result)


def main():
    """Function main()"""
    separator()
    call_check([1, 3, 5, 6], 5)
    separator()
    call_check([1, 3, 5, 6], 2)
    separator()
    call_check([1, 3, 5, 6], 7)
    separator()


if __name__ == '__main__':
    main()
