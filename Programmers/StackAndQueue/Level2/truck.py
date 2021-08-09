def solution(bridge_length, weight, truck_weights):
    done = []
    ing = []
    clock = 1
    
    while len(done) != len(truck_weights):
        if clock % bridge_length == 0:
            for _ in range (bridge_length):
                if ing:
                    done.append(ing.pop(0))
        ##다 비었을때...
        expected_weight = truck_weights[0] + sum(ing)
        if expected_weight <= weight and truck_weights:
            truck = truck_weights.pop(0)
            ing.append(truck)
        else:
            ing.append(0)
        clock += 1
        print(clock, done,ing)
        # break
    
    answer = len(done)
    return answer