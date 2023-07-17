# def solution(nums):
#     answer = 0
#     length = len(nums) // 2
#     temp = list(set(nums))
    
#     print(temp)
    
#     for value in temp :
#         if(answer < length):
#             answer +=1
#             print(answer, length)
#     return answer

# set로 중복값 제거해서 그걸 배열 길이의 반까지 돌게해서 +1 씩 

def solution(nums):
    answer = 0
    length = len(nums) //2
    kind = list(set(nums))
    print(kind)
    
    for i in kind:
        if(answer < length):
            answer += 1
    return answer