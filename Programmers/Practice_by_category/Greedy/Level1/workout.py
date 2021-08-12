def solution(n, lost, reserve):
    check = [0]
    for i in range(1,n+1):
        check.append(1)
    reserve.sort()
    
    for l in lost:
        check[l] = 0
        
    for r in reserve: 
        if r in lost:
            check[r] = 1
        elif r-1 in lost and check[r-1] == 0:
            check[r-1] = 1
        elif r+1 in lost:
            check[r+1] = 1
    return sum(check)