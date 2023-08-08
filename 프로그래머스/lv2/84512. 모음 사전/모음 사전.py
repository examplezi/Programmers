from itertools import product

def solution(word):
    # 만들 수 있는 단어 중복 순열로 생성
    lis = list()
    words = ['A','E','I','O','U']
    for j in range(1,6):
        for i in product(words,repeat=j):
            lis.append(list(i))
    lis.sort()
    # word와 단어 비교
    answer = 0
    for i in lis :
        answer += 1
        st = ''.join(s for s in i)
        if (st == word):
            break
    return answer