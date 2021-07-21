# https://leetcode.com/problems/hamming-distance

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #다르면 1 리턴 더하기
        return bin(x^y).count('1')