# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = list()
        for n in nums:
            heapq.heappush(heap,-n)
        
        for _ in range(1,k):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)

# #2번째 방법 heapify이용
# heapq.heapify(nums)
# for _ in range(len(nums)-k):
#     heapq.heappop(nums)
# return heapq.heappop(nums)

#heapq 모듈의 nlargest이용. k번째부터 큰값이 순서대로 담기고 여기서 마지막이 k번째 큰 값이다. 
# return heapq.nlargest(k, nums)[-1]

#정렬을 이용한 풀이
# return sorted(nums, reverse=True)[k-1]
