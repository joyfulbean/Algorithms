import collections

def solution(participant, completion):
    
    num_p = collections.Counter(participant)
    for c in completion:
        num_p[c] -= 1
    return num_p.most_common(1)[0][0]