# return에 idx가 들어감
# 카운터, dict
def solution(genres, plays):
    answer = []
    priority = {}
    location = [] 
    result = []
    #return answer
    for idx, count in enumerate(plays):
        location.append((idx, count))
    location.sort(key=lambda x: (x[1], x[0]))
    print(location, "위치")
    
    for x,y in zip(genres, plays):
        answer.append((x,y))
    answer = sorted(answer, key = lambda x:(x[0], x[-1]), reverse = True)
    #print("answer", answer)
    
    for g, p in answer:
        if g not in priority:
            priority[g] = p
        else:
            priority[g] += p
  
    priority = sorted(priority.items(),key = lambda item: item[1], reverse =True)
    priority = [list(i) for i in priority]
    #print(priority)
    
    for pri in priority:
        g, p = pri
        count = 0
        for sets in answer:  # 여기서 sets는 튜플
            #while pri[1] > 0 and count < 2:
            if g == sets[0] and pri[1] > 0 and count < 2:
                pri[1] -= sets[1]  # p -= sets[1]를 통해 p의 값을 변경해도 원본 priority의 값은 변경되지 않습니다.
                count +=1
                for idx, value in location:
                    if value == sets[1]:
                        result.append(idx)
                        location.remove((idx, value)) 
                        break
        #print("after", priority, count)
    return result
        
        
        
        
        
        
    # for g,p in priority:
    #     #print(g,p)
    #     # while p > 0 and 횟수 2번 이하 count < 2
    #     # g in answer -> max
    #     for sets in answer:
    #         print("시작",g,p,sets, sets[0], sets[1])
    #         if g == sets[0]:
    #             p -= sets[1] # 튜플 형태로 있어서 수정 안댐
    #         print("빼고 난 후",priority)
    
        