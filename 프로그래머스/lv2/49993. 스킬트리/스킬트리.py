def solution(skill, skill_trees):
    answer = []
    for k in skill_trees:
        str1 = ""
        for h in k:
            if h in skill:
                str1 += h
            else:
                continue
        answer.append(str1)
    cnt = 0
    for j in answer:
        if skill[:len(j)] == j:
            cnt += 1
        else:
            continue
    return cnt
    # answer = -1
    # q = deque(skill_trees)
    # # 불가능한걸 다 pop 하고 남은것만 len() 으로 해서 개수? 
    # for i in range(len(q)):
    #     print(q[i][0])
    
    
#     1.1. skill( order ) 외의 값 제거
# 이 값들은 올바른 값인지 영향을 주지 않습니다. 제거하고 시작합니다.
# 규칙 : CBD 일 떄
# tree [ 'BACDE', 'CBADF', 'AECB', 'BDA' ] =>
# tree [ 'BCD', 'CBD', 'CB', 'BD' ]

# 1.2. 제거한 값에서 CBD 값에 대한 인덱스 값만 추출합니다.
# [ [ 1, 0, 2 ], [ 0, 1, 2 ], [ 0, 1 ], [ 1, 2 ] ]

# 1.3. 추출한 인덱스 값이 0부터 순차적으로 구성되어야 올바른 값입니다.
# isRightOrder : [ false, true, true, false ] => 2
  