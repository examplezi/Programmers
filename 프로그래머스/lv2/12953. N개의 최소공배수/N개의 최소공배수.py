 #import math

# def are_coprime(a, b): # 서로소 
#     return math.gcd(a, b) == 1


# def solution(arr):
#     answer = 1
#     #arr.sort()
#     for i in range(1,len(arr)): # 오름차순 정렬필요? 
#         print(i,arr[i-1],arr[i],answer)
#         if arr[i] % arr[i-1] ==0:
#             answer *= arr[i]
#             #print(answer)
#         elif arr[i] % arr[i-1] != 0 and are_coprime(arr[i], arr[i-1]):
#             answer *= arr[i]
#         else:
#             answer *= (arr[i] / math.gcd(arr[i], arr[i-1]))
#     return int(answer)
    # 앞 요소 % 뒷요소 == 0 이면 뒷요소로 대체 
    # 안나눠 떨어지고 서로소가 1이면 그냥 곱하라
    # 안나눠 떨어지지만 약수가 존재한다면 (요소1)*(요소2 / 약수)
    
def solution(arr):
    from math import gcd                            # 최대공약수를 구하는 gcd() import
    answer = arr[0]                                 # answer을 arr[0]으로 초기화

    for num in arr:                                 # 반복문을 처음부터 끝까지 돈다.
        #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
        #2. (#1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
        #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
        answer = answer*num // gcd(answer, num)     

    return answer