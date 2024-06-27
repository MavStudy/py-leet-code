"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
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

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return []


"""
Approach 1: Brute Force
Algorithm

The brute force approach is simple. Loop through each element xxx and find 
if there is another value that equals to target−x.


Complexity Analysis

Time complexity: O(n^2).
For each element, we try to find its complement by looping through the rest 
of the array which takes O(n) time. Therefore, the time complexity is
O(n^2).

Space complexity: O(1).
The space required does not depend on the size of the input array, so only 
constant space is used.
"""


def call_method():
    obj = Solution()
    separator()

    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [3, 2, 4]
    target = 6
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [3, 3]
    target = 6
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [2, 5, 5, 11]
    target = 10
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [2, 1, 9, 4, 4, 56, 90, 3]
    target = 8
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [0, 4, 3, 0]
    target = 0
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()

    nums = [0, 1, 2, 3]
    target = 7
    print(f"Input: {nums = }, {target = }")
    result = obj.twoSum(nums, target)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()
