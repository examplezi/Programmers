# 최소값 -> heapq, bfs 
# 야근 피로도 () 최소화 
# works의 각 요소에 적절하게 n을 분배해서 뺀 요소의 값의 각 제곱의 합이 최소 
# works 를 순회하면서 n을 하나씩 빼는 방법 
from heapq import heapify, heappush, heappop
def solution(n, works):
    # answer = 0
    # min_count = float('inf') 
    
    if sum(works) <= n:
        return 0
#     for i in range(1,n+1):
#         print(i)
    
    
#     return answer
    works = [(-1) * work for work in works]
    heapify(works)
    while n:
        curr_work = heappop(works)
        post_work = curr_work + 1
        heappush(works, post_work)
        n -= 1

    return sum([work ** 2 for work in works])