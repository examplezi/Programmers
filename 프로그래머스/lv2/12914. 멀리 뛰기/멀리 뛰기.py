# def solution(n):
#     answer = 0
#     max = n
    # return answer % 1234567
    
    
# from itertools import product

# def solution(n):
#     answer = 0
#     #1과 2로 만들 수 있는 길이가 n인 모든 조합을 출력하는 함수
#     # 리스트 요소 값의 합이 n -> if sum(arr[i]) == n 
#     #
#     for i in range(1, n +1):
#         elements = [1, 2]
#         combinations = list(product(elements, repeat=i))
#         for tpl in combinations:
#             if sum(tpl) == n:
#                 answer += 1
              
#     return answer
                
def solution(n):
    if n<3:
        return n
    d=[0]*(n+1)
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]%1234567    
