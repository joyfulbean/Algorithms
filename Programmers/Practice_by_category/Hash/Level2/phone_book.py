def solution(phone_book):
    ### 효율성 검사 실패
#     phone_book.sort(key=lambda x:len(x), reverse=True)
    
#     while phone_book:
#         check = phone_book.pop()
#         for i in phone_book:
#             if i[:len(check)] == check:
#                 return False
###### string sorting은 1000,1001,1011 맨앞에 1을 기준으로 sorting이 된다. 
    
    phone_book.sort()
    
    for i in range(0,len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True