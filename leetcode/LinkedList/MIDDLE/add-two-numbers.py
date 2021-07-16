# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # 1번 2개의 링크드 리스트를 순서내도 읽으며, 거꾸로 숫자를 만든다. 스택을 이용하는게 좋을듯
        # 둘을 더한 값을 이용해서, 다시 링크드 리스트를 만든다. 거꾸로 하나씩 추출.-->str
        
        stack1 = []
        stack2 = []
        node1 = l1
        node2 = l2
        
        while node1 is not None:
            stack1.append(node1.val)
            node1 = node1.next
        
        while node2 is not None:
            stack2.append(node2.val)
            node2 = node2.next
            
        num1, num2 = "", ""
        
        while stack1:
            num1 += str(stack1.pop())
        # print(num1)
        
        while stack2:
            num2 += str(stack2.pop())
        # print(num2)
        
        # 둘의 값을 더한다. 
        result = int(num1) + int(num2)
        # print(result)
        result_list = str(result)
        # print(result_list)
        
        prev = None
        # 링크드 리스트를 만든다. 
        for l in result_list:
            new_node = ListNode(l)
            new_node.next = prev
            prev = new_node
        
        return new_node
        

#몫과 나머지를 구하는 방식
# root = head = ListNode(0)

# carry = 0
# while l1 or l2 or carry:
#     sum = 0
#     if l1:
#         sum += l1.val
#         l1 = l1.next
#     if l2:
#         sum += l2.val
#         l2 = l2.next
        
#     #몫(자리수 올림)과 나머지 (값) 계산
#     carry, val = divmod(sum + carry, 10)
#     head.next = ListNode(val)
#     head = head.next
# return root.next