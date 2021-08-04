#이 문제를 아래의 주석과 같이 풀면, 시간초과가 난다. greedy로는 풀수 없다. 

# import collections

# def solution(n, times):
#     current_time = 0
#     num_times = collections.defaultdict()    
    
#     #index로 자료형을 바꿔야 한다..! 그리고 time과 해당하는 수 넣어주기. 
#     for i,time in enumerate(times):
#         num_times[i] = [time, 0]
        
#     # num_times = collections.Counter(times)
    
#     for i in range(n):
#         minimum = float("inf") 
#         for time, value in num_times.items():
#             #minimum이 바뀌면, 그 값 저장..! 
#             temp_time = abs(current_time - (value[0])*(value[1]+1))
#             # print(time, value, temp_time)
#             if temp_time < minimum:
#                 minimum = temp_time
#                 minimum_time = value[0]
#                 minimum_value = value[1]
#                 minimum_index = time 
                
#         # print(minimum_num)
#         current_time = (minimum_time * (minimum_value+1))
#         # print(minimum_time, minimum_value, current_time)
#         num_times[minimum_index][1] += 1
    
#     answer = current_time
#     return answer



#이진 탐색 방법을 사용해야 한다. 
#모든 사람이 심사 받을 최댓값, 최소값 (가장 오래 걸리는 심사위원에게 다 받는것,0)
#mid (최대와 최소의 가운대 시간)
#만약 mid 시간 안에 심사가 가능한 사람의 수가 n개를 넘으면, 시간 줄이기.
#만약 mid 시간 안에 심사가 가능한 사람의 수가 n개를 안넘으면, 시간 늘리기.
#mid시간 / 심사대의 시간
#30/7, 30/10 의 몫이 4 + 3 = 7 /7은 6보다 크다.
#종료 조건: 전체가 전부 돌고,거기서 제일 작은걸 찾으면 되는것. 

answer = 0
def bn_search(min_time, max_time, times, n):
    global answer
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        result = 0
        for time in times:
            result += mid//time 
            if result >= n:
                break
        if result >= n:
            answer = mid
            max_time = mid - 1
        elif result < n:
            min_time = mid + 1 

def solution(n, times):
    global answer
    min_time = 1
    max_time = max(times) * n
    bn_search(min_time, max_time, times, n)
    
    return answer


