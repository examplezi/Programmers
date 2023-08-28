from collections import deque
def solution(progresses, speeds):
    bundle = list(zip(progresses, speeds)) # 할당 안됨 
    #print(bundle)
    perfect = 0
    day = deque()
    left = []
    answer = []
    # 100 - 각각의 요소 빼서 나머지 
    # speeds 돌면서 각각의 요소에 i를 곱해서 나머지 이상이 될 때까지 count + 1
    
    for i in progresses:
        left.append(100 - i)
    #print(left)
    
    for i in range(len(bundle)):
        perfect = bundle[i][0]
        count = 1
        #print("다시 처음부터",perfect)
        while perfect <= 100:
            perfect = bundle[i][0] + bundle[i][1] * count
            count += 1
            if perfect >= 100:
                #print("qqq",perfect, count)
                day.append(count-1)
                break
    
    while day:
        count = 1
        current = day.popleft()
        while day and day[0] <= current:
            count += 1
            day.popleft()
        answer.append(count)

    return answer
                
    # aaa = []
    # count2 = 0
    # print(day)
    # answer.append(day.popleft())
    # while len(day) > 0:
    #     if
    #     ele = day.popleft()
    #     count2 += 1
    #     #aaa.append(count2)
    #     if ele >= day[0]:
    #         count2 += 1
    #         day.popleft()
    #print("fgkfhh",day)
    #첫째값 >= 둘째값, 순회를 할 때 첫째값보다 작거나 같은 값이 나올 때까지 -> answer.append(len(갯수)),
    # 크거나 같은 값까지 모두 제거? 해주기 
    # while len(day) >0:
    #     # answer.append(day.popleft())
    #     # print( answer, day)
    #     if len(answer) == 0:
    #         answer.append(day.popleft())
    #         #print("비어있을 때")
    #     elif answer[0] >= day[0]:
    #         answer.append(day.popleft())
    #         #print("앞에보다 작거나 같을 때")
    #     else:
    #         aaa.append(len(answer))
    #         answer.clear
    #         #print("횟수 구분될 때")
    # print(aaa,answer)
    # print(count1)
    #     print(day[i])
    #     day.popleft()
    #     print(day)
        #answer.append( day.popleft())
        #print(answer)
        #while len(day) >0:
            
    