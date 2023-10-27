
import sys

n = int(sys.stdin.readline())
arr = [0] + [int(sys.stdin.readline()) for i in range(1, n + 1)]
#print(n, arr)
if n < 2: 
	print(arr[n])
else:
	dp = [0] * (n + 1)
	dp[1] =arr[1]
	dp[2] = dp[1] +arr[2]
	for i in range(3, n + 1):
		dp[i] = max(dp[i - 2], dp[i - 3] +(arr[i - 1])) +arr[i]
    
	print(dp[n])