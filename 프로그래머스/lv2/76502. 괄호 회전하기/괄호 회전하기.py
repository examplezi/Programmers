def checking(a):
    stack = []
    for i in a:
        if (i == '(') or (i == '{') or (i == '['):
            stack.append(i)
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and i == ']' and stack[-1] == '[':
            stack.pop()     
        else:
            return 0

    if len(stack) == 0:
        return 1
    else:
        return 0

def solution(s):
    arr = list(s)
    result = 0
    cnt = 0
    temp = 0
    while cnt != len(arr):
        cnt += 1
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = temp
        if checking(arr) == 1:
            result += 1

    return result

