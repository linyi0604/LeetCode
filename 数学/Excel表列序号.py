"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
"""


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        li = [ord(i) - ord("A") + 1 for i in reversed(s)]
        for i in range(len(li)):
            sum += li[i] * 26**i
        return sum




if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber("ZY"))
