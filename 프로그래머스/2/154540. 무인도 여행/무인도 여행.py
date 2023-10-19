# from collections import deque
# def solution(maps):
#     answer = []
#     for i in maps:
#         if all(j == 'X' for j in i):
#             return [-1]
#     # x = 바다 -> 100 
#     visited = [ [0] * len(maps[0]) for _ in range(len(maps))]
#     #print(visited)
#     for i in range(len(maps)):
#         for j in range(len(maps[i])):
#             #print(i,j)
#             if maps[i][j] == 'X':
#                 visited[i][j] = 100
#     #print(visited)
#     direction = [[1,0], [-1,0], [0,1], [0,-1]]
#     q = deque()
#     q.append((0,0)) # 시작값
#     count = 0
#     #visited[0][0] = 1  # 시작 위치 방문 처리
#     while q:
#         x,y = q.popleft()
#         for i in direction:
#             nx = x + i[0]
#             ny = y + i[1]
#             if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
#                 # 큐, 방문처리
#                 visited[nx][ny] = 1
#                 count += int(maps[nx][ny])
#                 q.append((nx,ny))
#     answer.append(count)
    
#     for i in range(len(visited)):
#         for j in range(len(visited[i])):
#             if visited[i][j] == 0:
#                 answer.append(int(maps[i][j]))
#     return sorted(answer)


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, r, c, visited, field):
    q = deque([(x, y)])
    visited[x][y] = 1
    cost = int(field[x][y])

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and field[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cost += int(field[nx][ny])
                    q.append((nx, ny))

    return visited, cost   

def solution(maps):
    answer = []
    r, c = len(maps), len(maps[0])
    visited = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited, ans = bfs(i, j, r, c, visited, maps)
                answer.append(ans)

    return sorted(answer) if answer else [-1]