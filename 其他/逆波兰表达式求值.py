"""
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:

    def isnum(self, t):
        return t.strip("-").isdigit()

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        while len(tokens) > 1:
            i = 0
            while i < len(tokens)-2:
                o, a, b = tokens[i+2], tokens[i], tokens[i+1]
                if not self.isnum(o) and self.isnum(a) and self.isnum(b):
                    if o == "+":
                        r = int(a) + int(b)
                    elif o == "-":
                        r = int(a) - int(b)
                    elif o == "*":
                        r = int(a) * int(b)
                    else:
                        a, b = int(a), int(b)
                        r = int(a/b)

                    tokens.pop(i)
                    tokens.pop(i)
                    tokens.pop(i)
                    tokens.insert(i, str(r))
                    i -= 1
                    continue
                i += 1

        return int(tokens[0])


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))