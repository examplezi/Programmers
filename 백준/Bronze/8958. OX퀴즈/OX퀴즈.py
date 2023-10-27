import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    qs = input().strip().split('X')
    score = 0
    #print(qs)
    for q in qs:
        length = len(q)
        #print(length)
        score += (length * (length + 1)) // 2  
    print(score)