# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         start = commands[i][0]
#         stop = commands[i][1]
#         target = commands[i][2]
#         result = array[start-1:stop]
#         result.sort()
#         for j in range(len(result)):
#             if j == target-1:
#                 answer.append(result[j])
#     return answer
# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         start = commands[i][0]
#         stop = commands[i][1]
#         target = commands[i][2]
#         result = array[start-1:stop]
#         result.sort()
#         for j in range(len(result)):
#             if j == target-1:
#                 answer.append(result[j])
#     return answer

def solution(array,commands):
    answer = []

    for i in commands:
        ary = array[i[0]-1 : i[1]] #문제에서 주어진 크기만큼 자르기

        ary.sort() # 오름차순
        answer.append(ary[i[2]-1]) # k번째 값 넣기 

    return answer