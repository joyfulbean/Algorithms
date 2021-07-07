# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def dfs(index,path):
            result.append(path)
            
            for i in range(index,len(nums)):
                dfs(i+1,path+[nums[i]])
                
        dfs(0,[])
        return result