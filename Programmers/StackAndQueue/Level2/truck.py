def solution(bridge_length, weight, truck_weights):
    done = []
    ing = []
    clock = 0
    num = len(truck_weights)
    prev = 0
    
    while len(done) != num:
        if clock != 0:
            add = 0
            if ing and clock - ing[0][1] == bridge_length: 
                prev = ing.pop(0)
                done.append(prev)
            for k in ing:
                add += k[0]
            if truck_weights and truck_weights[0] + add <= weight:
                truck = truck_weights.pop(0)
                ing.append([truck, clock])
        # print(clock, done,ing)
        clock += 1
    
    return clock-1