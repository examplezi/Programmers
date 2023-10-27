import sys

input = sys.stdin.readline

n = int(input())

if n >= 90:
    print("A")
elif 80 <= n:
    print("B")
elif 70 <= n:
    print("C")
elif 60 <= n:
    print("D")
else:
    print("F")
