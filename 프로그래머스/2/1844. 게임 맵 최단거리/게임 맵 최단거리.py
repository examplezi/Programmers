# 최단거리, bfs
from collections import deque
def solution(maps):
    answer = []
    count = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * (m) for _ in range(n)] # m+1?
    print(visited)
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    directions = [[0,1], [0,-1], [1,0], [-1,0]]

    
    while q:
        x, y = q.popleft()
        for i in directions:
            nx = x + i[0]
            ny = y + i[1]
            
            if 0<= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))

                
    if maps[n-1][m-1] == 1: # 업데이트가 되지 않았다는 의미 -> 못간다
        return -1
    else:
        return maps[n-1][m-1]
        #return count
    

    