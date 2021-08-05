answer = []

def dfs(num, total, k, number):
    global answer
    
    if k > 8 :
        return -1
    
    if total == number:
        answer.append(k)
        return
        
    for i,n in enumerate(num):
        dfs(num, total-n, k+i+1, number)
        dfs(num, total+n, k+i+1, number)
        dfs(num, total*n, k+i+1, number)
        dfs(num, total/n, k+i+1, number)
        

def solution(N, number):
    global answer
    digit = len(str(number))
    num = []
    for d in range(1,digit+1):
        num.append(int(str(N)*d))

    dfs(num, 0, 0, number)
    if not answer:
        return -1
    return min(answer)