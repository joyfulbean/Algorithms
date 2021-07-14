# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
        
            left = check(root.left)
            right = check(root.right)
        
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1