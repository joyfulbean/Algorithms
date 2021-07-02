#https://www.acmicpc.net/problem/11724

# 연결 요소에 속한 모든 정점을 연결하는 경로가 있어야 한다.
# 또 다른 연결 요소에 속한 정점과 연결하는 경로가 있으면 안된다.
# https://velog.io/@polynomeer/연결-요소Connected-Component

# 시간 초과: https://www.acmicpc.net/blog/view/70

#dfs & bfs : https://www.youtube.com/watch?v=7C9RgOcvkvo
# collections from dequeue, stack = []

#1)그래프 표현 = 인접리스트 방식, 0은 비우고 1과 연결된거 쭉, 2와 연결된거 쭉 리스트 만들기
#2) 노드 개수만큼 1차원 리스트 초기화
#3) visited true가 있으면 계속 부르기!!

import sys
from sys import stdin
sys.setrecursionlimit(1000000) 
global visited

def dfs(graph, v, visited):
    visited[v] = True

    if not graph.get(v):
        return 

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

n, m = map(int, input().split())

graph = {}
for i in range(m):
    c, d = map(int, stdin.readline().split())
    if not graph.get(c):
        temp = []
        temp.append(d)
        graph[c] = temp
    else:
        graph[c].append(d)

    if not graph.get(d):
        temp = []
        temp.append(c)
        graph[d] = temp
    else:
        graph[d].append(c)

visited = [False] * (n+1)
visited[0] = True

count = 0
for i in range(1,len(visited)):
    if(visited[i] == False):
        dfs(graph,i,visited)
        count = count + 1

print(count)




