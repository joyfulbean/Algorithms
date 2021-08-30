# https://www.acmicpc.net/problem/17135
#### not sure
import math

def cal_dist((r1,c1),(r2,c2)):
    dist = abs(r1-r2) + abs(c1-c2)
    return dist

N, M, D = map(int,input().split())
map_structure = [list(map(int,input().split())) for _ in range(N)]

#모든 공격 대상을 모아둔곳, + 그의 위치!! 
#이게 만약 다 없어지면,, 멈춤...갈수 있는 곳에서 각 궁수마다 왼쪽에 있는거 선택, 그리고 한번에 제거..! = 0, pop 한번만 가능!! ??.

#궁수 3명의 위치 선정, 그에 따른 제거 가능한 최대 적의 수 : 아마도 내 위에 가장 많은 적이 있으면?, 적이 몰린곳
map_structure.append([-1,-1,-1] + [0]*(M-3))
#궁수의 위치 r1,c1으로 기록

while 1 not in map_structure:
    #거리 d이하에 공격할 대상이 있는지 먼저 찾기. 
        #가장 가까운거 우선, 왼쪽 우선, 같은 사람 공격 가능
        #성에 가거나, 공격당하면 제외
    start = N - D - 1
    for i in range(start,N):
        for j in range(M):
            