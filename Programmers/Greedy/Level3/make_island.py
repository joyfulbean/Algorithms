import collections
import heapq

# n / costs / answer
# 5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
# 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
# 4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
# 5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
# 6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
# 5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
# 5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
# 5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8

# [[0,1,1],[3,4,1],[1,2,2],[2,3,4]]

# n = 5
# costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]
# answer = 15
#다익스트라 알고리즘 적용이 필요하다. 
def solution(n, costs):
    
    answer = 0
    costs.sort(key = lambda x: x[2])
    connect = set([costs[0][0]])
    
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            elif cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer
#     answer = []
#     for key in graph.keys():
#         Q = [(0, key, 0)]
#         dist = collections.defaultdict(int)

#         while Q:
#             money, node, m = heapq.heappop(Q)
#             if node not in dist:
#                 dist[node] = m
#                 for n in graph[node]:
#                     alter = money + n[1]
#                     heapq.heappush(Q,(alter, n[0], n[1]))
#         answer.append(sum(dist.values()))
# #         print(dist)
#     return min(answer)