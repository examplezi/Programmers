from collections import Counter
def solution(s):
    
    cnt, zero = 0, 0
    while s != '1':
        cnt += 1
        counter = Counter(s)
        zero += counter['0']
        s = bin(counter['1'])[2:]
    return [cnt, zero]