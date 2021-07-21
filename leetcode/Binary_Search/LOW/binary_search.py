# https://leetcode.com/problems/binary-search/


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
            
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
        return binary_search(0, len(nums)-1)


# #이진 검색 모듈
# index = bisect.bisect_left(nums, target)
# if index < len(nums) and nums[index]:
#     return index
# else:
#     return -1

# #이진 검색 사용 x
# try:
#     return nums.index(target)
# except ValueError:
#     return -1