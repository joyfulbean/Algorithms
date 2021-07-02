total_num = int(input())
arrayB = list(map(int,input().split()))
count = 0 

#전체에서 빼는걸로 알고리즘을 짜는게 효율적이다.
while(sum(arrayB) != 0):
    for j in range(total_num):
        if arrayB[j] == 0:
            continue
        if(arrayB[j] % 2 == 1):
            arrayB[j] = arrayB[j]-1
            count = count + 1
        
    if sum(arrayB) == 0:
        break
    #모두 짝수로 만들고, 2배 나누기
    arrayB = [ k / 2 for k in arrayB]
    count = count + 1

print(count)