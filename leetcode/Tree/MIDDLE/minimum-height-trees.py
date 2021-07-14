# https://leetcode.com/problems/minimum-height-trees/

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <=1:
            return [0]
        
        graph = collections.defaultdict(list)
        #무방향 그래프 = 양방향
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        #print(graph)
        
        #첫번째 리프 노드 추가
        leaves =[]
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        #루트 노드만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves 
        return leaves
        