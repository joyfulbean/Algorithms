# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        count_heap = []
        
        for c in count :
            #값과 key 푸쉬
            heapq.heappush(count_heap, (-count[c], c))
                
        topk =[]
        #k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(count_heap)[1])
        return topk

#return list(zip(*collections.Counter(nums),most_common(k)))[0]