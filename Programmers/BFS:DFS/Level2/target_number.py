# 순열과 조합의 차이점을 잘 이해해야 하는 문제
# 순열: next_number와 prev_number를 통해 나눠준다. next_number안에서 또다시 조합이 되어 중복 있음
# 조합: 인덱스와 k-1로 카운트를 하기 때문에 또 다시 조합을 반복하지 않는다. 해당 인덱스에 대해 다했으면 다음으로 넘어감.

#순열을 이용한 풀이. 풀이는 되나, 시간 초과를 통과하지 못한다. 
# import operator

# count = 0

# def solution(numbers, target):
#     global count
#     operator = {"+": (lambda x: 0+x), "-": (lambda x: 0-x)}
    
#     def dfs(number, start, k):
#         global count
#         if k == 0:
#             sum_n = sum(number)
#             if target == sum_n:
#                 count += 1
#                 # print(count)
#                 # print(results)
            
#         for opt in operator:
#             for i in range(start, len(numbers)):
#                 number.append(operator[opt](numbers[i]))
#                 print(number)
#                 dfs(number, i+1, k-1)
#                 number.pop()
    
#     dfs([],0,len(numbers))
#     return count