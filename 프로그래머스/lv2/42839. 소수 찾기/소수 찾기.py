# from itertools import combinations
# import math
# from itertools import permutations
# def solution(numbers):
#     result = set()  # 중복을 허용하지 않는 집합(Set)을 사용하여 중복된 결과 제거
#     for i in range(1, len(numbers) + 1):
#         permutations_list = list(permutations(numbers, i))
#     for perm in permutations_list:
#         result.add(int("".join(perm)))

#     result = sorted(result)  # 결과를 오름차순으로 정렬
#     print(result)  # 출력: [1, 7, 17, 71]
from itertools import permutations
import math

def is_prime(x):    #소수 판별 함수
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = list(numbers)

    a = []
    for i in range(1, len(n)+1):
        a += list(permutations(n, i))   #경우의 수 반환

    b = []
    for i in a:
        b.append(int(''.join(i)))   
    b = list(set(b))    #경우의 수를 int형으로 담은 배열 b 선언

    for i in b:
        if i <= 1:
            continue    #1 이하면 무시
        elif is_prime(i):   # 소수면
            answer += 1     # answer 증가

    return answer    
    
    
   
    # for i in answer:
    #     print(i)
    #     # if i <= 1:
    #     #     #return False
    #     #     continue
    #     if i == 2:
    #         cnt += 1
    #         print(i,cnt, "2인 경우")
    #     elif i % 2 != 0 and i >= 3:
    #         cnt += 1
    #         print(i,cnt, "홀수")
    # print(cnt)
    # return cnt

        # sqrt_n = int(math.sqrt(n))
        # for i in range(3, sqrt_n + 1, 2):
        # if n % i == 0:
        # return False
        # return True
