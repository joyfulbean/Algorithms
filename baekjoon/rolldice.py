#deep copy, simulation
import copy

n,m,original_x,original_y,total_num = map(int, input().split())
map_structure = [list(map(int,input().split())) for _ in range(n)]
moving = list(map(int,input().split()))

direction = [(0,1),(0,-1),(-1,0),(1,0)]

east = [(0,2),(1,1),(2,5),(3,0),(4,4),(5,3)]
west = [(0,3),(1,1),(2,0),(3,5),(4,4),(5,2)]
south = [(0,4),(1,0),(2,2),(3,3),(4,5),(5,1)]
north = [(0,1),(1,5),(2,2),(3,3),(4,0),(5,4)]

dice = [0,0,0,0,0,0]
new_dice = [0,0,0,0,0,0]
new_x = original_x
new_y = original_y

for i in range(total_num):
    new_x = new_x + direction[moving[i]-1][0]
    new_y = new_y + direction[moving[i]-1][1]
    if new_x >=0 and new_x < n and new_y>=0 and new_y < m:
        if moving[i] == 1:
            for pair in east:
                new_dice[pair[1]] = dice[pair[0]]
        elif moving[i] == 2:
            for pair in west:
                new_dice[pair[1]] = dice[pair[0]]
        elif moving[i] == 3:
            for pair in north:
                new_dice[pair[1]] = dice[pair[0]]
        elif moving[i] == 4:
            for pair in south:
                new_dice[pair[1]] = dice[pair[0]]
        dice = copy.deepcopy(new_dice)
        if map_structure[new_x][new_y] == 0:
            map_structure[new_x][new_y] = dice[5]
        else:
            dice[5] = map_structure[new_x][new_y]
            map_structure[new_x][new_y] = 0
        print(dice[0])

    else:
        new_x = new_x - direction[moving[i]-1][0]
        new_y = new_y - direction[moving[i]-1][1]
        continue

##### 알고리즘 total num만큼 반복
#1)originalx와 originaly에서 모든게 0인 dice를 map_structure에 두고
#2)moving부터 meaning-1에서 꺼내서 각각 어떻게 움직여야 하는지 파악
#3)만약 주사위 칸을 넘는지 확인하고 넘으면 출력 x 그냥 continue, 
# 안넘으면,
# 해당하는 배열에서 꺼내서 새로운 리스트를 만들어 재 정비, 
# floor에서 front의 해당하는 번째 출력, 또 아래 down에 해당하는거 복사 처리 
# 바닥이 0이면, 주사위 수 복사, 0이 아니면 주사위가 복사 그리고 바닥은 0