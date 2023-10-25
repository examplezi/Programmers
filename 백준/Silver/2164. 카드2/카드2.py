from collections import deque
n = int(input())
# 버리기 횟수 : n -1
# 보내기 횟수 : n -2 
arr = []
for i in range(1,n+1):
    arr.append(i)

arr = deque(arr)
#arr.popleft()
count = 0
#print(q,arr)
while arr:
   #탈출조건
    if len(arr) == 1:
        break
    if count == 0 or count % 2 == 0:
        arr.popleft()
        count += 1
    else: # count 횟수 홀수
        e = arr.popleft()
        arr.append(e)
        count += 1
print(arr[-1])
