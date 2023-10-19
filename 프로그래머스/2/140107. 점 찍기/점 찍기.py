#조합? 범위만 정하고 조합으로 돌리면 될거 같은데 
# from math import sqrt
# def solution(k, d):
#     filt = []
#     for i in range(0,d+1,k):
#         for j in range(0,d+1,k):
#             #print(i,j)
#             if sqrt(i**2 + j**2) <= d: 
#                 filt.append((i,j))

#     return len(filt)


from math import sqrt

def solution(k, d):
    answer = 0
    summ = 0

    for y in range(0, d + 1, k):
        x = d ** 2 - y ** 2
        cnt = sqrt(x) // k + 1
        summ += cnt

    return summ

    