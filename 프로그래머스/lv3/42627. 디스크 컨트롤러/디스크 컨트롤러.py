# import heapq
# def solution(jobs):
#     answer = 0
#     tunnel = []
#     cnt = len(jobs)
#     time = 0
#     #jobs = heapq.heapify(jobs) #None
#     #while jobs:
#     for i in range(len(jobs)):
#         befar = jobs[i][0]
#         if not befar:
#             befar = 0
#         print(befar)
#     while jobs:
#         if len(tunnel) == 0: # 터널이 비었으면 while len(tunnel) > 0
#             first = heapq.heappop(jobs)
#             tunnel.append(first)
#             time += befar +tunnel[0][1] - tunnel[0][0]
#             #first[1]  = first[1] - 1
#             tunnel.pop()
#             print(time, first[0], first[1])
#             #break
# #print(time // cnt)
        
#     return time // cnt

import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시점 기준으로 정렬
    time, total_time, cnt = 0, 0, len(jobs)
    heap = []  # 최소 힙 (소요 시간 기준)

    while jobs or heap:
        # 현재 시점에서 처리 가능한 작업들을 heap에 추가
        while jobs and jobs[0][0] <= time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(heap, (processing_time, request_time))
        
        if heap:
            # heap에서 소요 시간이 가장 짧은 작업 선택
            processing_time, request_time = heapq.heappop(heap)
            time += processing_time
            total_time += time - request_time
        else:
            # 현재 시점에서 처리 가능한 작업이 없으면 시간을 1 증가
            time += 1

    return total_time // cnt