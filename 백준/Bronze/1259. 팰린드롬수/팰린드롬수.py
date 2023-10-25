
arr = []
while True:
    a = input()
    if a == '0':
        break
    else:
        arr.append(a)

#print(arr)

for i in arr:
    #print(i,i[::-1])
    if i == i[::-1]:
        print("yes")
    else:
        print("no")