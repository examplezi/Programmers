def solution(numbers):
    sum = 0
    numbers.sort()
    print(numbers)
    for i in range(10):
        if i not in numbers:
            #print(i)
            sum += i
    return sum