
from itertools import combinations
a, b = map(int, input().split())
arr = list(map(int,input().split()))
#print(arr)
total = 0
for i in combinations(arr,3):
    #print(i, sum(i))
    if total < sum(i) and sum(i) <= b:
        total = sum(i)
print(total)