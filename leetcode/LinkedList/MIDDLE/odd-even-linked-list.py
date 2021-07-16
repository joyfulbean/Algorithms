# https://leetcode.com/problems/odd-even-linked-list/
\
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = head.next
        
        #반복하면서 홀짝 노드 처리 
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        #홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head