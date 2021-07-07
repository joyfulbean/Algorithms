# https://leetcode.com/problems/permutations/

# 재귀 알고리즘
#1(next_2개),2(next=1개),3 종료 prev_element전부 복사
#3종료후 팝
#1,2남음
#2 종류후 팝
#1,3 이 prev에 추가된 상태.
#1,3,2 종료 prev_element 전부 복사
#2()로 반복!! 

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        prev_elements = []

        def dfs(elements):
            #리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return results

#라이브러리를 사용한 방식
# list(map(list, itertools.permutation(nums)))

#객체 복사 방식
#b = a[:]
#b = copy.deepcopy(a) 복잡한 이중 배열도 전부 복사 가능! 
#b = a.copy()
