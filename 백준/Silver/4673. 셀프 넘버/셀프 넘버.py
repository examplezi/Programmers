arr = set()
total = 0
for i in range(1, 10001):
    com = list(str(i))
    total = sum([int(j) for j in com])
    #print(list(str(i)),total + i )
    arr.add((total+i))
    
    #arr.add(total)
#print(arr)
    # if i < 10:
    #     arr.append(i*2)
    # elif i < 100:
    #     q = i // 10
    #     r = i % 10
    #     arr.append((i + q + r))
    # elif i < 1000:
    #     q = i // 100
    #     r = i % 100
    #     if q + r + i <= 10000:
    #         arr.append((i + q + r))
    # else:
    #     q = i // 1000
    #     r = i % 1000
    #     if q + r + i <= 10000:
    #         arr.append((i + q + r))
#print(arr[::-1])


for i in range(1, 10001):
    if i not in arr:
        print(i)