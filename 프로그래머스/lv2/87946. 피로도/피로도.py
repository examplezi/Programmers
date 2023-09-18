# 던전 순서에 따라 탐험 최댓값 구하라 =>순서에 예민, permutaions
#[최소 피로도, 소모피로도]
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        #print(p)
        tmp = k # 현재 남아있는 피로도
        cnt = 0 # 던젼 탐험 갯수
        for need, spend in p:
            #print(need,spend)
            if tmp >= need:
                tmp -= spend
                cnt += 1
        #print(cnt)
        if cnt > answer:
            answer = cnt
    return answer

        