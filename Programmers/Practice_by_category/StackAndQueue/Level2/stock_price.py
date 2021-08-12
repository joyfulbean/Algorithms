def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer

# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
 
#     for i, price in enumerate(prices):
#         #stack이 비었이면 false
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
 
#     # for문 다 돌고 Stack에 남아있는 값들 pop
#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j
 
#     return answer


