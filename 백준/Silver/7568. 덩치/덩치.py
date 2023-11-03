
import sys
from collections import deque
input = sys.stdin.readline

body = []
n =int(input())
for i in range(n):
    info = list(map(int, input().split()))
    body.append(info)
#print(body)
ans = []
for i in range(n):
    count = 0
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    ans.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
 
for d in ans:
    print(d,end=" ")
