def solution(s):
    # 마지막에 리스트에 남아 있다면 false, 비어있다면 true 
    stack = []
    for i in range(len(s)):
        if i == 0 and s[i] == ')':
            return False
        if not stack:
            stack.append(s[i])
        elif stack and stack[-1] == '(' and s[i] == ')':# 스택에 이미 있고 내 앞에 꺼가 '('라면 삽입
            stack.pop()
            #if # 스택 내부가 라스트 팡이면 업애라 
        else:
            stack.append(s[i])
        #print("for", stack)
    #print(stack)
    if len(stack) >0:
        return False
    else:
        return True