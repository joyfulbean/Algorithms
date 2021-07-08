class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            return True
        
        #순환 구조는 아니지만, 그래프 안에 여러개의 구조가 있을 수 있다. 
        #undirectional 이기 때문에.. 
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
    


#visited 라는 변수를 이용해서, 한번 확인한건 반복해서 확인하지 않기!!! 
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         graph = collections.defaultdict(list)
#         for x, y in prerequisites:
#             graph[x].append(y)
        
#         traced = set()
#         visited = set()
        
#         def dfs(i):
#             if i in traced:
#                 return False
#             if i in visited:
#                 return True
            
#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
#             traced.remove(i)
#             visited.add(i)
            
#             return True
        
#         #순환 구조는 아니지만, 그래프 안에 여러개의 구조가 있을 수 있다. 
#         #undirectional 이기 때문에.. 
#         for x in list(graph):
#             if not dfs(x):
#                 return False
        
#         return True
    
        