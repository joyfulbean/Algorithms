from itertools import permutations
import math
def is_prime(n):
    if n==0 or n==1:                            
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  
            if n % i == 0:                         
                return False
        
        return True    

def solution(numbers):
    answer = []
    #순열 i개씩 생성
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))   
        # print(arr)
        for j in range(len(arr)):
            num = int(''.join(map(str,arr[j])))   
            if is_prime(num):
                answer.append(num)
    answer = list(set(answer))  
    return len(answer)

# numbers로 만들수 있는 수 그게 소수인지 체크