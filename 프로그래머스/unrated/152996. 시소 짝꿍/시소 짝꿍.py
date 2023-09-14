#weights의 길이가 최대 10만이기 때문에 O(n^2)보다 좋은 알고리즘을 생각
#weights를 한번만 순회하여 답을 구하는 것이 목표!

            
from collections import Counter
def solution(weights):
    answer = 0
    # 나올 수 있는 비율 : 1:1, 2:3, 2:4, 3:4
    
    # 1:1 , 같은 무게인 사람 골라내기, 2명씩 뽑는 경우의 수 만큼 짝꿍
    counter = Counter(weights)
    print(counter)
    for k,v in counter.items():
        if v>=2:
            answer+= v*(v-1)//2 # 조합 계산식 vC2
    weights = set(weights) # 중복 제거

    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        print(w)
        if w*2/3 in weights: # 270, 180 
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights: # 360, 180 
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights: # 360, 270
            answer+= counter[w*3/4] * counter[w]
    return answer