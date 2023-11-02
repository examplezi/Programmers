import sys
from collections import deque
n = int(input())
for _ in range(n):
    nlist = sys.stdin.readline().rstrip()
    stack = []
    for char in nlist:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                stack.append(char)
                break
    if stack:
        print("NO")
    else:
        print("YES")
