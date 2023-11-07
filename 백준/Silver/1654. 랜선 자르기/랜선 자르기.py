import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 이진 탐색을 위한 초기 설정
start = 1
end = max(arr)

# 이진 탐색 실행
while start <= end:
    mid = (start + end) // 2  # 중간 길이
    cnt = sum(lan // mid for lan in arr)  # 중간 길이로 만들 수 있는 랜선의 수

    if cnt >= k:  # 충분한 수의 랜선을 만들 수 있는 경우
        result = mid  # 현재 길이를 결과로 저장
        start = mid + 1  # 더 긴 길이 탐색
    else:  # 부족한 경우
        end = mid - 1  # 더 짧은 길이 탐색

print(result)
