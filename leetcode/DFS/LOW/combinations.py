# https://leetcode.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        
        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)
                elements.pop()

        dfs([],1,k)
        return results

#라이브러리 사용
# return list(itertools.combination(range(1,n+1),k))