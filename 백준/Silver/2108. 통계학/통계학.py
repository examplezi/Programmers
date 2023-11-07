import sys

input = sys.stdin.readline
from collections import Counter
n = int(input())
arr = [int(input()) for _ in range(n)]
#print(arr)
arr= sorted(arr)

# def round2(num): # 사사오입 -0.33
#     #print(int(num), "aa")
#     return int(num) + (1 if num - int(num) >= 0.5 else 0)
def round2(num):
    if num < 0:
        return int(num) - (1 if num - int(num) <= -0.5 else 0)
    else:
        return int(num) + (1 if num - int(num) >= 0.5 else 0)

print(round2(sum(arr) / n))
mid = n // 2
#print(mid)
cnt = 0
for _ in arr:
    #cnt += 1
    if cnt == mid:
        print(arr[mid])
    cnt += 1

#print(Counter(arr).most_common())
if len(Counter(arr).most_common()) >= 2:
    if Counter(arr).most_common()[0][1] == Counter(arr).most_common()[1][1]:
        print(Counter(arr).most_common()[1][0])
    else:
        print(Counter(arr).most_common()[0][0])
else:
     print(Counter(arr).most_common()[0][0])

print(arr[-1] - arr[0])