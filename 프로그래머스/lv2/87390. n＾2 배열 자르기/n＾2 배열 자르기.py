# #left / n의 값과 left % n의 값을 잘 활용하시면 저 left와 right 사이의 값들을 잘 유추하실 수 있읍니
# def solution(n, left, right):
#     print(left / n, left % n)
#     # answer = [] * 0 for _ in range(n)
#     # print(answer)
# #     answer = [] #길이 n * n 
# #     for i in range(1,n+1): # 1행 처리 
# #         answer.append(i)
    
# #     print(answer)
# #     for i in range(2,n+1):
# #         arr = []
# #         for j in range(1,n+1):
# #             if i == j:
# #                 arr.append(j)
# #                 print(i,j)
        
# #         answer.extend(arr)
# #         print(answer)
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = max(i//n, i%n) + 1 # x=i//n, y=i%n | x, y 중에 큰 수를 구해 +1을 해서 값으로 넣어줌
        #print(i//n, i%n,v) # 몫, 나머지 
        answer.append(v)
    return answer
