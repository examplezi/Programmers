
# from collections import deque
# def solution(k, dungeons):
#     answer = -1
#     needed = 0
#     consumed = 0
#     result = 0
#     # 1. 필요필요도가 제일 큰 것을 시작(내림차순 정렬 필요)
#     # 2. 소모필요도가 제일 작은 것부터 시작
#     dungeons = deque(sorted(dungeons, key = lambda x : x[0], reverse = True))
#     #dungeons = deque(dungeons)
#     print(dungeons)
#     for i in range(len(dungeons)):
#         print(dungeons[i][0],dungeons[i][1])
#         if dungeons[i][0] > k:
#             dungeons.popleft()
#         else: # 필요피로도가 k보다 작고 다시 정렬 x: x[1]기준으로 
#             # k -= dungeons[i][1] 
#             # result += 1
#             # dungenons.popleft()
    
#     #return answer
    
    
def solution(k, dungeons):
    answer = 0
    answerlist=[0]
    def dundfs(k2,dun2,count2):
        #print("k2 :",k2,"dun2 :", dun2, count2)
        for i in range(len(dun2)):
            if i<len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dundfs(k2-dun2[i][1],dun2[:i]+dun2[i+1:],count2+1)
            elif i==len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dundfs(k2-dun2[i][1],dun2[:i],count2+1)
        answerlist.append(count2)

    count=0
    for i in range(len(dungeons)):
        #print(i)
        if i<len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dundfs(k-dungeons[i][1],dungeons[:i]+dungeons[i+1:],count+1)
        elif i==len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]: # 마지막 리스트
            dundfs(k-dungeons[i][1],dungeons[:i],count+1)
    answer=max(answerlist)

    return answer