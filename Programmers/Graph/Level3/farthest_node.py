import collections
import heapq

max_length = 0
def solution(n, edge):
    # 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
    # 각각 최단 거리를 부르고, 개수 저장
    graph = collections.defaultdict(list)
    for u,v in edge:
        graph[u].append((v,1))
        graph[v].append((u,1))
        
    Q = [(0,1)]
    dist = collections.defaultdict(int)
    
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt,v)) 

    answer = list(dist.values()).count(max(dist.values()))
    return answer