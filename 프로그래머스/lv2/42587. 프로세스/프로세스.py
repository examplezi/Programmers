#레퍼런스 코드
from collections import deque

def solution(priorities, location):
    result = []
    queue = deque()

    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))
    #print(queue)
    while queue:
        current = queue.popleft()
        #print(current)
        if any(current[0] < idx[0] for idx in queue):
            # 큐에 뒤에 다시 추가
            queue.append(current)
        else:
            result.append(current)			
            if current[1] == location:
                return len(result)
    #print(result)
            
#     for idx, priority in enumerate(result):
#         if priority[1] == location:
#             return idx + 1