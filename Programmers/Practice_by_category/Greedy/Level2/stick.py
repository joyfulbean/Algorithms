def solution(name):
    up_down = 0
    min_length = len(name) - 1
    for k in range(len(name)):
        up_down += min(abs(ord(name[k]) - ord("A")), 26 - abs(ord(name[k]) - ord("A")))
        
        next = k+1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_length = min(min_length, k*2 + len(name) - next)
    
    answer = min_length + up_down
    return answer