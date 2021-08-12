def solution(answers):
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    
    count = [[0,1],[0,2],[0,3]]
    for i in range(len(answers)):
        if person1[i%len(person1)] == answers[i]:
            count[0][0] += 1
        if person2[i%len(person2)] == answers[i]:
            count[1][0] += 1
        if person3[i%len(person3)] == answers[i]:
            count[2][0] += 1
    
    answer = []
    for c in count:
        if max(count)[0] == c[0]:
            answer.append(c[1])
    return answer