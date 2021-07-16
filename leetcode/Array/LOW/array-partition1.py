#  https://leetcode.com/problems/array-partition-i/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            #앞에서부터 오른차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        
        return sum