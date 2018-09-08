"""
给定一个未排序的数组，请判断这个数组中是否存在长度为3的递增的子序列。

正式的数学表达如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法时间复杂度为O(n)，空间复杂度为O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
"""


# class Solution:
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) < 3:
#             return False
#
#         n1, n2 = float("inf"), float("inf")
#
#         for i in nums:
#             if i < n1:
#                 n1 = i
#             elif n1 < i < n2:
#                 n2 = i
#             elif i > n2:
#                 return True
#         return False

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        start, mid = float("inf"), float("inf")

        for i in nums:
            if i < start:
                start = i
            elif start < i < mid:
                mid = i
            elif i > mid:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([2,5,3,4,5]))