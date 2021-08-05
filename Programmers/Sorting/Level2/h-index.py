def solution(citations):
# [12, 11, 10, 9, 8, 1] 5
# [6, 6, 6, 6, 6, 1] 5
# [4, 4, 4] 3
# [4, 4, 4, 5, 0, 1, 2, 3] 4
# [10, 11, 12, 13] 4
# [3, 0, 6, 1, 5] 3
# [0, 0, 1, 1] 1
# [0, 1] 1
# [10, 9, 4, 1, 1] 3
    
    citations.sort()
    left = 0
    right = len(citations)-1
    answer = []
    while left <= right:
        mid = (left+right)//2
        h_index = 0
        for c in citations:
            if c >= citations[mid]:
                h_index += 1
        if h_index <= citations[mid]:
            answer.append(h_index)
            right = mid -1
        else:
            left = mid + 1
    if not answer:
        answer.append(0)
    return max(answer)

#충격적인 풀이1
    # def solution(citations):
    # citations.sort(reverse=True)
    # answer = max(map(min, enumerate(citations, start=1)))
    # return answer

#충격적인 풀이2
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0

# 지금 몇 편이 남았는가? -> 모든 인용횟수가 이 값보다 큰가?(가장 작은 값이 이 값보다 큰가?)] 로 생각의 순서를 바꾼 것이라고 할 수 있겠습니다. 