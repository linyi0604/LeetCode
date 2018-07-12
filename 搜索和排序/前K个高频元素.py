'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

例如，

给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

注意：

你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for key in nums:
            if key not in dic.keys():
                dic[key] = 1
            else:
                dic[key] += 1
        items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        return [items[i][0] for i in range(k)]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
