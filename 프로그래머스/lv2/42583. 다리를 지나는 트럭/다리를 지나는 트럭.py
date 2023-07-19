# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     #queue에서 앞에 트럭부터 하나씩 빼서 ing에 넣기(max weight), 
#     answer = 0
#     ing = deque([0 for _ in range(bridge_length)])
#     queue = deque(truck_weights)
#     print("다리를 지나는 트럭",ing,"대기큐", queue)
    
# #     #while len(ing) > 0:
# #     if max(ing)== 0:
# #         ing.pop()
# #         #ing.appendleft(queue[0])
# #         ing.appendleft(queue.popleft())
# #         #queue.popleft()  
# #         answer += 1
# #         print(ing,queue)
     

# #     elif sum(ing) + queue[0]  <= weight: # sum(ing) + queue[0] <= weight
# #         ing.pop()
# #         ing.appendleft(queue.popleft())
# #         answer += 1
# #         print(queue,ing, "바보")
    
# #     else: # sum(ing) + queue[0] >= weight, 그리고 ing에 있는 시간이 다 되었다면 popleft()
# #         answer += 1
#     allocation_time = deque([0] * bridge_length)  # 트럭의 할당 시간을 저장하는 큐
#     print("이게 답이 아니라고?",ing, allocation_time)
# #     while len(ing) > 0:
# #         if max(ing) == 0:
# #             ing.popleft()
# #             ing.appendleft(queue.popleft())
# #             allocation_time.popleft()
# #             answer += 1
# #             allocation_time.appendleft(answer)

# #             print(ing, queue, allocation_time)

# #         elif sum(ing) + queue[0]  <= weight: # sum(ing) + queue[0] <= weight
# #             ing.pop()
# #             ing.appendleft(queue.popleft())
# #             answer += 1
# #             #allocation_time[0] += 1
# #             print(queue,ing, "바보")
# #             if len(allocation_time) < bridge_length:
# #                 allocation_time.appendleft(0)
# #             else:
# #                 allocation_time[0] += 1
# #             print(queue, ing, allocation_time)

# #         else:
# #             if bridge_length - allocation_time[0] == 0:
# #                 ing.popleft()
# #                 allocation_time.popleft()
# #             else:
# #                 answer += 1
# #                 allocation_time[0] += 1
# #                 print(ing, queue, allocation_time)

# #     return answer
from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0]*bridge_length)
    orders = deque(truck_weights)
    time=0
    total=0
    while orders:
        time+=1
        total -= queue[0]
        queue.popleft()
        if total + orders[0] > weight:
            queue.append(0)
        else:
            w = orders.popleft()
            total+=w
            queue.append(w)

    return time+bridge_length