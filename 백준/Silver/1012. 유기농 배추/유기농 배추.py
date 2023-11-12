import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in directions:
            nx = x + i[0]
            ny = y + i[1]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 2
    return 1







for _ in range(T):
    n,m,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    #   print(graph)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i,j)

    print(cnt)