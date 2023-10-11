def solution(m, n, puddles):
    answer = 0
    graph = [[0] * (m+1) for _ in range(n+1)]
    graph[1][1] = 1
    print(graph)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i,j)
            if [j,i] in puddles or graph[i][j] == 1:
                continue
            else: # 이동해라,오른쪽, 아래
                graph[i][j] = graph[i][j-1] + graph[i-1][j]
    print(graph)
    return graph[-1][-1] % 1000000007