# n을 k 진수로 바꿈
# 진수에서 0을 포함하지 않는 연속된 숫자 or 단일 숫자 >= 2를 찾음(P) 
# 연속된 숫자가 소수이면 카운트 +1 
def solution(n, k):
    
#     def prime_number(n):
#         if n < 2:
#             return False
#         for i in range(2, n):
#             if i % n == 0:
#                 return False
                
#         return True
    def prime_number(number):
        if number==1:
            return False
        for i in range(2, int(number**(0.5))+1):
            if number%i==0:
                return False
        return True
                  
    answer = []
            
    prime = ''
    num = []
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    k_num =  list(rev_base[::-1] )
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

    for i in range(len(k_num)):
        if k_num[i] != '0':
            prime += k_num[i]
        else: #0이라면
            prime += ','
    num.append(prime.split(','))
    filtered_list = [int(item) for item in num[0] if item.strip()]

    for i in filtered_list:
        if prime_number(i):
            answer.append(i)

    return len(answer)



        
        