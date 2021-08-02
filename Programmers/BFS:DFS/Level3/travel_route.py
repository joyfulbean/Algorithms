import collections
answer = []
def dfs(tickets_dict, start):
    global answer
    while tickets_dict[start]:
        dfs(tickets_dict, tickets_dict[start].pop(0))
    answer.append(start)
    
def solution(tickets):
    global answer
    
    tickets_dict = collections.defaultdict(list)
    for start, end in sorted(tickets):
        tickets_dict[start].append(end)
    
    dfs(tickets_dict, 'ICN')
    
    return answer[::-1]