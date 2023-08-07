
#from collections import deque 
def solution(n):
    jump = 0
    # visited = [0] * n
    # q = deque()
    # q.append(0)
    #print(q, visited)
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            #print("짝수", n, jump)
        else:
            jump += 1
            n = n // 2
            #print("홀수", n, jump)
            if n == 1:
                jump += 1
                #print("마지막 1", n, jump)
                break
       
    return jump
    
    