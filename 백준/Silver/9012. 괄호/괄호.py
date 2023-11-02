import sys
input = sys.stdin.readline
n = int(input())
#nlist = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    nlist = list(input().rstrip())
    stack = []
    # for i in range(len(nlist)):
    #     if len(stack) == 0:
    #         stack.append(nlist[i])
    #     elif stack and nlist[i] == ')':
    #         stack.pop()
    #     else:
    #         stack.append(nlist[i])
    # print(stack)
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