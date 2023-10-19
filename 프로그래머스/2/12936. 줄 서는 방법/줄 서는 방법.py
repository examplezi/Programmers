from math import factorial
def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    order = []
    k -= 1
    for i in range(n-1, -1, -1):
        temp = factorial(i)
        q, r = divmod(k, temp)
        k = r
        order.append(q)
    # print(order)
    for idx in order:
        answer.append(nums.pop(idx))

    return answer