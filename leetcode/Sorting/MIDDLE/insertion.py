# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
# https://leetcode.com/problems/insertion-sort-list/

#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #head는 정렬을 해야할 대상
        #cur은 정렬을 끝낸 대상으로 반복한다. 
        
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            
            #필요한 경우에만 되돌아가라
            if head and cur.val > head.val:
                cur = parent
        return cur.next