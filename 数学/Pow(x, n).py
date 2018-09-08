"""
Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        res = x
        t = n if n % 2 == 0 else n-1
        t = t if t > 0 else -t

        while t > 1:
            t /= 2
            res *= res
        if n > t:
            res *= x

        if n > 0:
            return res
        else:
            return 1 / res


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
