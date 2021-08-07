def solution(m, n, puddles):
    
    map = []
    for i in range(n+1):
        temp = []
        for j in range(m+1):
            temp.append(0)
        map.append(temp)
        
    for puddle in puddles:
        map[puddle[1]][puddle[0]] = -1
    
    map[1][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            ## 웅덩이 체크!
            if map[i][j] == -1:
                map[i][j] = 0
            else:
                map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007
                
    return map[n][m]