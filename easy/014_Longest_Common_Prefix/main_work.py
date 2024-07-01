"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.

Constraints:

-  1 <= strs.length <= 200
-  0 <= strs[i].length <= 200
-  strs[i] consists of only lowercase English letters.
"""
from typing import List


def separator():
    """
    Function separator

    :return:
    """
    print('-' * 50)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Function to find the longest common prefix string amongst an array
        of strings.
        :param strs:
        :return: st
        """

        if len(strs) == 1:
            return ''.join(strs[0])
        result = [""]
        strs.sort(key=len, reverse=False)
        strs_arr = list(strs)
        min_str_arr = strs[0]
        break_out_flag = False
        for i in range(len(min_str_arr)):
            check = strs[0][i]
            for j in range(1, len(strs)):
                if check != strs_arr[j][i]:
                    break_out_flag = True
                    break
            else:
                result.append(check)
            if break_out_flag:
                break

        return ''.join(result)


def call_method():
    """
    Function for check

    :return:
    """
    obj = Solution()

    strs = ["flower", "flow", "flight"]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()

    strs = ["dog", "racecar", "car"]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()

    strs = ["apple"]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()

    strs = [""]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()

    strs = ["ab", "a"]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()

    strs = ["cir", "car"]
    print(f"Input: {strs = }")
    result = obj.longestCommonPrefix(strs)
    print(f"Output: {result = }")
    separator()


def main():
    call_method()


if __name__ == '__main__':
    main()
