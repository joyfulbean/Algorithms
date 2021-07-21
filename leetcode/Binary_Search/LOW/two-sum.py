# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)- 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left+1, right+1


# # bisect 모듈 + 슬라이싱 제거
# for k,v in enumerate(numbers):
#     expected = target - v
#     i = bisect.bisect_left(numbers, expected, k+1)
#     if i < len(numbers) and numbers[i] == expected:
#         return k+1, i+1