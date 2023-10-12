from math import ceil
def solution(n, stations, w):
    answer = 0
    start = 1
    
    for station in stations:
        end = station - w #3 10
        dt = end - start # 2 4 
        if end > 1 and dt > 0:
            answer += ceil(dt / ((2*w) + 1))
        
        start = station + w + 1 # 6 12
    
    if start <= n: # 12 16
        dt = n - start + 1
        answer += ceil(dt / ((2*w)+1))
    return answer
        