import sys

arr = list(map(int, input().split()))
#print(arr)
asc = sorted(arr)
dsc = sorted(arr,reverse = True)
# print(asc)
# print(dsc)
if arr == asc:
    print("ascending")
elif arr == dsc:
    print("descending")
else:
    print("mixed")