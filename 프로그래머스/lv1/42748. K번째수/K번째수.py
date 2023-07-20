def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]
        stop = commands[i][1]
        target = commands[i][2]
        print(target)
        result = array[commands[i][0]-1:commands[i][1]]
        result.sort()
        print(result)
        for j in range(len(result)):
            print(j, target-1)
            if j == target-1:
                answer.append(result[j])
                print(answer)

    return answer
            
            
        #print(result)