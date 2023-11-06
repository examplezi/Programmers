import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    count, target = map(int, input().split())
    priorities = list(map(int, input().split()))

    # 각 문서의 인덱스와 우선순위를 함께 저장합니다.
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    
    answer = 0

    while queue:
        current = queue.popleft()
        
        # 현재 문서보다 우선순위가 높은 문서가 대기열에 있으면 뒤로 보냅니다.
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            answer += 1
            # 목표 문서가 인쇄되면 인쇄 순서를 출력합니다.
            if current[1] == target:
                print(answer)
                break
