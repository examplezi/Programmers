n = int(input())

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    

result = factorial(n)
#print(factorial(n))

cnt = 0
for i in str(result)[::-1]:
    #print(i)
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)