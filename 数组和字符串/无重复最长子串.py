"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res = 1
        start = 0
        end = start
        while start < len(s)-1 and end < len(s)-1:
            # print(start, end)
            # input()
            next = end + 1
            if s[next] not in s[start:end+1]:
                end += 1
                if res <= end - start + 1:
                    res = end - start + 1
            else:
                start += 1
                end = start
        return res



if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("bbbbb"))