
from collections import deque

def solution(maps):
    answer = []

    # for i in maps:
    #     if all(j == 'X' for j in i):
    #         return [-1]
        
    if all(all(j == 'X' for j in i) for i in maps):
        return [-1]

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    print(visited)
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'X' or visited[i][j]:
                continue

            q = deque()
            q.append((i, j))  # 시작 위치
            visited[i][j] = 1  # 시작 위치 방문 처리
            count = int(maps[i][j])

            while q:
                x, y = q.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                        visited[nx][ny] = 1
                        count += int(maps[nx][ny])
                        q.append((nx, ny))
            
            answer.append(count)

    return sorted(answer)
