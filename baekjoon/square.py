# https://www.acmicpc.net/problem/14712

#난이도:상 
#문제 유형:dfs
#실수한 부분: 알고리즘 접근 자체에 어려움..! ***$####@@
#포인트: 

#문제 요약:
# 2×2 격자판에 2×2 사각형을 이루지 않도록 “넴모”들을 배치하는 방법은 모든 경우(24 = 16) 중 네 칸 모두에 “넴모”가 올라가 있는 경우를 제외한 15가지가 있다.

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# 1-index
Map = [ [ 0 for _ in range(M + 1) ] for __ in range(N + 1) ]
answer = 0

# print(Map)

def dfs(count):
    global answer
    if count == N * M:
        answer += 1
        return
    
    y = count // M +1
    x = count % M + 1

    dfs(count+1)
    if Map[y - 1][x] == 0 or Map[y][x - 1] == 0 or Map[y - 1][x - 1] == 0:
        Map[y][x] = 1
        dfs(count + 1)
        Map[y][x] = 0

dfs(0)
print(answer)




#다른 방법
# 1)for loop으로 접근후
# 2)하나씩 풀기
# 3)