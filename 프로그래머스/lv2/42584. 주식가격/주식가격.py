from collections import deque
'''
queue에 하나씩 넣음 
prices에 current보다 작은 요소가 나오면, 작은 요소까지의 거리 len(prices)
current 
'''
def solution(prices):
    answer = [] #deque([0 for _ in range(prices)])
    queue = deque(prices)
    while queue:
        current = queue.popleft()
        count = 0
        for i in queue:
            count += 1
            if current > i:
                break
        answer.append(count)
    return answer
#     while queue:
#         current = queue.popleft()
#         length = 0

#         for i in queue:
#             length += 1
#             if i < current:
#                     break
#         answer.append(length)
#     return answer

        