# https://leetcode.com/problems/diameter-of-binary-tree/
# DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = 0
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(left)
            right = dfs(right)
            
            self.longest = max(self.longest, left+right+2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
            