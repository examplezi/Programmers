import sys
input = sys.stdin.readline


n, m= map(int, input().split())
#arr = [ input().split() for _ in range(n)]

dict = {}
for i in range(n):
    address, password = input().split()
    dict[address] = password

#print(dict)

for i in range(m):
    target = input().strip()
    #print(target)
    #if target in dict:
    print(dict[target])