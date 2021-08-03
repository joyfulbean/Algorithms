import collections
def draw_dot(now, direction):
    return [now[0]+direction[0], now[1]+direction[1]]
    
def solution(arrows):
    
    direction = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    answer = 0
    dot = [0,0]
    visited_edge = set()
    visited_dot = {(0,0)}
    for arrow in arrows:
        for i in range(2):
            before_edge = (dot[0],dot[1])
            dot = draw_dot(dot, direction[arrow])
            new_edge = (dot[0],dot[1])
            check_edge = (before_edge, new_edge)
            if new_edge in visited_dot:
                if check_edge not in visited_edge:
                    answer += 1
            visited_dot.add(new_edge)
            visited_edge.add(check_edge)
            visited_edge.add((new_edge,before_edge))
        
    return answer