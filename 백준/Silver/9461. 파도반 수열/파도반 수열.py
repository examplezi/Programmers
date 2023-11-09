import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0,1,1,1]
for i in range(4, max(arr)+1):
   
    dp.append(dp[i-2] + dp[i-3])


for i in arr:
    print(dp[i])