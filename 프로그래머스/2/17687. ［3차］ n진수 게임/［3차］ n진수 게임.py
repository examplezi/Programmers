#t는 말해야 하는 갯수
# t = len(answer)
# 0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F
# def solution(n, t, m, p):
#     answer = ''
#     num = '0'
    # 진법을 구하는 식 
    # 퇴출 조건 t = len(answer)
    # for i in range(1,t*m): # 1~ 31
    #     #print(i, n % i)
    #     if i < n: # 1~ 15
    #         if i >= 10: # 10~15
    #             i = chr(ord('A')+ i- 10)
    #             num += str(i)
    #         # else:
    #         #     num += str(i)
    #     elif i >= n: # 16~31
    #         num += str(i%n)
    #     print(num)
    #     # while i > 0:
    #     #     num += str(n %i)
    
    #n = 'n'
#     for i in range(1,t*m): # 1-7
#         nums = format(i,f'{n}')
#         print(nums)
#         num += nums
#     print(num)

def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t):
        result = ""
        while num > 0:
            num, remainder = divmod(num, n)
            result += notation[remainder]

        answer += result[::-1]


    return answer[p-1::m][:t]
        