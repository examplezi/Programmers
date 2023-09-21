#from math import sqrt, ceil
# from collections import deque
# def solution(n, s):
#     answer = []
#     sets = deque([])
#     if n > s:
#         return [-1]
#     for i in range(1,s):
#         print(i)
        
    
def solution(n, s):
    answer = []
    
    if s<n:
        return [-1]
    
    num = s//n
    rest = s%n
    
    for idx in range(n):
        answer.append(num)
    
    if rest != 0:
        for a in range(len(answer)):
            answer[a] += 1
            rest -= 1
            if rest == 0:
                break
    
    answer.sort()
    return answer