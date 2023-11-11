import sys
from itertools import combinations, product
input = sys.stdin.readline
n,s = map(int, input().split())
arr = list(map(int,input().split()))

# count = [list(map(int, input().split())) for _ in range(m)]
#print(arr)

result = set()
cnt = 0
for i in range(1,n+1):

    for j in combinations(arr,i):
        #print(j, sum(j))
        if sum(j) == s:
            cnt += 1
print(cnt)