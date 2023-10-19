# #from itertools import permutations
# def solution(n, k):
#     answer = []
#     arr = []
#     for i in range(1,n+1):
#         arr.append(i)
# #     for i in permutations(arr,n):
# #         answer.append(list(i))

# #     for i in range(len(answer)):
# #         if i+1 == k:
# #             return answer[i]
    
    
# #     itertools 사용 x (n이 커질수록 시간 초과)

# # factorial list로 순회, k의 몫과 나머지를 사용 divmod

# 이 문제는 팩토리얼로 전체 경우의 수를 구하고,
# 거기서 범위를 연산해서 순서를 구해야 합니다.

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    # 총 n!의 경우의 수를 갖고있음
    # 맨 앞의 수가 정해지면 (n - 1)! 의 경우의 수를 가짐
    # k에서 (n - 1)!을 나눴을 때의 몫이 첫번째 오는 자리
    # k에서 (n - 1)!을 나눴을 때의 나머지가 다시 k로 오는 자리
    result = []
    num_list = [i for i in range(1, n + 1)]
    while(n != 0):
        num_case = factorial(n - 1)
        idx = k // num_case
        k = k % num_case
        if k == 0:
            result.append(num_list.pop(idx - 1))
        else:
            result.append(num_list.pop(idx))
        n -= 1
    return result