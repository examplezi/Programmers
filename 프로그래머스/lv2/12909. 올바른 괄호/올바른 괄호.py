from collections import Counter

def solution(s):
#     stack = []
  
#     for i in s:
        
#         if i == '(':  # '('는 stack에 추가
#             stack.append(i)
#         else:  # i == ')'인 경우
#             if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
#                 return False
#             else:
#                 stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
  
#     return stack==[] # 스택이 비어있으면 true, 아니면 false 반환

    answer = []
    
    # for i in range(len(s)):
    #     if s[0] == ')':
    #         return False
    #     else:
    #         if s[i] == '(' and s[i-1] == ')':
    #             s.replace(s[i], "")
    #             s.replace(s[i+1], "")
    #             print(s)
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")" and stack: # 스택이 비어있지 않으면 
            stack.pop()
        else:
            stack.append(c)
    print(stack)
    # answer = "".join(stack)
    # print(answer)
    if len(stack) >0:
        return False
    else:
        return True
        
