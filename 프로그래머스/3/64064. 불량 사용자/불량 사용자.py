# 제재 아이디 목록 갯수 
# 모든 글자가 * 처리되어 있는거부터 고정시키기고 user_id에서 제거
# 밴에서 별표 제외하고 문자열만 반환해서 비교 
# def solution(user_id, banned_id):
#     answer = 0
#     user_id.sort()
#     banned_id.sort()
#     print(user_id, banned_id)

import re
from itertools import permutations 

def solution(user_id, banned_id):
    n = len(banned_id)
    banned_id = [i.replace("*", ".") for i in banned_id]
    answer = []

    for i in permutations(user_id, n):
        lst = list(i)
        flag = True
        for j in range(n):
            if re.match(banned_id[j], lst[j]) and (len(banned_id[j]) == len(lst[j])) :
                continue 
            else:
                flag = False
                break
        if flag:
            if sorted(lst) not in answer:
                answer.append(sorted(lst))

    return len(answer) 