import collections
def solution(n, computers):
    
    def bfs(edge_list, visited, nodes):
        count = 0
        for i in range(1,len(visited)):
            if visited[i] == 0:
                queue = []
                queue.append(nodes[i-1])
        
                while queue:
                    node = queue.pop(0)
                    if visited[node] == 0:
                        visited[node] = 1
                        for n in edge_list[node]:
                            queue.append(n)
                count += 1
            else:
                continue
        return count
    
    edge_list = collections.defaultdict(list)
    answer = 0
    visited = [0]
    nodes = []
    for i in range(n):
        visited.append(0)
        nodes.append(i+1)
        for j in range(n):
            if computers[i][j] == 1:
                edge_list[i+1].append(j+1)
    answer = bfs(edge_list, visited, nodes)

    return answer