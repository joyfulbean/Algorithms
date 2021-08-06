# answer = []

# def make_triangle(triangle, i, j):
#     new_triangle = []
#     count = 2
#     for row in range(i+1, len(triangle)):
#         temp = []
#         for level in range(count):
#             temp.append(triangle[row][j+level])
#         count += 1
#         new_triangle.append(temp)
#     return new_triangle

# def dfs(triangle, total, k, height):
#     global answer
#     if k == height:
#         answer.append(total)
#         return
    
#     for i in range(len(triangle)):
#         for j in range(len(triangle[i])):
#             now = triangle[i][j]
#             new_trig = make_triangle(triangle, i, j)
#             #leaf만 계산하게 해주면 효율적...! 
#             print(new_trig, i, j, k, total, now, total+now)
#             dfs(new_trig, total+now, k+1, height)

    
# def solution(triangle):
#     global answer
#     height = len(triangle)
#     dfs(triangle, 0, 0, height)
#     # print(answer)
#     return max(answer)


import collections
answer = []
    
def solution(triangle):
    global answer
    height = len(triangle)
    new_trig = triangle[::]

    for i in range(1, len(new_trig)):
        for j in range(len(new_trig[i])):
            if j == 0:
                new_trig[i][j] += new_trig[i-1][j]
            elif j == len(new_trig[i])-1:
                new_trig[i][j] += new_trig[i-1][j-1]
            else:
                new_trig[i][j] += max(new_trig[i-1][j-1], new_trig[i-1][j])
    
    answer = max(new_trig[len(new_trig[i])-1])    
    return answer