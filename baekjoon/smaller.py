#https://velog.io/@dlrmwl15/파이썬-입력받기
#파이썬 입력
# in 

original_str = input()
check_str = input()

without_digit = ''
for i in original_str:
    if not i.isdigit():
        without_digit = without_digit + i

if check_str in without_digit:
    print("1")
else:
    print("0")

