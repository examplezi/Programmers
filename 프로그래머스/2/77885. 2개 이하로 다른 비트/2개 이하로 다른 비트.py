# def solution(numbers):
#     answer = []
#     for i in numbers:
#         a = format(i,'b')
#         print(a, a.count('1'))
#         # i보다 큰 수를 2진수로 만들면서 비교해서 1의 개수가 2개 이하면 answer 에 넣어라 
#         for j in range(i+1,12):# (10**15) + 1
#             #print(i,j)
#             b = format(j,'b')
#             #print(int(a) - int(b), "2  진수끼리 뺄셈")
#             print(i,j, a,b,int(a)^int(b),i^j, "XOR")
#             # if a.count('1') - b.count('1') <= 2:
#             #     answer.append(j)
#             #     break
#         print(answer)
#     return answer

# from collections import Counter
# def solution(numbers):
#     answer = []
#     binary = []    
#     for i in numbers:
#         for j in range(i+1, (10**15)+1): # 100,001 
#             #print(i,bin(i),bin(j),j, "xor", i^j,bin(i^j), Counter(bin(i^j)))
#             #print(i,j)
#             counter = Counter(bin(i^j))
#             #print(counter)
#             if counter['1'] <= 2:
#                 answer.append(int(j))
#                 break
#     return answer

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer