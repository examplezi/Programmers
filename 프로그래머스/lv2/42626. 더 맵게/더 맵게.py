# from collections import deque
# def solution(scoville, K):
#     cnt= 0
#     fail = -1
#     #queue = deque(scoville)
#     scoville.sort()
#     queue = deque(scoville)
    
#     #while len(queue) > 1:
#     # 뭔차이지..? 
#     #q[0]이 K 이상인지 확인하는 게 이미 음식을 섞고 난 후이기 때문에 
#      # k = 4, queue = [5,6,7] 인 경우 섞을 필요가 없기 때문에
#     while queue[0] < K and len(queue) > 1:
#         first = queue.popleft()
#         second = queue.popleft()
       
#         spicy = first + (second * 2)
#         cnt += 1
#         queue.append(spicy)
#         #list(queue).sort()
#         queue = deque(sorted(list(queue)))  # 오름차순으로 재정렬
#         #print(first, second, queue, spicy, cnt)
#         if all(value >= K for value in queue):
#             break
#     #     else:
#     #         cnt = -1
#     # return cnt
#     if all(value >= K for value in queue):
#         return cnt
#     else:
#         return fail

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer
  