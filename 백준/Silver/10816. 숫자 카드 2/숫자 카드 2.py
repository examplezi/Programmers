import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))

k = int(input())
klist = list(map(int, input().split()))


ndict = {}
for i in nlist:
    if i not in ndict:
        ndict[i] = 1
    else:
        ndict[i] += 1

for i in klist:
    if i in ndict:
        print(ndict[i], end=' ')
    else:
        print(0, end=' ')