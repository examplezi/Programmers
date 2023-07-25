# 1. 큐 선언 q = deque()
# 2. 큐에 시작값 넣어주기 
# 3. while q: 큐가 빌동안 반목해라 
# 4. 큐에서 하나씩 빼서 확인하기 
# 5. visited = [0] * len() 방문했는지 확인하는 용도 
# 6. for문으로 하나씩 직접 다 확인해보기 => 조건이 일치하면 visited += 1 
# 7. 큐가 비었으니 다음 값 append 

# from collections import deque
# def solution(name):
#     answer = 0
#     cnt = 0
#     q = deque()
#     pointer = 
#     forward = deque.rotate(1)
#     backward = deque.rotate(-1)
#     leftward
#     rightward 
#     abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     q.append((abc[0],cnt))
#     print(q)
    

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
from collections import deque
from itertools import product

def solution(name):    
    results = []

    for rs in product((-1,1), repeat=len(name)-1):
        name_deque = deque(name)
        default = deque('A'*len(name))

        for c, r in enumerate([0]+list(rs)):
            default.rotate(r)
            name_deque.rotate(r)
            default[0] = name_deque[0]

            if name_deque == default:
                results.append(c)
                break

    return min(set(results))+sum([min(ord(l)-ord('A'), ord('Z')-ord(l)+1) for l in name])