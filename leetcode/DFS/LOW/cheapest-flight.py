#https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
            
        Q = [(0,src, k)]
        
        while Q:
            time, node, stops = heapq.heappop(Q)
            if node == dst:
                return time
            if stops >= 0:
                for v,w in graph[node]:
                    alter = time + w
                    heapq.heappush(Q,(alter,v, stops-1))
        return -1
                    