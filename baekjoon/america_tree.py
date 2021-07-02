# https://www.acmicpc.net/problem/4358
#난이도:하
#문제 유형:딕셔너리 이용
#실수한 부분: 
#포인트: time complexity 최소화를 하기위해 입력을 잘 받고, 한번에 처리하는게 중요.

import sys
from collections import defaultdict
input = sys.stdin.readline
 
tree = defaultdict(int)
cnt = 0
while True:
    name = input().rstrip()
    if name == "":
        break
    tree[name] += 1
    cnt += 1
tname = list(tree.keys())
tname.sort()

for n in tname:
    print("%s %.4f" % (n, tree[n]*100/cnt))

