# def solution(n, computers):
#     answer = 0
#     visited = []

#     def newRoot (i,n,visited):
#         for j in range(n):
#             print(j)
#             if computers[i][j] == 1 and j not in visited:
#                 visited.append(j)
#                 newRoot(j,n,visited)

#     for i in range(n):
    
#         if i not in visited :
#             visited.append(i)
#             answer = answer+1
#             print(i,n,visited, answer)
#             newRoot(i,n,visited)

#     return answer

# def solution(n, computers):
#     answer = 0
#     visited = [False for i in range(n)]
#     print(visited)
#     for com in range(n):
#         if visited[com] == False:
#             DFS(n, computers, com, visited)
#             answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
#     return answer

# def DFS(n, computers, com, visited):
#     visited[com] = True
#     for connect in range(n):
#         if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
#             if visited[connect] == False:
#                 DFS(n, computers, connect, visited) 
#         print(com,connect, visited)


# def solution(n, computers):
#     answer = 0

#     queue = []
#     visited = []

#     for a in range(n):
#         if a not in visited:
#             print("a는 뭐가 있을까", a)
#             queue.append(a)
#             print("0,2가 들어가야", queue)
#             answer += 1
#             print("앤써- ",answer)
#             while queue :
#                 now = queue.pop(0)
#                 print("queue.pop(0)", queue, visited)
#                 for i in range(n):
#                     if computers[now][i] == 1 and i not in visited:
#                         visited.append(i)
#                         queue.append(i)
#                         print("queue", queue, visited)
#     print(visited, answer)
#     return answer

def solution(n, computers):
    answer = 0

    queue = []
    visited = []

    for a in range(n):
        print("a는 뭘까",range(a))
        if a not in visited:
            print("a는 뭐가 있을까", a)
            queue.append(a)
            print("0,2가 들어가야", queue)
            answer += 1
            print("앤써- ",answer)
            while queue :
                now = queue.pop(0)
                print("queue.pop(0)",now, queue, visited)
                for i in range(n):
                    print("i값은", i)
                    if computers[now][i] == 1 and i not in visited:
                        visited.append(i)
                        queue.append(i)
                        print("queue", queue, visited)
    print("11112222",visited, answer)
    return answer