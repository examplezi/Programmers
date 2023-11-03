import sys
from math import sqrt

input = sys.stdin.readline # 테스트할 때는 이 줄을 주석 처리하고 사용하시면 됩니다.

n, m = map(int, input().split())

def isPrime(i):
    if i < 2:  # 2 미만의 수는 소수가 아님
        return False
    if i == 2:  # 2는 소수임
        return True
    if i % 2 == 0:  # 2를 제외한 짝수는 소수가 아님
        return False
    for j in range(3, int(sqrt(i)) + 1, 2):  # 홀수 나눗수만 검사
        if i % j == 0:
            return False
    return True  # 위 조건을 모두 통과하면 소수임

for i in range(n, m + 1):
    if isPrime(i):
        print(i)  # 소수일 경우에만 출력
