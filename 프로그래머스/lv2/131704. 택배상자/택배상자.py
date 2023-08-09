def solution(order):
    answer = 0
    tmp = [] # 임시 컨테이너 
    i=1 # [1,2,3,4,5] 기존 순서 유지 
    
    while i != len(order)+1:
        tmp.append(i)
        while tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
            if len(tmp) == 0:
                break
        i += 1
    return answer



# from collections import deque
# def solution(order):
#     stack = []
#     answer = 0
#     length = len(order)
#     order = deque(order)
#     while length > 0:
#         isTrue = False
#         for i in range(1, len(order) + 1):
#             #print("아이는",i)
#             if stack and order[0] < stack[-1]:
#                 break
#             if i == order[0]: # i = 4
#                 order.popleft()
#                 answer += 1
#                 isTrue = True
#                 break
#             elif stack and order[0] == stack[-1]: # i = 5
#                 #print("order[0] == stack[-1]:", i)
#                 stack.pop()
#                 order.popleft()
#                 answer += 1
#                 isTrue = True
#                 break
#             elif i < order[0]:
#                 stack.append(i)
#         if isTrue == False:
#             break
#         length -= 1
#         #print(i,answer,stack, length)
#     return answer


    
    