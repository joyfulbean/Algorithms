# 1×1, 2×2, 3×3, 4×4, 5×5

def check5(now_placed, paper):
    if (now_placed[0] + 4 < 10) and (now_placed[1] + 4 < 10):
        i = now_placed[0]
        j = now_placed[1]
        for _ in range(i, i + 5):
            for _ in range(j, j + 5):
                print(i, j)
                if paper[i][j] != 1:
                    return False
        return True
    return False

def check4(now_placed, paper):
    if (now_placed[0] + 3 < 10) and (now_placed[1] + 3 < 10):
        i = now_placed[0]
        j = now_placed[1]
        for _ in range(4):
            for _ in range(4):
                if paper[i][j] != 1:
                    return False
        return True
    return False

def check3(now_placed, paper):
    if (now_placed[0] + 2 < 10) and (now_placed[1] + 2 < 10):
        i = now_placed[0]
        j = now_placed[1]
        for _ in range(3):
            for _ in range(3):
                if paper[i][j] != 1:
                    return False
        return True
    return False

def check2(now_placed, paper):
    if (now_placed[0] + 1 < 10) and (now_placed[1] + 1 < 10):
        i = now_placed[0]
        j = now_placed[1]
        for _ in range(2):
            for _ in range(2):
                print(i,j)
                if paper[i][j] != 1:
                    print('hi')
                    return False
        return True
    return False

paper = [list(map(int, input().split())) for _ in range(10)]
print(paper)

used_paper = 0
for i in range(10):
    for j in range(10):
        if paper[i][j] == 1:
            now_placed = (i,j)
            print(now_placed)
            #실제로 기록
            if check5(now_placed, paper):
                print('change occurr5')
            elif check4(now_placed, paper):
                print('change occurr4')
            elif check3(now_placed, paper):
                print('change occurr3')
            elif check2(now_placed, paper):
                print('change occurr2')
            else:
                print('chnage occurr1')
            used_paper += 1
print(used_paper)

