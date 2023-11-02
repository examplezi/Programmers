n = int(input())

target = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

dict = {}
for i in range(len(alphabet)):
    if alphabet[i] not in dict:
        dict[alphabet[i] ] = i+1

arr = []
for i in target:
    if i in alphabet:
        arr.append(dict[i])


total = 0
for i in range(len(arr)):
    total += arr[i] * 31**i


print(total % 1234567891)