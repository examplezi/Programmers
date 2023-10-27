import sys
input = sys.stdin.readline


n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

count = 0

for coin in coins:
    count += target // coin
    target %= coin
print(count)