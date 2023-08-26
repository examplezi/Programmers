def solution(n):
    
    #print(n % 10, int(n /10 ))
    sum = 0
    
    while n > 0 :
        sum += (n % 10)
        n = int(n/10)
    
    return sum