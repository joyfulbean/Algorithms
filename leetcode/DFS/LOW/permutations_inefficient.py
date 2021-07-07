# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(index,path):
            count = path.count(" ")
            if count == len(nums):
                path = path.split(" ")
                path = path[:-1]
                result.append(path)
                return

            for i in range(index,len(nums)):
                for j in dic[i]:
                    if str(j) in path:
                        test_path = path.split(" ")
                        if str(j) in test_path:
                            pass
                        else: 
                            dfs(i+1,path+str(j)+" ")
                    else:
                        dfs(i+1,path+str(j)+" ")

        
        if not nums:
            return []

        dic = {}
        for i in range(len(nums)):
            dic[i] = nums
        #print(dic)
        
        result = []
        dfs(0,"")
        
        return result