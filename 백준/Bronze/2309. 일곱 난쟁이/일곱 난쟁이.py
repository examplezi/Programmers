import sys

from itertools import combinations, permutations
input = sys.stdin.readline
#n = int(input())
arr = [int(input()) for _ in range(9)]
#print(arr)
result = []
for i in combinations(arr,7):
    #print(i, sum(i))
    if sum(i) == 100:
        result.append(i)
        break

#print(result)

for i in result:
    i = sorted(i)
    for j in i:
        print(j)