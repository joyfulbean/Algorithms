def solution(priorities, location):
    
    index = []
    for i,priority in enumerate(priorities):
        index.append((priority, i))
    
    answer = 0
    while index:
        maximum = max(index)
        check = index.pop(0)
        # print(maximum, check[0], check[1])
        if check[0] == maximum[0]:
            answer += 1
            if check[1] == location:
                return answer
        else:
            index.append(check)
        # print(index)
    return answer