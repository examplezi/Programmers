def solution(n, computers):
    answer = 0
    queue = []
    visited = []
    for a in range(n):
        if a not in visited:
            queue.append(a)
            answer += 1
            
            while queue :
                now = queue.pop(0)
                print("queue.pop(0)",now, queue, visited)
                for i in range(n):
                  
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        queue.append(i)
                        print("queue", queue, visited)
  
    return answer