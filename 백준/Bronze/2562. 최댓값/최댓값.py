arr = []
for i in range(9):
	arr.append(int(input()))


#print(arr)
max_v = 0
for i in arr:
    if i > max_v:
        max_v = i
print(max_v)

for i in range(len(arr)):
    if arr[i] == max_v:
        print(i+1)
        break