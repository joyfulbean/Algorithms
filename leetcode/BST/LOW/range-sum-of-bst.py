# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#브루투 포스 방식이다. 최적화는 아래의 코드를 참조하자. 
class Solution(object):
    result = 0
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root:
            root.right = self.rangeSumBST(root.right, low, high)
            if root.val >= low and root.val <= high:
                self.result += root.val
            root.left = self.rangeSumBST(root.left, low, high)
        
            return self.result
        # 왼쪽은 작은것 오른쪽은 큰것이라는 사실을 이용하자.
        # 목표는 L보다 크거나 같고, R보다 작거나 같은걸 찾는것이다. 
        # if node.val < L:
        #   return dfs(node.right)
        # if node.val > R:
        #   return dfs(node.left)
        #return node.val + dfs(node.left) + dfs(node.right)
        
