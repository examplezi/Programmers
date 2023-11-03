import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)
arr = sorted(arr, key= lambda x: (x[1],x[0]))
#print(arr)
for i in arr:
    print(i[0],i[1])