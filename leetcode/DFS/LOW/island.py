# https://leetcode.com/problems/number-of-islands/submissions/
class Solution(object):
    def numIslands(self, grid):
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #맴버 함수로 만들어야 grid 글로벌 선언 안하고, self없이 깔끔한 코드가됨
        
        def dfs(i,j):
            if i<0 or i>= len(grid) or \
                j<0 or j>= len(grid[0]) or \
                grid[i][j] != '1':
                    return 
        #중복 코드 없애기 위한 최적화, 
            grid[i][j] = 0
            #동서 남북 확인하면서 1은 0으로 만들어 주기, 그러다가 주변에서 0을 발견하면 스탑하고, 리턴 
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        #1일때만 하면, 0으로 dfs에서 이미 찾은걸 바꿔주니까 각 섬만 계산 가능
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count
        
        
        
        