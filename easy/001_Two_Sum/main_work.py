"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


def separator():
    print('-' * 50)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        result = []
        size = len(nums)

        for head in range(size):
            tail = -1
            i = 1
            not_complete = True
            while not_complete:
                idx = head + i
                if idx == size:
                    not_complete = False
                    continue
                if nums[head] + nums[idx] == target:
                    result.append(head)
                    result.append(idx)
                    return result
                idx = tail - i
                if nums[tail] + nums[idx] == target:
                    result.append(tail + size)
                    result.append(idx + size)
                    result.reverse()
                    return result
                i += 1
        return result


def call_method():
    obj = Solution()

    result = obj.twoSum([2, 7, 11, 15], 9)
    print(f"Output: {result = }")
    print('-' * 79)

    result = obj.twoSum([3, 2, 4], 6)
    print(f"Output: {result = }")
    separator()

    result = obj.twoSum([3, 3], 6)
    print(f"Output: {result = }")
    separator()

    result = obj.twoSum([2, 5, 5, 11], 10)
    print(f"Output: {result = }")
    separator()

    result = obj.twoSum([2, 1, 9, 4, 4, 56, 90, 3], 8)
    print(f"Output: {result = }")
    separator()

    result = obj.twoSum([0, 4, 3, 0], 0)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()