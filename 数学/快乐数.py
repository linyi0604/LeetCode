"""
c
"""


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = []
        while True:
            n = self.get_add(n)
            if n == 1:
                return True
            elif n in temp:
                return False
            else:
                temp.append(n)

    def get_add(self, n):
        ret = 0
        while n != 0:
            g = n % 10
            ret += g ** 2
            n = int(n / 10)
        return ret



if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
