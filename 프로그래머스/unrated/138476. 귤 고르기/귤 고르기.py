from collections import Counter
def solution(k, tangerine):
    answer = 0
    survey = Counter(tangerine)
    cnt = survey.most_common() # value 기준 내림차순

  
    filtered = [(t, count) for t, count in cnt if count <= k]
    selected = [(t, count) for t, count in cnt if count > k]
    # print(filtered) # 작은거
    # print(selected) #큰거
    # print(cnt)
    #for i in range(len(selected)):
    if len(selected):
        answer = 1
        return answer
            
    for i in range(len(filtered)):
        if k > 0  :
            k -= cnt[i][1]
            answer += 1
    #print("answer",answer)
    return answer





