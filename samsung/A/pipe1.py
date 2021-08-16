import sys

input = sys.stdin.readline
def dfs(x, y, direction):
    global result
   
    if x == n-1 and y == n-1:
        result += 1
        return 
    # print(x,y)
    if direction == 0 or direction == 2:
        if y + 1 < n:
            if map_structure[x][y+1] == 0:
                dfs(x, y+1, 0)
    if direction == 1 or direction == 2:
        if x + 1 < n:
            if map_structure[x+1][y] == 0:
                dfs(x+1, y, 1)
    if x+1 < n and y+1 < n:
        if map_structure[x+1][y] == 0 and map_structure[x][y+1] == 0 and map_structure[x+1][y+1] == 0:
            dfs(x+1,y+1,2)
    
n = int(input())
map_structure = [list(map(int,input().split())) for _ in range(n)]
result = 0
dfs(0,1,0)
print(result)






N = int(input())
board = [list(map(int, input().split(' '))) for _ in range(N)]
result = [[[0 for i in range(N)] for i in range(N)] for i in range(3)]
result[0][0][1] = 1

# 맨 첫줄은 가로밖에
for i in range(2, N):
    if board[0][i] == 0:
        result[0][0][i] = result[0][0][i-1]

# 두번째 줄부터
for i in range(1, N):
    # 파이프가 (0, 0) , (1, 0)에 놓여있으니까 3번째부터
    for j in range(2, N):
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]

        if board[i][j] == 0:
            # 가로
            result[0][i][j] = result[0][i][j-1] + result[2][i][j-1]
            # 세로
            result[1][i][j] = result[1][i-1][j] + result[2][i-1][j]


answer = [result[x][N-1][N-1] for x in range(3)]
print(sum(answer))