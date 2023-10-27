import sys
input = sys.stdin.readline


n= int(input())

#arr = [ mfor _ in range(n)]
arr = list(map(int, input().split()))
#print(arr)
print(min(arr),max(arr))