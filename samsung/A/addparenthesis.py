import sys
max_num = float('-inf')
def dfs(idx,ret):
    global max_num
    if idx == len(op):
        max_num = max(ret,max_num)
        return

    dfs(idx+1, cal(ret, op[idx], num[idx+1]))
    if idx + 1 < len(op):
        dfs(idx+2, cal(ret, op[idx], cal(num[idx+1], op[idx+1], num[idx+2])))



def cal(n1, operation, n2):
    if operation == '*':
        return n1 * n2
    elif operation == '-':
        return n1 - n2
    elif operation == '+':
        return n1 + n2

n = int(input())
expression = list(input())
op = []
num = []

for e in expression:
    if e.isdigit():
        num.append(int(e))
    else:
        op.append(e)

dfs(0,num[0]) 

print(max_num)
