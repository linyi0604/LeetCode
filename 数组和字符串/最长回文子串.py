"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        t = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if j-i+1 < len(t):
                    break
                a = s[i:j]
                b = a[::-1]
                if a == b and len(a) >= len(t):
                    t = a
        return t


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abc"))