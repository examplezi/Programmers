def solution(numbers):
    # 1. numbers의 모든 요소를 더한다. -> sum
    # 2. sum을 numbers의 길이로 나눈다.
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)