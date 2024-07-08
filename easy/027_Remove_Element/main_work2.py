# coding=utf-8
"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get
accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the
  elements which are not equal to val. The remaining elements of nums are not
  important as well as the size of nums.

- Return k.


Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [3, 2, 2, 3], val = 3
Output: 2, nums =[2, 2, _, _]
Explanation: Your function should return k = 2, with the first two elements
of nums being 2.
It does not matter what you leave beyond the returned k (hence they are
underscores).


Example 2:
Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
Explanation: Your function should return k = 5, with the first five elements of
nums containing 0, 0, 1, 3, and 4.
It does not matter what you leave beyond the returned k (hence they are
underscores).


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

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
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Change the array nums such that the first k elements of nums contain
        the elements which are not equal to val. The remaining elements of nums
        are not important as well as the size of nums. Return k.

        :param nums: integer array
        :param val: integer number
        :return: the number of elements in nums which are not equal to val
        """
        size = len(nums)
        k = nums.count(val)
        result = size - k
        i = 0
        while i < size:
            if nums[i] == val:
                nums.pop(i)
                size -= 1
            else:
                i += 1
        nums.extend('_' * k)
        return result


def call_method():
    """
    Function for check

    :return:
    """
    separator()

    obj = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Input: {nums = }, {val = }")
    print(OUTPUT, end='')
    result = obj.removeElement(nums, val)
    print(f"{result}, ", end='')
    print(f"{nums = }")
    separator()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(f"Input: {nums = }, {val = }")
    print(OUTPUT, end='')
    result = obj.removeElement(nums, val)
    print(f"{result}, ", end='')
    print(f"{nums = }")
    separator()


def main():
    """Function main()"""
    call_method()


if __name__ == '__main__':
    main()
