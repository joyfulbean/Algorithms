# https://www.acmicpc.net/problem/2160
# 4중 for loop

# 5*7 n개씩 배열에 저장하기, 
# 작은 수 순서대로
# 다른게 몇개인지 계산 

#알고리즘
#1)첫번째 그림과 비교 후 다른게 있다면 pair 리스트에 넣기, [1번째 2번째] 숫자 몇 으로!! 
#2)중복 안되게 1-2,2-3


num_pic = int(input()) 
pic = []
for i in range(num_pic):
    temp_pic = [list(input()) for _ in range(5)]
    pic.append(temp_pic)

diff = []
for i in range(len(pic)):
    for j in range(i+1,len(pic)):
        diff_count = 0
        for k in range(5):
            for l in range(7):
                if pic[i][k][l] == pic[j][k][l]:
                    continue
                else: 
                    diff_count = diff_count + 1
        diff.append(([i,j],diff_count))

diff.sort(key=lambda x:x[1])

print(diff[0][0][0]+1, diff[0][0][1]+1)
