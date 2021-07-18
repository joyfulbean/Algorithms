# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #사용된 char의 index로 위치 기록
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            #이미 등장했던 문자라면 start 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: #최대 부분 문자열 같이 갱신
                max_length = max(max_length, index - start + 1)
            
            #현재 문자의 위치 삽입   
            used[char] = index
            
        return max_length