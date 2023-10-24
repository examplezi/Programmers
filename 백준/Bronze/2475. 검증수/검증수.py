arr = list(map(int, input().split()))


arr = [i **2 for i in arr]

print(sum(arr) % 10 )