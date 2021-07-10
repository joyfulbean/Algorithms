# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #로그의 앞부분을 제외하고 뒷부분을 가지고, sortingd
        #문자가 있는게 앞, 알파벳 순 --> 식별자 순 -->숫자는 입력한 순
        
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        #[1:]를 키로 지정해서 sorting하고, [0]을 기준으로 다시 sorting
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
        
        return letters + digits