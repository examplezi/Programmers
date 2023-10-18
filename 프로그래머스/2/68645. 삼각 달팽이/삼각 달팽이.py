# # 반복 느낌? -> 반복되는걸 재귀함수로 표현
# # 맨 마지막 n개의 수는 n부터 차례대로
# # 1. 리스트에 n 만큼의 이중 리스트 만들기
# # 2. 각 리스트 첫번째 자리에 순서대로 값 넣기
# # 3. 마지막 리스트라면 연이은 숫자 넣기
# # 4. 각 리스트의 끝 값 넣기 -> 다시 리스트의 빈 첫번째 인덱스에 순서대로 넣기

# # 아니면 dp로 아래 -> 위로? 
# def solution(n):
#     answer = []
#     for i in range(1,n+1): # 리스트 만들기
#         answer.append([0] * i)
#     answer[0][0] =1
#     answer[n-1][0] = n
#     idx = 0
# #     def dfs(x,y,idx):
# #         start = answer[x+1][y] # 0, 2, 3, 4
# #         for i in range(x, len(answer)):# 첫값 채우기
# #             for j in range(len(answer[i])):
# #                 if answer[i][j] == 0 and answer[i-1][j] and answer[i-1][j] != 0:
# #                     #answer[i][0] = j+1 
# #                     answer[i][j] = answer[i-1][j] + 1

# #         for i in range(n): # 마지막 리스트 값 채우기
# #             answer[-1][i] = n + i


# #         for i in range(n-2,0,-1): # 리스트의 마지막값들 채우기
# #             answer[i][-1] = answer[i+1][-1] + 1
# #         print(answer)
# #         dfs(x+1,y,idx)
    
# #     dfs(0,0,0)
    
#     # def dfs(x, y):
#     #     if x == n - 1:  # 재귀 종료 조건
#     #         return
#     #     print(answer)
#     #     for i in range(x+1, len(answer)):
#     #         for j in range(len(answer[i])):
#     #             print(i,j,answer[i][j] )
#                 # if answer[i][j] == 0 and answer[i - 1][j] and answer[i - 1][j] != 0:
#                 #     answer[i][j] = answer[i - 1][j] + 1

# #         for i in range(n):
# #             answer[-1][i] = n + i

# #         for i in range(n - 2, 0, -1):
# #             answer[i][-1] = answer[i + 1][-1] + 1

#        # dfs(x + 1, y)


#     for i in range(n-1,0,-1):
#         for j in range(len(answer[i])):
#             print(i,j)
#             if i == n -1 and answer[i][j] == 0 :
#                 answer[i][j] = answer[i][j-1] + 1
#             else:
#                 answer[i][j] = answer[i+1][j] -1
#         print(answer)
    
    
    #print(answer)
    #return answer
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] # 삼각형 구조 만들기
 
    x, y = -1, 0 # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1
 
    for i in range(n): # 방향
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
 
    return sum(answer, [])
    