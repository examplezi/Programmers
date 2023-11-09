import sys

input = sys.stdin.readline
n = int(input())

cnt = 0
for i in range(1, n+1):
    if i <= 99:  # 두 자리 수 이하는 항상 한수
        cnt += 1
    else:
        arr = [int(j) for j in str(i)]
        length = len(arr)  # 각 숫자에 대한 자릿수 길이 계산
        diffs = {arr[h] - arr[h-1] for h in range(1, length)}  # 연속된 두 자리의 차이를 집합에 저장

        if len(diffs) == 1:  # 모든 차이가 동일하면 한수
            cnt += 1

print(cnt)
