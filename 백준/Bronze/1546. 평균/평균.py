n = int(input())
arr = list(map(int,input().split()))
#print(arr)
max_score = max(arr)
total = 0

for i in arr:
    new_score = (i / max_score) * 100
    total += new_score
print(total / n)