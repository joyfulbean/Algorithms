# https://www.acmicpc.net/problem/14697

#난이도:하
#문제 유형:브루트 포스
#실수한 부분: time complexity 최소화를 하기위해 나누기로 접근했을때, 최소 케이스 무시... 
#포인트: 타임 컴플랙시티에 맞게 최적화

#빈 침대 없이 배정이 가능할 경우 표준 출력으로 1을, 불가능할 경우 0을 출력한다.
#A,B,C의 조합 가능한 모든 조합을 시도하는것 뿐..! 

a,b,c,n = map(int, input().split())

a_ = n//a
b_ = n//b
c_ = n//c

# print(a_,b_,c_)

flag = 0 
for i in range(a_+2):
    for j in range(b_+2):
        for k in range(c_+2):
            result = (a*i)+(b*j)+(c*k)
            if result == n:
                print("1")
                flag = 1
                exit(0)

if flag == 0:
    print("0")