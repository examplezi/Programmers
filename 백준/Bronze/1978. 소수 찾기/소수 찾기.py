from math import sqrt, floor
n = int(input())
arr = list(map(int,input().split()))
total = 0

def is_prime(n):
    if n == 1:
        return False
    div = floor(sqrt(n))
    for i in range(2,div +1):
        if n % i == 0:
            return False
    return True

for i in arr:
    if is_prime(i):
        total += 1
print(total)