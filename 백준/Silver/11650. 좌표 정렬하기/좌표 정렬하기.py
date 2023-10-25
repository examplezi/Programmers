arr = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
#print(arr)
arr = sorted(arr, key= lambda x: (x[0],x[1]))
#print(arr)
for i in arr:
    print(i[0],i[1])