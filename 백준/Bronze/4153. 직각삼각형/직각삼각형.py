arr = []
while True:
    a,b,c = map(int, input().split())
    #print(a,b,c)
    if a == b == c == 0:
        break
    else:
        array2 = [a,b,c]
        array2= sorted(array2)
        arr.append(array2)
for i in range(len(arr)):
    if arr[i][0]**2 + arr[i][1]**2 == arr[i][2]**2:
        print("right")
    else:
        print("wrong")