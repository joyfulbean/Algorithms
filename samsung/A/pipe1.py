# 즉, 파이프는 항상 빈 칸만 차지해야 한다.
# 오른쪽 왼쪽 아래 대각선, 아래 이렇게 3방향, 밀면 45도씩 회전 가능

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

# 갈수 있는 방향 
# - 가로: 가로, 대각선
# - 세로: 세로, 대각선
# - 대각선: 가로, 세로, 대각선 
result = 0
def dfs(x, y, direction):
    global result
   
    if x > n-1 or y > n-1:
        return
    else:
        if map_structure[x][y] == 1:
            return 
        # print(x,y)
        if x == n-1 and y == n-1:
            result += 1
    
    if direction == 'l':
        for left in lefts:
            dfs(x+left[0], y+left[1], left[2])
    elif direction == 'd':
        for down in downs:
            dfs(x+down[0], y+down[1], down[2])
    elif direction == 'c':
        for cross in crosses:
            dfs(x+cross[0], y+cross[1], cross[2])

n = int(input())
map_structure = [list(map(int,input().split())) for _ in range(n)]

lefts = [(0,1,'l'),(1,1,'c')]
downs = [(1,0,'d'),(1,1,'c')]
crosses = [(0,1,'l'),(1,0,'d'),(1,1,'c')]

dfs(0,1,'l')

print(result)

