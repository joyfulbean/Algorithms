possible_product = []
def possible(total):
    for i in range(1,total):
        if total%i == 0:
            if i >= total//i:
                possible_product.append([i,total//i])
    
def solution(brown, yellow):
    total = brown + yellow
    possible(total)
    # print(possible_product)
    for p in possible_product:
        size = p[0]*2 + p[1]*2 - 4
        if size == brown:
            return p