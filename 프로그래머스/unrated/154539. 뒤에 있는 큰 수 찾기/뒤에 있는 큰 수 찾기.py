def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    #print(result)
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            result[idx] = numbers[i]
            #print("while", stack, result)

        stack.append(i)
        #print(stack, result)

    return result

