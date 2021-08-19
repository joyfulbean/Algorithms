# import sys

# input = sys.stdin.readline
# def dfs(x, y, direction):
#     global result
   
#     if x == n-1 and y == n-1:
#         result += 1
#         return 
#     # print(x,y)
#     if direction == 0 or direction == 2:
#         if y + 1 < n:
#             if map_structure[x][y+1] == 0:
#                 dfs(x, y+1, 0)
#     if direction == 1 or direction == 2:
#         if x + 1 < n:
#             if map_structure[x+1][y] == 0:
#                 dfs(x+1, y, 1)
#     if x+1 < n and y+1 < n:
#         if map_structure[x+1][y] == 0 and map_structure[x][y+1] == 0 and map_structure[x+1][y+1] == 0:
#             dfs(x+1,y+1,2)
    
# n = int(input())
# map_structure = [list(map(int,input().split())) for _ in range(n)]
# result = 0
# dfs(0,1,0)
# print(result)





n = int(input())
arr = [[int(x) for x in input().split()]for y in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(2,n):
        if arr[i][j] == 0 and arr[i][j-1] == 0: #가로에서 오는길 가능
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        if arr[i][j] == 0 and arr[i-1][j] == 0: #세로에서 오는길 가능
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i-1][j] == 0: #대각에서 오는길 가능
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            
print(sum(dp[n-1][n-1]))