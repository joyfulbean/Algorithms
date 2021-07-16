# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = []
        if not head:
            return True
        
        node = head
        
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
            
        #팰린드롬 판별
        return q == q[::-1]

# #Linked-List
# rev = None
# slow = fast = head

# #runner를 이용해서 역순 연결 리스트 구성
# while fast and fast.next:
#     fast = fast.next.next
#     rev, rev.next, slow = slow, rev, slow.next
# if fast:
#     slow = slow.next

# while rev and rev.val == slow.val:
#     slow, rev = slow.next, rev.next
# return not rev

