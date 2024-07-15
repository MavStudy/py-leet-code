# coding=utf-8
"""
88. Mege Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.
(Вам даны два целочисленных массива nums1 и nums2, отсортированных в
порядке неубывания, и два целых числа m и n, представляющие количество
элементов в числах 1 и num2 соответственно.)

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
(Объедините nums1 и nums2 в единый массив, отсортированный в порядке
неубывания.)

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of
m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length
of n.
(Окончательный отсортированный массив не должен быть возвращен функцией, а
вместо этого должен храниться внутри массива nums 1. Чтобы учесть это, nums1
имеет длину m + n, где первые m элементов обозначают элементы, которые должны
быть объединены, а последние n элементов имеют значение 0 и должны
игнорироваться. nums2 имеет длину n.)


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
                            - -   -
from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there
to ensure the merge result can fit in nums1. (Обратите внимание, что, поскольку
m = 0, в nums 1 нет элементов. Значение 0 используется только для того, чтобы
результат слияния мог поместиться в nums 1.)


Constraints:

•  nums1.length == m + n
•  nums2.length == n
•  0 <= m, n <= 200
•  1 <= m + n <= 200
•  -10^9 <= nums1[i], nums2[j] <= 10^9


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
(Продолжение: Можете ли вы предложить алгоритм, который выполняется за
O(m + n) времени?)

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
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead. (Ничего не
        возвращайте, вместо этого измените nums1 на месте.)

        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        # last index nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


def check_method(nums1: List[int], m: int, nums2: List[int], n: int):
    """

    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """

    separator()
    obj = Solution()
    print(f"Input: {nums1 = }, {m = }, {nums2 = }, {n = }")
    separator()
    obj.merge(nums1, m, nums2, n)
    print(OUTPUT, nums1)


def main():
    """Function main()"""
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    check_method(nums1, m, nums2, n)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    check_method(nums1, m, nums2, n)

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    check_method(nums1, m, nums2, n)

    nums1 = [2, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    check_method(nums1, m, nums2, n)


if __name__ == '__main__':
    main()
