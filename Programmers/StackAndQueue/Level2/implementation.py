import math

def solution(progresses, speeds):
    queue = []
    for progress, speed in zip(progresses, speeds):
        rest = 100-progress
        take = math.ceil(rest/speed)
        queue.append(take)
    print(queue)
    answer = []    
    while queue:
        first = queue.pop(0)
        count = 1
        while queue and first >= queue[0]:
            queue.pop(0)
            count += 1
        answer.append(count)
            
    return answer

#100프로가 되면 서비스 반영 가능
#개발 속도는 전부 다름, 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 될 수 있다. 
#하지만 앞에 있는 기능이 완성 될 때 함께 배포가 된다. 
#FIFO
#배포는 하루에 한번만 이루어짐..! 하루동안 다 차있는거 배포. 



