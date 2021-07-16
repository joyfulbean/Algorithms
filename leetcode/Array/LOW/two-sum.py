# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_dic = {}
        for i, num in enumerate(nums):
            if (target - num) in num_dic:
                return [i,num_dic[target-num]]
            num_dic[num] = i
        