def solution(answers):
    answer = [0,0,0]
    arr = []
    guy1 =[1, 2, 3, 4, 5]
    guy2 = [2, 1, 2, 3, 2, 4, 2, 5]
    guy3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        #print(i)
        # 학생별로 분기
        if guy1[i % len(guy1)] == answers[i]:
            answer[0] += 1
        
        if guy2[i % len(guy2)] == answers[i]:
            answer[1] += 1
        
        if guy3[i % len(guy3)] == answers[i]:
            answer[2] += 1
    #print(answer)
    max_score = max(answer)
    for i in range(len(answer)):
        if max_score == answer[i]:
            arr.append(i+1)
    return arr