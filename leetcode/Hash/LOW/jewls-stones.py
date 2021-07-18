# https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # a, A
        result = 0
        for char in jewels:
            result += collections.Counter(stones)[char]
        return result

## 파이썬 다운 방식
# return sum(s in J for s in S)

## counter사용

