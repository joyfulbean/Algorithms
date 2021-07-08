# https://leetcode.com/problems/reconstruct-itinerary

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # print(tickets)
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        #print(graph)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        dfs('JFK')
        
        return route[::-1]

#좀더 효율적인 방법
#pop()이 훨씬더 효율적임, 그렇게 하려면 처음에 reverse필요
# class Solution(object):
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         # print(tickets)
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets, reverse=True):
#             graph[a].append(b)
#         #print(graph)
        
#         route = []
#         def dfs(a):
#             while graph[a]:
#                 dfs(graph[a].pop())
#             route.append(a)
#         dfs('JFK')
        
#         return route[::-1]


##stack으로 풀이
# class Solution(object):
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         # print(tickets)
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)
#         #print(graph)
        
#         route = []
#         stack = ['JFK']
#         def dfs(a):
#             while stack:
#                 while graph[stack[-1]]:
#                     stack.append(graph[stack[-1].pop(0)])
#             route.append(stack.pop())
#         dfs('JFK')
        
#         return route[::-1]