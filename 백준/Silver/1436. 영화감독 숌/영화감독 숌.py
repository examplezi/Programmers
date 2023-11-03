n = int(input())
cnt = 0
result = 666
 
while True:
    if '666' in str(result):
        cnt += 1
        #print(cnt, result)
 
    if cnt == n:
        break
 
    result += 1
    #print(result)
 
print(result)