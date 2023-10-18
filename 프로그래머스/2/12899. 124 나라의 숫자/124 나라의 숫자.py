# # 중복 permutations
# from itertools import product
# def solution(n):
#     answer = '' # ''.join()
#     # n % 3 == 0 , 4
#     # n % 3 == 1 , 1
#     # n % 3 == 2 , 2
#     arr = list(str(n))
#     num = len(arr)
#     ele = [1,2,4]
    #print(arr,num, "점검")
    
#     if n <= 3 and n % 3 == 0:
#         return '4'
#     elif n <= 3 and n % 3 == 1:
#         return '1'
#     elif n <= 3 and n % 3 == 2:
#         return '2'
        
    
#     while n != 0:
#         #num -= 1
#         #print( n, "왜?")
#         if n % 3 == 0:
#             answer = '4' + answer
            
#         elif n % 3 == 1: # 몫 + 나머지
#             n = n //3
#             answer = '1' + answer
#         else: # 몫 + 나머지
#             n = n //3
#             answer = '2' + answer

#     #print(answer,'dfdfdf')
#     return answer
    # n으로 자릿수 조절 1자리 = 3, 2자리 = 9, 3자리 = 27, 4자리, 81
    # count = 0
    # while n != 0:
    #     count += 1
    #     n = 
    # for i in range(n):
    #     for j in range(3*i):
    #         print(i,j)
    # permu = list(product(ele,repeat = 2))
    # print(permu)
    
def solution(n):
    answer = ''
    while n:
        n, na = divmod(n, 3)
        answer = str([4,1,2][na]) + answer
        if na == 0:
            n -= 1
    return answer