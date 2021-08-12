import collections

def solution(n, results):    
    #안에 반복되지 않게 set자료형 이용
    wins, loses = collections.defaultdict(set), collections.defaultdict(set)
    
    #results 추가
    for result in results:
        wins[result[0]].add(result[1])
        loses[result[1]].add(result[0])
    
    for i in range(1,n+1): 
        #너가 졌으니까, 너가 이긴건 애도 이긴거야
        for winner in loses[i]: 
            wins[winner].update(wins[i])
        #너가 이겼으니까, 너가 진애는 애도 진거야
        for loser in wins[i]:
            loses[loser].update(loses[i])
            
    answer  = 0
    for i in range(1, n+1):
        if len(wins[i])+len(loses[i]) == n-1:
            answer += 1
    
    return answer