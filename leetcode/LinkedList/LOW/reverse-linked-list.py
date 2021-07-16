# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node =  head
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev

# ##재귀로 풀이
# if not node:
#     return prev

# next, node.next = node.next, prev
# return reverse(nexxt, node)