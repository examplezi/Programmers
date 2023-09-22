# # 오른쪽, 아래로만 움직임 
# from collections import deque
# def solution(m, n, puddles):
#     # 방문 여부 -> paddles 부분을 True 바꿔줌 
#     # 방향키
#     visited = [[False] * (m+1) for _ in range(n+1)] # 인덱스 맞추기 위해 +1
#     answer = 0
#     for i in range(len(puddles)):
#         visited[puddles[i][0]][puddles[i][1]] = True
#     #visited[0] = True
#     for i in range(len(visited)):
#         visited[0][i] = True
#     #print(visited)
#     direction = [[1,0], [0,1]]
#     # dx = [1, 0]
#     # dy = [0, 1]
#     queue = deque([(1,1,1)])
#     visited[1][1] = True
    
#     while queue:
#         x,y,count = queue.popleft()
#         for i in direction:
        
#             nx = x + i[0]
#             ny = y + i[1]
#             if 0<= nx and nx < n and 0 <= ny and ny < m and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx,ny,count+1))
#     return count % 1000000007
def solution(m, n, puddles):
    a = [[0]*(m+1) for _ in range(n+1)]
    for i, j in puddles:
        a[j][i] = 1
    a[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i][j]:
                a[i][j] = 0
            else:
                a[i][j] = (a[i-1][j]+a[i][j-1]) % 1_000_000_007
    return a[-1][-1]