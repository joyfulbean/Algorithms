# https://leetcode.com/problems/maximum-subarray/

#0보다 작아지면, 나 자신을 그대로 들고 내려옴. 그리고 누적해 나아감.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)