def solution(operations):
    
    priority_queue = []
    for op in operations:
        if op[0] == 'I':
            priority_queue.append(int(op[2:]))
            priority_queue.sort()
        else:
            if len(priority_queue) > 0:
                if op[2] == '1':
                    priority_queue.pop()
                else:
                    priority_queue.pop(0)
            else:
                continue
        print(priority_queue)
    if len(priority_queue) == 0:
        return [0,0]
    else:
        return(priority_queue.pop(), priority_queue.pop(0))