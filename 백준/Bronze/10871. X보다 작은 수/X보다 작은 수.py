n, m = map(int, input().split())
#print(n,m)
arr = list(map(int, input().split()))
#print(arr)


result = []
for i in arr:
    if i < m:
        print(i, end= ' ')