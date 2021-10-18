import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def dfs(y, x, count):
    global answer, used

    if y >= 10:
        answer = min(answer, count)
        return

    if x >= 10:
        dfs(y+1, 0, count)
        return

    # 현재 좌표가 1일 때
    # 색종이 붙이기
    if paper[y][x] == 1:
        for k in range(5):
            if used[k] == 5:
                continue
            if y + k >= 10 or x + k >= 10:
                continue

            flag = True
            for i in range(y, y+k+1):
                for j in range(x, x+k+1):
                    if paper[i][j] == 0:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                for i in range(y, y+k+1):
                    for j in range(x, x+k+1):
                        paper[i][j] = 0
                used[k] += 1
                dfs(y, x+k+1, count+1)

                used[k] -= 1
                for i in range(y, y+k+1):
                    for j in range(x, x+k+1):
                        paper[i][j] = 1
    # 현재 좌표가 0이라면
    # 옆으로 넘어간다.
    else:
        dfs(y, x+1, count)

paper = [list(map(int, input().split())) for _ in range(10)]
used = [0] * 5
answer = 26

dfs(0, 0, 0)
print(answer if answer != 26 else -1)