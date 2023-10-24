from collections import Counter

arr = []
for i in range(3):
    arr.append(int(input()))

#print(arr)
total = 1
for i in arr:
    total *= i
arr = list(str(total))
#print(arr)
arr = (Counter(arr))
#print(arr)
# for i in arr:
#     print(i, arr[i])
#print("1111111")

for i in range(10):
    if str(i) in arr:
        print(arr[str(i)])
    else:
        print(0)