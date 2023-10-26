import sys
input = sys.stdin.readline
a, b = map(int, input().split())

dict = {}
for i in range(a):
    name = input().rstrip()
    dict[name] = 1
#print(dict)
arr2 = []
for i in range(b):
    name = input().rstrip()
    #arr2.append(name)
    if name in dict:
        arr2.append(name)
print(len(arr2))
arr2 = sorted(arr2)
for i in arr2:
    print(i)