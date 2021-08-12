answer = 1000

def is_possible(begin, word):
    
    count = 0
    for i,j in zip(begin, word):
        if i != j:
            count += 1
    if count == 1:
        return word
    else:
        return 0
    
def dfs(now, target, words, k):
    global answer
    
    if now == target:
        answer = k
        return

    for i in range(len(words)):
        next = words[i]
        if is_possible(now, next):
            next_words = words[::]
            next_words.remove(next)
            dfs(next, target, next_words, k+1)
    
def solution(begin, target, words):
    global answer
    
    k = 0
    #target exists
    if target in words:
        print(words)
        dfs(begin,target, words, 0)
    
        return answer
    
    else:
        return 0

