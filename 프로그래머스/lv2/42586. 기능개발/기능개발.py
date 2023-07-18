# def solution(progresses, speeds):
#     answer = []
#     pair = []
#     deployment = []
#     total = 0
#     for i in zip(progresses, speeds):
#         pair.append(list(i))
#     print(pair)
    
    
#     for p in pair:
#         date = 1
#         rate = p[0] + p[1] * date
#         if rate >= 100:
#             date = 1
#             #deployment.append(date)
#         while rate < 100:
#             date += 1
#             rate = p[0] + p[1] * date
          
#             print(p[0], p[1], rate)
       
#         print("작업완료날짜 : ", date)
#         deployment.append(date)
#     print(deployment)
    
#     for i in range(len(deployment) -1 ):
#         print(deployment[i], deployment[i+1])
#         if deployment[i] >= deployment[i+1]:
#             total += 1
#         else:
#             answer.append(total + 1)
#             total = 0
#     answer.append(total + 1)
#     print(answer)
#     return answer

from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    print(queue)

    while True:
        if not queue: # queue가 비었으면 나와라 
            break

        for i in range(len(queue)):
            queue[i] += speeds[i]
            print(queue[i] )
        count = 0
        while True:

            if not queue:
                answer.append(count)
                break
            if queue[0] >= 100:
                queue.popleft()
                del speeds[0]
                count += 1
            else:
                if count > 0:
                    answer.append(count)
                break
        #print(queue)
    return answer