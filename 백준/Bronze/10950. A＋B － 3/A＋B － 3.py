import sys
input = sys.stdin.readline


n= int(input())

arr = [ list(map(int, input().split())) for _ in range(n)]
#print(arr)
#arr = list(map(int, input().split()))
for i in arr:
    print(sum(i))