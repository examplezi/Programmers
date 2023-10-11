# 최대값 -> 최소힙 반대로..? 
from collections import deque
# def solution(A, B):
#     answer = 0
#     if min(A) > max(B):
#         return 0
    
#     while B:
#         # for i in range(len(A)):
#         #     for j in range(len(B)): # 0으로 바꾸기
#         #         print(A[i],B[j])
#         if A[i] < B[j]:
#             answer += 1
#             B[j] = 0
#             break
    
    
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    while B:
        if A[0] < B[0]:
            answer += 1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
    return answer

    