n = int(input())
#print(n)
result = 0

total = 0
for i in range(1, n+1):
    total = 0
    total += i
    for j in str(i):
     
        total += int(j)
    if n == total:
        result = i
        break
print(result)