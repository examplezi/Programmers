import sys

input = sys.stdin.readline

arr = set()
for i in range(10):
    n = int(input())
    arr.add(n % 42)
print(len(arr))