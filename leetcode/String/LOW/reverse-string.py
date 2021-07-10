# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

        #s[::] = s[::-1]
        #two pointer 방식:
        #left, right = 0, len(s)-1
        #while left<right:
        #s[left], s[right] = s[right], s[left]
        #left += 1
        #right -= 1