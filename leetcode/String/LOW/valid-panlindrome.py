# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1단계 리스트를 lower case로 만들고
        #2단계 reverse copy한다
        #3간계 2개의 리스트를 비교 한다. 
        
        lower_s = [l.lower() for l in s if l.isalnum()]
        reverse_lower_s = lower_s[::-1]
        # print(f'lower_s: {lower_s}')
        # print(f'reverse_lower_s: {reverse_lower_s}')
        if lower_s == reverse_lower_s:
            return True
        else:
            return False

    # 뒤에서부터 pop으로 푸는 방식도 존재할 수도 있다. 
    # deque를 사용하면 O(n)으로 엄청난 성능 향상을 가져온다. 
    # collections.deque() 

    #slicing을 이용한 방법
    #c로 되어 있어서 훨씬더 빠르다. 
    #s = s.lower()
    #s = re.sub('[^a-z0-9]', '', s)
    #return s == s[::-1]

