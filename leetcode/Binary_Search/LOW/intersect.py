# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set()
        nums2.sort()
        for n1 in nums1:
            #이진 검색으로 일치 여부
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2)> i2 and n1==nums2[i2]:
                result.add(n1)
        return result