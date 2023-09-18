from collections import deque

def solution(maps):
 
		# n -> 미로의 행 수
 map_rows = len(maps)
 # m -> 미로의 열 수
 map_columns = len(maps[0])
 
 # 방문 여부를 저장하기 위한 2차원 배열
 visited = [[False] * map_columns for _ in range(map_rows)]
 #visited = []
 # for i in range(map_rows):
 #     visited.append([False] * map_columns)
 print(visited)
 # 상하좌우 이동 방향을 정의 : 각 오른쪽, 왼쪽, 아래, 위임.
 direction = [[1,0], [-1,0], [0,1], [0,-1]]
 
 # 시작 노드를 큐에 추가
 queue = deque([(0, 0, 1)])  # (x, y, 이동 횟수)
 visited[0][0] = True
 
 while queue:
     x, y, count = queue.popleft()
     
     # 도착 노드에 도달하면 이동 횟수 반환
		# 왜 -1 씩 해줘야 하냐면 index가 전부 0부터 시작하기 때문에 -1 해줘야 함
     if x == map_rows - 1 and y == map_columns - 1:
         return count
     
     # 상하좌우 이동을 검사
     for i in direction:
         row_x = x + i[0]
         column_y = y + i[1]
         
         # 미로 범위 내에 있고, 길이고 아직 방문하지 않았고 길이 연결되어 있을 때
         if 0 <= row_x < map_rows and 0 <= column_y < map_columns and not visited[row_x][column_y] and maps[row_x][column_y] == 1:
								# 방문 처리
             visited[row_x][column_y] = True
								# 큐에 추가
             queue.append((row_x, column_y, count + 1))
 # 도착점에 도달하지 못한 경우
 return -1