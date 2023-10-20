def solution(triangle):
    answer = 0
    n = len(triangle)
    
    while n > 1:
        for i in range(n-1): #0,1,2,3
            triangle[n-2][i] += max(triangle[n-1][i] , triangle[n-1][i+1])
        n -= 1
    answer = triangle[0][0]
    return answer