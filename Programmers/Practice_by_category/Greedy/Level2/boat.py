def solution(people, limit):
    people.sort()
    
    l = 0
    r = len(people)-1
    boat = 0
    
    while l <= r:
        result = people[l] + people[r]
        if result > limit:
            r -= 1
        else:
            l += 1
            r -= 1
        boat += 1
    
    return boat