"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, length, res = sorted(nums), len(nums), []
        for i in range(length-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, length - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]

                if target < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif target > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    r = [nums[i], nums[j], nums[k]]
                    res.append(r)
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(s.threeSum([-2,0,1,1,2]))


