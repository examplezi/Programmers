import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    num = int(input())
    #print(num)
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))
