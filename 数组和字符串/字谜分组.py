"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_copy = ["".join(sorted(s)) for s in strs]
        dic = {}
        for i in range(len(strs_copy)):
            cur = strs_copy[i]
            if cur not in dic.keys():
                dic[cur] = [i]
            else:
                dic[cur].append(i)
        return [[strs[i] for i in li] for key, li in dic.items()]



if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))