#개구간 (s, e)로 표현되는 폭격 미사일은 s와 e에서 발사하는 요격 미사일로는 요격할 수 없습니다.(경계값은 안된다) 
#요격 미사일은 실수인 x 좌표에서도 발사할 수 있습니다. 실수 가능 3.5 뮤조건 .5 
# bfs 
# 	[[1, 4], [3, 7], [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]]
# from collections import deque
# def solution(targets):
#     answer = 1
#     targets.sort()
#     targets = deque(targets)
#     attack = []
#     units = []
#     attack.append(targets.popleft())
#     print(attack, targets)
#     #print(attack[-1][1] )
#     while len(targets) > 0:
#         #print(targets[0][0], targets[0][1])
        
#         if attack[-1][0] <= targets[0][0]:
#             attack.clear()
#             attack.append(targets.popleft())
#             answer += 1
#             #print(answer, targets)
#         elif  attack[0][1] > targets[0][0] and attack[0][1] != targets[0][0]:
#             #answer += 1
#             #attack = []
#             attack.append(targets.popleft())
#             #print("NEW", attack, targets, answer)
#     return answer


def solution(targets):
    targets.sort(key = lambda x: x[1])

    shoot = -1
    cnt = 0
    for target in targets:
        if target[0] > shoot :
            cnt += 1
            shoot = target[1]-0.5

    return cnt