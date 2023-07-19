# from collections import deque

# def solution(prices):
#     answer = [] #deque([0 for _ in range(prices)])
#     queue = deque(prices)
#     while queue:
#         current = queue.popleft()
#         length = 0

#         for i in range(len(queue)): # current 보다 작은 수까지 범위
#             if queue[i] >= current:
             
#                 length += 1
             
#             else: # 현재보다 작다면
#                 length += 1
#                 break
#         answer.append(length)
#     return answer

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer
        