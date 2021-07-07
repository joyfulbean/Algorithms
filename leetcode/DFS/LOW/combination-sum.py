# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        elements = []
        def dfs(elements, start, summation):
            
            if target <= summation:
                #print(elements[:])
                ##자기 자신을 반복하는것도 가능...!! 
                if target == summation:
                    results.append(elements[:])
                return
                
            for i in range(start,len(candidates)):
                elements.append(candidates[i])
                dfs(elements,i,summation+candidates[i])
                elements.pop()
        
        dfs(elements, 0, 0)
        
        #여기서 계산이 7아닌거 버리기! 
        return results