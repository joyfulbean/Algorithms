import collections

def solution(clothes):
    closet = collections.defaultdict(int)
    for clothe in clothes:
        closet[clothe[1]] += 1
    answer = 1
    #경우의 수 체크 answer *= (옷 가지수 + 안 입을 경우)
    for i in closet.values():
        answer *= (i+1)

    #모두 다 안입는 경우는 존재하지 않으므로 -1
    return answer-1