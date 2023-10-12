# 백트랙킹 -> bfs 
# 방문하지 않았던 곳의 길이 visited로 움직였을 때, 0이라면 answer += 1 
# 좌표 밖으로 벗어낫으면 -> continue 
# U[i][j+1] D[i][j-1] L[i-1][j] R[i+1][j] 
# def solution(dirs):
#     answer = 0
#     graph = [ 11 * [0] for _ in range(11)]
#     graph[5][5] = 1
#     #print(graph)
#     # dirs 길이 같게 해줄 순 없나? 
#     if len(dirs) < len(graph):
#         dirs += "0" * (len(graph) - len(dirs))
#     print(dirs)
    
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             start = graph[5][5]
#             print(i,j, graph[i][j],dirs[j])
#             if dirs[j] == "D" and graph[i][j] == 0:
#                 graph[i][j-1] = 1 
            
#             if dirs[j] == "U" and graph[i][j] == 0:
#                 graph[i][j+1] = 1
                
#             if dirs[j] == "L" and graph[i][j] == 0:
#                 graph[i-1][j] = 1
                
#             if dirs[j] == "R" and graph[i][j] == 0:
#                 graph[i+1][j] = 1
        
          
def solution(dirs):
    answer = 0
    x = 5
    y = 5
    # 'U', 'D', 'R', 'L'
    Map = []
    move = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dy,dx) = move[dirs[i]]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        Map.append((x,y,x+dx,y+dy))
        Map.append((x+dx,y+dy,x,y))
        x = x + dx
        y = y + dy
    mapSet = set(Map)
    answer=len(mapSet)//2

    return answer