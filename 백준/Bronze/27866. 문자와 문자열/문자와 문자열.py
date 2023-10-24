s = input()
n = int(input())


for i in range(len(s)):
    if i+1 == n:
        print(s[i])
        break