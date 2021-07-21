# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #예외 처리
        if not matrix:
            return False
        
        #첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) -1
        
        while row <= len(matrix) -1 and col >= 0:
            if target == matrix[row][col]:
                return True
            #타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            #타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False
        
# 파이썬다운 방식
# return any(target in row for in matrix)