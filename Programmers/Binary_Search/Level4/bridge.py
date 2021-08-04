def solution(distance, rocks, n):

# [1]답을 정해둔, 이진 탐색 방법을 사용해야 한다.

# [2]최소 값은 0 최대값은 마지막 지점인 25로정하고, 미드는 12가 된다. 

# [3]처음 위치를 0으로 두고 다음 바위까지의 거리가 mid보다 작으면 제거 아니면 그 바위로 이동한다. 

# [4]제거한 바위가 n이상이면 기준값을 줄여야 한다.

    left = 0
    right = distance 
    rocks.insert(0,0)
    rocks.append(distance)
    rocks.sort()
    answer = []
    while(left <= right):
        num = 0
        mid = (left + right) //2
        i = 0
        for j in range(1,len(rocks)):
            if rocks[j]-rocks[i] < mid:
                num += 1
            else:
                i = j
        
        if num > n:
            right = mid - 1
        else:
            left = mid + 1
            answer.append(mid)
        
    return max(answer)
                