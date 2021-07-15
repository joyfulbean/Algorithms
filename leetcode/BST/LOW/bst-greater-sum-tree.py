# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    longest = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
        
        root.right = self.bstToGst(root.right)
        self.longest += root.val
        root.val = self.longest
        root.left = self.bstToGst(root.left)
        
        return root
    
    