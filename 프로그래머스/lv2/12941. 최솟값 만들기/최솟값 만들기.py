def solution(A,B):
    answer = 0
    A.sort()
    B = sorted(B,reverse = True)
    for i in range(len(A)):
        # for j in range(len(B)):
        #     if i == j:
                answer += A[i] * B[i]
            
    return answer