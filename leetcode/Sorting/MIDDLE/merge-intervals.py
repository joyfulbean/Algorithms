# https://leetcode.com/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged [-1][1] = max(merged[-1][1],i[1])
            else:
                merged += i,
        return merged
        