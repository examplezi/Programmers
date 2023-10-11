# 최연소니 deque 사용해서 bfs
from collections import deque
def solution(begin, target, words):
  
    q= deque()
    q.append([begin,0])
    
    if target not in words:
        return 0
    while q:
        visited = len(words) * [0] # 반복마다 초기화 해주기 위해 내부 
        b, idx = q.popleft()
        #탈출조건
        if target == b:
            break
        
        for i in range(len(words)):
            print(i,words[i])
            for j in range(len(words[i])):
                print(i,j,words[i][j], b[j])
                if words[i][j] == b[j]:
                    visited[i] += 1
        print(visited)
        for i in range(len(visited)):
            if visited[i] == (len(target) -1):
                q.append((words[i], idx+1))
                words[i] = str(idx) # 중복 반복 막기 위해 
                print(q, words)
    return idx



# from collections import deque
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#     q = deque() # 큐 선언
#     q.append((begin,0)) # 큐에 시작값, 인덱스 
#     print(q)
#     while q:
#         visited = [0]*len(words) # 방문했는지 확인용
#         b,idx = q.popleft() # 큐에서 하나씩 뽑아서 확인 
#         if b == target: # 출구 조건
#             break
#         for i in range(len(words)):
#             for j in range(len(words[i])):
#                 print("알파벳비교",i,j, b[j], words[i][j])
#                 if b[j] == words[i][j]: # 알파벳 비교 
#                     visited[i] +=1 # 단어를 비교하여 알파벳이 얼마나 똑같은게 있는지 
#             print("방문 visited", visited)

#         for i in range(len(visited)):
#             print("같은 알파벳 갯수 들어있다면",visited[i],(len(target)-1))
#             if visited[i] == (len(target)-1):
#                 q.append((words[i],idx+1))
#                 words[i] = str(idx) # 중복해서 큐에 들어가는 것을 방지
#                 print("words[i]", q, words)
     