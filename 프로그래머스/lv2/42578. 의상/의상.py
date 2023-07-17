from collections import Counter

def solution(clothes):
    category = Counter([clothes[i][1] for i in range(len(clothes))]).values()
    answer = 1
    # 카테고리 개수 세기 
    print(category)
    for j in category:
        #print(j)
        answer *= (j+1)
        print(answer)
    return answer-1