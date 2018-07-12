'''

给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda i: i.start)
        res = []
        while len(intervals) >= 2:
            cur, nex = intervals[0], intervals[1]
            if nex.start <= cur.end <= nex.end:
                intervals[1] = Interval(cur.start, nex.end)
                intervals.pop(0)
            elif cur.end >= nex.end:
                intervals[1] = Interval(cur.start, cur.end)
                intervals.pop(0)
            else:
                res.append(intervals.pop(0))
        res += intervals
        return res


if __name__ == '__main__':
    s = Solution()
    interval_list = [
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    ]
    print(s.merge(interval_list))
