n = int(input())
arr = []
for i in range(n):
    a, b = input().split()
    arr.append([int(a),b])
#print(arr)

arr = sorted(arr, key= lambda x : x[0])
#print(arr)
for i in arr:
    a, b = i
    print(a,b)