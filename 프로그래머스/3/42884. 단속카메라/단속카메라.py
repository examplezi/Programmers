# 모든 차량이 한번은 단속 카메라 만남 -> 최소 카메라 개수
# bfs => 큐, 와일
# 정렬이 필요할거 같음
# from collections import deque
# def solution(routes):
#     answer = 0
#     routes.sort(key = lambda x: x[1])
#     q =deque()
#     routes = deque(routes)
#     print("경로",routes)
#     q.append(routes.popleft())
#     #print("경로2",route
#     while routes:
#         if not q:  # q가 비어 있으면 루프 종료
#             break
#         start, end = q.popleft()

#         if not routes:  # routes가 비어 있으면 루프 종료
#             break
#         next_route = routes[0]

#         while end != start:
#             start += 1
#             if end < next_route[0]:
#                 answer += 1
#                 routes.popleft()
#                 if routes:  # routes가 비어 있지 않은 경우에만 q에 추가
#                     q.append((routes[0][0], routes[0][1]))
#                     routes.popleft()
#                     print("경로는", routes)
#                 break
#             if start == end and end >= next_route[0] and end <= next_route[1]:
#                 answer += 1
#                 routes.popleft()
#                 if routes:  # routes가 비어 있지 않은 경우에만 q에 추가
#                     q.append((routes[0][0], routes[0][1]))
#                     routes.popleft()
#                 break

#     return answer 

#     for i in range(len(routes)):
#         start, end = q.popleft()
#         print("q는 비었을까요",q, len(routes),routes)
#         # 탈출조건
#         if len(routes) == 0:
#             break
            
#         while end != start:
#             start += 1
#             if start == end and end >=routes[i][0] and end <= routes[i][1]:  
#                 answer += 1
#                 print(answer)
#                 q.append((routes[i][0],routes[i][1]))
#                 routes.popleft()
#                 break
                
        # start +1 해주면서 start == end and end >= routes[i][0] and end <= routes[i][1]
        # => answer + 1, popleft()
def solution(routes):
    routes.sort()
    answer = 0

    camera = routes[0]

    for i in routes[1:]:
        if i[0]<=camera[1]:
            camera = [i[0], min(i[1], camera[1])]
        else:
            camera = i
            answer+=1


    return answer+1
                    
        