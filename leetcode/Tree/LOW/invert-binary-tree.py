# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None


#BFS로의 풀이 

# queue = collections.deque([root])

# while queue:
#     node = queue.popleft()
#     if node:
#         node.left, node.right = node.right, node.left
#         queue.append(node.left)
#         queue.append(node.right)
    
    # return root

#DFS
# stack = collections.deque([root])
# while stack:
#     node = stack.pop()
#     if node:
#         node.left, node.right = node.right, node.left
        
#         stack.append(node.left)
#         stack.append(node.right)

#     return root

