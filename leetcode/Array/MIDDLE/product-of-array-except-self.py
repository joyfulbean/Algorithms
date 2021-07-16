# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        out = []
        p = 1
        #왼쪽 곱셈
        for i in range(0,len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        
        #왼쪽에 곱셈결과에 오른쪽 차례대로 곱셈
        for i in range(len(nums)-1, 0-1,  -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out
    