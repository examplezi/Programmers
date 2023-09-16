def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(v): # 노드 안 
        visited[v] = True # 셀프 루프 제거 
        for j in range(n):
            if computers[v][j] == 1 and visited[j] == False:
                dfs(j) # 다음 연결된 노드로 가려면 반복 증가하는 j
    
    
    for i in range(n):
        #print(i)
        if visited[i] == False: #방문이 안되어 있으면
            dfs(i) # 안에 들어가서 살펴봐라, dfs가 끝나면 다시 돌아옴
            answer += 1 # 연결된 노드 모두 조사 후에 + 1
    return answer
    
    