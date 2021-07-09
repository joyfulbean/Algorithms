# https://leetcode.com/problems/network-delay-time/

#첫번째 source의 거리는 0으로 만든다. 
#source를 전부 넣은 priority q를 하나 생성
#그래프레서 v를 하나씩 꺼내서, 반복
#만약 v가 source애 없다면,dist[v]를 무한대로 바꾸기. prev[v]를 undefined 로 바꾼다. 
#그리고 q에 넣는다. 거리와 v를. 
#q가 다 빌때까지 반복
#q에서 가장 낮은걸 꺼내서 u에 넣는다. 
#u의 모든 neighbor방문하면서, u,v의 거리와 u를 더해서 alt에 넣고
#distv가 alter보다 크면, 즉 alt가 더 작으면, 
#dist[v]에 alter를 넣고, prev[v]에 u를 넣는다
#그리고 q의 우선순위를 감소시킨다. 

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        #print(graph)
        #정점까지의 소요시간을 담아두는 변수, (소요시간, 정점)으로 구성됨
        Q = [(0,k)]
        #node와 걸리는 시간 기록
        dist = collections.defaultdict(int)
        
        #모든 경로를 갈 때까지
        while Q:
            #다음선택한 경로를 q에 담아두고, 그걸 팝하기
            #heapq는 (우선순위, 값)의 형태가 된다. 최소값 부터 팝
            time, node = heapq.heappop(Q)
            #print(node)
            #만약 노드가 거리에 없다면, 
            if node not in dist:
                dist[node] = time
                #선택된 정점으로 부터 연결된 모든 노드 방문.
                for v,w in graph[node]:
                    #새로 구한 거리가 더 짧다면, Q에 넣어라.!!
                    alt = time + w
                    heapq.heappush(Q, (alt,v)) 
        
        if len(dist) == n:
            return max(dist.values())
        return -1
                    
            
        
