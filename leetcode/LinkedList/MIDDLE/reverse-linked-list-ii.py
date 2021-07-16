# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        #예외 처리
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        #start, end 지정
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        #반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next