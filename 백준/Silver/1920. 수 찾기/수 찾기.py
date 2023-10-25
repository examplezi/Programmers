n = int(input())
arr = set(map(int,input().split()))
n2 = int(input())
arr2 = list(map(int,input().split()))
# print(arr)
# print(arr2)
for i in arr2:
    if i in arr:
        print(1)
    else:
        print(0)