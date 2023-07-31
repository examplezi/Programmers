from math import ceil
def solution(n,a,b):
    answer = 0
    
   
    while n > 1: # if 조건 걸어주기 
        n = n // 2
        a = a / 2
        b = b / 2
        print("b나눗셈 후", b)
        a = ceil(a)
        b = ceil(b)
        answer += 1
        print(n, answer, a, b)
        if a == b:
            break
    return answer