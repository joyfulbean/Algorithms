https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #문자열을 파싱해서 정렬하고 같은거 끼리 묶기
        #딕셔너리의 리스트 형으로 만들기
        
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
    
    #sorted(b)
    #"".join(sorted(b)) 다시 결합하는 방법
    #alist.sort() 리스트 자체를 제자리 정렬, 리턴값없고 덮어 쓰는 방법이다. 
    #sorted(c, key=len) 길이 순서로 정렬이 된다. 
    #sorted(a,key=fun)
    #def fn(s):
        # return s[0], s[-1]
