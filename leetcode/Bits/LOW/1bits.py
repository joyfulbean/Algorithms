# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

#1을 뺀 값과 and 연산 횟수 측정
# count = 0
# while n:
#     n &= n -1
#     count += 1
# return count