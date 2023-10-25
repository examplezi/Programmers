from itertools import combinations
a,b = map(int, input().split())
#print(a,b)
arr = []
for i in range(1, a+1):
    arr.append(i)
#print(arr)
total = 0
for i in combinations(arr,b):
    #print(i)
    total += 1
print(total)