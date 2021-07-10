# https://leetcode.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #정규식에서 \w는 문자를 뜻하며, ^는 not을 의미한다. 따라서 위 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다. 
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        #most_common의 리턴형 [(문자,횟수)]
        return counts.most_common(1)[0][0]