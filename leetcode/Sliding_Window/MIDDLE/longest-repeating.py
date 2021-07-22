# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right-1]] += 1
            #가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]
            
            #k초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
                