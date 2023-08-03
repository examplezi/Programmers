from collections import deque
def solution(cacheSize, cities):
    answer = 0
    time = 0
    queue = deque(maxlen=cacheSize)
    cities = [i.lower() for i in cities]
    cities = deque(cities)
    #print(queue)
    # queue 에 없으면 앞에 추가하고, time += 5 (cache miss)
    # queue 에 있으면 원소를 앞쪽으로 옮기고, time += 1 (cache hit)
    for i in range(len(cities)):
        #if len(queue) == 0:
            #queue.appendleft(cities.popleft())
            #print(queue, cities)
        if cities[i] in queue:
            queue.remove(cities[i])
            #queue.appendleft(cities[i])
            time += 1
        elif cities[i] not in queue and len(queue) < queue.maxlen: # 없고 아직 큐가 안찾다면 
            #queue.appendleft(cities[i])
            time += 5
        else: # queue에 없고 큐가 찼다면
            if len(queue) > 0:
                queue.pop()
            time += 5  # Cache Miss
        queue.appendleft(cities[i])
        #print(queue)
    print(time)
    return time
#         if cities[i] in queue:
#             queue.remove(cities[i])
#             time += 1  # Cache Hit
#         elif cities[i] not in queue and len(queue) < queue.maxlen:  # 없고 아직 큐가 안찾다면
#             time += 5  # Cache Miss
#             queue.appendleft(cities[i])
#         else:
#             time += 5  # Cache Miss
#             queue.pop()  # 가장 오래된 원소 제거 (queue가 꽉 찼으므로)

#         queue.appendleft(cities[i])
#         answer += time

