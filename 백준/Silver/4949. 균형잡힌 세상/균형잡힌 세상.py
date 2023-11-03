while True:
    line = input()
    
    if line == '.':
        break
    else:
        stack = []
        check = True
        for char in line:
            if char in '([':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    check = False
                    break
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    check = False
                    break

        if check and not stack:
            print("yes")
        else:
            print("no")
