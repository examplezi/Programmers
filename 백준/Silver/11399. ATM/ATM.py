import sys
input = sys.stdin.readline
n = int(input())
#print(n)

arr = list(map(int,input().split()))
#arr = list(map(int, input().strip()))
arr = sorted(arr)
#print(arr)

total = 0
for i in range(len(arr)):
    total += (arr[i] * (n-i))
print(total)