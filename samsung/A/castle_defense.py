# -*- coding: utf-8 -*-

# https://www.acmicpc.net/problem/17135
from itertools import combinations

def cal_dist(pairs1, pairs2):
    dist = abs(pairs1[0]-pairs2[0]) + abs(pairs1[1]-pairs2[1])
    return dist

def initial_cluster(possible_arch):
    clusters = {}
    for p in possible_arch:
        clusters[p] = []
    return clusters

#input 받기
N, M, D = map(int, input().split(' '))
M_list = [i for i in range (M)]
#궁수 3명이 위치 할수 있는 j값 기록 
possible_arch = list(combinations(M_list,3))
#최종 결과 확인을 위한 max
max_kills = [0]
#맨처음 판의 상태
map_structure = [list(map(int,input().split(' '))) for _ in range(N)]

for each_arch in possible_arch:
    #값이 1인것들이 enemy이고, 현재 위치를 전부 기록 
    kills = 0
    enemy_placed = []
    for i in range(N):
        for j in range(M):
            if map_structure[i][j] == 1:
                enemy_placed.append((i,j))

    #게임 끝날때까지 for문
    while enemy_placed:
        #이들의 위치...
        possible_kills = initial_cluster(each_arch)
        selected_enemy = set()

        # print(enemy_placed)

        for i in range(3):
            for enemy in enemy_placed: 
                dist = cal_dist((N, each_arch[i]), (enemy[0], enemy[1]))
                if dist <= D:
                    #dist, enemy 위치로 기록 (공격가능한 가장 왼쪽 생기면 스탑하기 위해)
                    possible_kills[each_arch[i]].append((dist, enemy[0], enemy[1]))
            if possible_kills[each_arch[i]]:
                selected_enemy.add(min(possible_kills[each_arch[i]], key = lambda t: (t[0], t[1])))
        # print(selected_enemy)

        #kill the enemy
        for each_selected_enemy in selected_enemy:
            # print((each_selected_enemy[1],each_selected_enemy[2]))
            enemy_placed.remove((each_selected_enemy[1],each_selected_enemy[2]))
            kills += 1

        gone = []
        #update the enemy
        for i in range(len(enemy_placed)): 
            if enemy_placed[i][0] + 1 == N:
                gone.append((enemy_placed[i][0] + 1, enemy_placed[i][1]))
            enemy_placed[i] = (enemy_placed[i][0] + 1, enemy_placed[i][1])

        # #gone the enemy
        for g in gone:
            enemy_placed.remove((g[0],g[1]))

        # print(enemy_placed)
        # print('hi')
        
    #records the number of kills
    max_kills.append(kills)

print(max(max_kills))