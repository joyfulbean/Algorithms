# https://leetcode.com/problems/task-scheduler/

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            #개수 순 추출
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
                
            if not counter:
                break
            
            #idle 이 나옴 1개
            result += n - sub_count + 1
        return result