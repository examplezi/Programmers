import sys
input = sys.stdin.readline
n = int(input())
#print(n)
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)

for i in arr:
    print(sum(i))