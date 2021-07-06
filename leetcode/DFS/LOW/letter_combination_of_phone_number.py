# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(index, path):
            #자리수 만큼 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return 
            
            #숫자 자리수 만큼 반복
            for i in range(index,len(digits)):
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
                    
        if not digits:
            return []
            
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6": "mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        result = []
        dfs(0, "")
        
        return result
        