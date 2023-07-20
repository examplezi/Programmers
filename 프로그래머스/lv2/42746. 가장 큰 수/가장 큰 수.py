# # def solution(numbers):    
# #     s = list(map(str,numbers))
# #     a = sorted(s,key=lambda x: x*3,reverse=1)
# #     return str(int("".join(a)))
# import functools

# def comparator(a,b):
#     #comparator 함수는 두 개의 문자열 a와 b를 비교
#     #이 두 문자열을 합한 두 가지 경우의 수를 비교하여 더 큰 수를 리턴
#     t1 = a+b
#     t2 = b+a
#     print(t1,t2)
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

# def solution(numbers):
#     n = [str(x) for x in numbers]
#     #print(n)
#     n = sorted(n, key=functools.cmp_to_key(comparator), reverse = True) 
#     # 가장 큰 수를 만들기 위해 내림차순 정렬 reverse = True
#     print(n)
#     answer = str(int(''.join(n)))
#    # print(str(''.join(n)))
#     return answer

#from itertools import combinations
def solution(numbers):
    comb = ''
    #for i in numbers:
    numbers = sorted(map(str,numbers), key = lambda x: x*10, reverse = True)
    #print(numbers)
    return str(int(''.join(numbers)))
    #return 
    