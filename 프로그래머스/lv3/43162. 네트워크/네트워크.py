def solution(n, computers):
    answer = 0
    queue = []
    visited = []
    for a in range(n):
        if a not in visited:
            queue.append(a)
            answer += 1
            print(queue)
            while queue : # 큐가 빌때까지 반복
                now = queue.pop(0)    
                for i in range(n):
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        queue.append(i)
                        print(visited,queue)
    return answer