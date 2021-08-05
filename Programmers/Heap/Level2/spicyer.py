import heapq
def solution(scoville, K):
    mix_scoville = []
    for sc in scoville:
        heapq.heappush(mix_scoville,sc)
    
    min_scoville = 0
    answer = 0
    while (1):
        if len(mix_scoville) == 1:
            if heapq.heappop(mix_scoville) > K:
                return answer
            else:
                return -1
        min_scoville = heapq.heappop(mix_scoville)
        second_min_scoville = heapq.heappop(mix_scoville)
        heapq.heappush(mix_scoville,min_scoville+(second_min_scoville*2))
        if min_scoville > K:
            break
        answer += 1
    
    return answer