# https://leetcode.com/problems/minimum-window-substring

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #필요한 문자 개수
        need = collections.Counter(t)
        #필요한 문자의 전체 개수
        missing = len(t)
        left = start = end = 0
        
        # 오른쪽 포인터 이동, 1부터 시작
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            #필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                #left 가 음수가 아닐때까지, 복원하면서 left를 옴겨준다. 
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                #start and end 와 left 와 right을 비교
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]