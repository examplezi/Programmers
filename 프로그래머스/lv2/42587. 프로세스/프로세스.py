# def solution(priorities, location):
#     answer = 0
#     #return answer
#     for i in range(len(priorities)): # i가 location == i  
#         print(i, priorities[i], max(priorities))
     
#         if i == location:
                   
from collections import deque
def solution(priorities, location):
    answer = 0
    my_doc = [0 for _ in range(len(priorities))]
    
    my_doc[location] = 1
    queue = deque(priorities)
    print(my_doc, queue)
    while True:

        if not my_doc or max(my_doc) == 0: #my_doc 리스트가 비어있음
            print('Break!')
            break
        elif max(queue) == queue[0]: #큐의 가장 앞에 있는 문서의 우선순위가 가장 높은 경우
            queue.popleft() # 가장 앞에 있는 것 제거 
            del my_doc[0]
            answer += 1
        else:
            queue.append(queue[0]) #큐의 가장 앞에 있는 문서를 큐의 맨 뒤에 추가
            my_doc.append(my_doc[0])
            #print(queue, my_doc)
            queue.popleft() # popleft()는 deque 에서만 사용 가능 
            del my_doc[0] # 리스트에서 제거 : del 
            #print(queue, my_doc)

    return answer