import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

total = [0] * (n+1)
#print(total)
for i in range(1,n+1):
    total[i] = total[i-1] + arr[i-1]
#print(total)
for i in range(m):
    start, end = map(int, input().split())
    #print(start, end)
    print(total[end] - total[start-1])