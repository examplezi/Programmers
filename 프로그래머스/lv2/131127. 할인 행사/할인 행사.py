# # want[i] <= discount
# from collections import deque
# def solution(want, number, discount):
#     answer = 0
#     basket = {}
#     queue = deque(discount)
#     length = sum(number)
#     for grocery, count in zip(want, number):
#         if grocery not in basket:
#             basket[grocery] = count
#         else:
#             basket[grocery] += count
#     print(basket)
#     #print(sum(basket.values()))
#     i = 0
# #     for i in range(i+1,len(queue)):
# #         print(i)
    
    
#     while len(queue) > 0:
        
#         if sum(basket.values()) == 0:
#             # popleft() 이거 개수 리턴
#             return answer
#         for i in range(len(queue)): # 0~12 
#             if queue[i] in basket and  basket[queue[i]] > 0:
#                 basket[queue[i]] -= 1
#                 print("인정",queue[i],i)
#                 #i += 1
#                 #answer +=1
#             else:
#                 continue
                #answer +=1
                #i += 1
   
            #print(queue.popleft())
            #queue.popleft() #while - queue 사용, 인덱스가 변하기 떄문 
            # 큐의 길이가 변한다면 while - queue 사용 
            
    # discount를 순회하면서 디스카운트의 요소가 basket에 있다면 해당 요소 카운트 -1
    # want에 없다면 맨 앞 popleft() -> continue 
    # 만약 sum(basket[i][1]) == 0 : 리턴 인덱스 +1
    #return 0
    
    
from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == check:
            answer += 1

    return answer