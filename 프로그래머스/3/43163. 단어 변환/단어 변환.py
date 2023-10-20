from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin,0))
    
    
    while q:
        visited = [0] * len(words)
        begin, count= q.popleft()
        if begin == target:
            break
            
        for i in range(len(words)):
            for j in range(len(words[i])):
                #print(i,words[i], words[i][j])
                if begin[j] == words[i][j]:
                    visited[i] += 1
        
        #print(visited)
        for i in range(len(visited)):
            if visited[i] == len(begin) - 1:
                q.append((words[i], count+1))
                #q.pop(i)
                words[i] = str(count)
    return count