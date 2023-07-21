# def solution(answers):
#     answer = []
#     arr = []
#     p1 = [1,2,3,4,5]
#     p2 = [2,1,2,3,2,4,2,5]
#     p3 = [3,3,1,1,2,2,4,4,5,5]
#     c1 = 0
#     c2 = 0 
#     c3 = 0
#     if len(p1)< len(answer):
#         p1.extend(answer[len(p1):])
#     if len(p2)< len(answer):
#         p2.extend(answer[len(p2):])
#     if len(p3)< len(answer):
#         p3.extend(answer[len(p3):])

#     for i, j in zip(p1,answers):
#         #print(i,j)
#         if i == j:
#             c1 += 1
#     answer.append(c1)
 
#     for i, j in zip(p2,answers):
     
#         if i == j:
#             c2 += 1
#     answer.append(c2)
#     #print(answer)
#     for i, j in zip(p3,answers):
#         #print(i,j)
#         if i == j:
#             c3 += 1
#     answer.append(c3)
#     print(answer)
#     #answer.sort()
    
#     # for i in range(len(answer)):
#     #     print(i)
#     #     arr.append(i+1)
#     #return max(answer)
#     max_score = max(answer)
    
#     for idx, score in enumerate(answer, 1):
#         if score == max_score:
#             arr.append(idx)
#     print(sorted(arr))
#     return sorted(arr)

def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]  # 각 학생들의 점수를 기록할 리스트

    for idx, ans in enumerate(answers):
        if ans == p1[idx % len(p1)]:
            scores[0] += 1
        if ans == p2[idx % len(p2)]:
            scores[1] += 1
        if ans == p3[idx % len(p3)]:
            scores[2] += 1

    max_score = max(scores)  # 가장 높은 점수
    for idx, score in enumerate(scores, 1):
        if score == max_score:
            answer.append(idx)

    return answer
