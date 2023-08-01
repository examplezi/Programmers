def solution(triangle):
    dp = [[0 for j in i]for i in triangle]
    #a = [[0 for j in i] for i in triangle]
    
    dp[0][0] = triangle[0][0]
   # print(dp)
    a= []
    for i in range(len(triangle)):
        for j in range(i):
            #print(i,j)
            dp[i][j] = max(dp[i][j],dp[i-1][j] + triangle[i][j])
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
            #print(dp)
    return max(dp[-1])