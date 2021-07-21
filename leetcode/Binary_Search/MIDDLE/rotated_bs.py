# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = nums.index(min(nums))
        # print(pivot)
        
        def binary_search(left, right):
            if left <= right:
                mid = left + (right-left)//2
                mid_pivot = (mid + pivot) % len(nums)
                if nums[mid_pivot] < target:
                    return binary_search(mid+1, right)
                if nums[mid_pivot] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid_pivot
            else:
                # print("hi")
                return -1
            
        if not nums:
            return -1
        
        return binary_search(0,len(nums)-1)
        
    
        