from collections import deque

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = deque(arr)

result = []
stack = []
current = 1

while current <= n:
    stack.append(current)
    result.append('+')
    current += 1

    while stack and stack[-1] == arr[0]:
        stack.pop()
        arr.popleft()
        result.append('-')

if stack:
    print("NO")
else:
    for res in result:
        print(res)
