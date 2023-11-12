import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in directions:
            nx = x + i[0]
            ny = y + i[1]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: # 인접하는지 체크 
                q.append((nx, ny))
                graph[nx][ny] = 2
    #print(graph, "체크하고나서")
    
    return 1

T = int(input())
for i in range(T):
    n,m,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    #print(graph)
    #arr = list(map(int,input().split()))
    cab = [list(map(int, input().split())) for _ in range(k)]
    visited = [0] * n
    #print(cab)






    for i, j in cab:
        graph[i][j] = 1
    #print(graph)
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)