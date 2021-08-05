    # sorted(numbers, cmp=compare)
    
#     #삽입정렬 구현! 
#     for i in range (1,len(numbers)):
#         j = i
#         while(j > 0 and swap_numbers(numbers[j],numbers[j-1])):
#             numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
#             j -= 1
                
    
#     quick = quick_sort(numbers)
#     print(quick)
#     answer = 0


import functools
def comparator(a,b):
    t1,t2 = a+b, b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
    #t1이 크면 1, t2가 크면 -1, 같으면 0 리턴

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer

#충격적인 풀이
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
    
    