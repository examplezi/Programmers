from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
#     visited =[0]*len(words)

    q = deque()
    q.append((begin,0))
#     cnt = 0
    while q:
        visited = [0]*len(words)
        b,idx = q.popleft()
        if b == target:
            break
        for i in range(len(words)):
            for j in range(len(words[i])):
                if b[j] == words[i][j]:
                    visited[i] +=1
        for i in range(len(visited)):
            if visited[i] == (len(target)-1):
                q.append((words[i],idx+1))
                words[i] = str(idx)


    return idx
