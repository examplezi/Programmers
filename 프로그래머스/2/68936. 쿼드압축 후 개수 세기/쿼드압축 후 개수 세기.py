# 0,1 갯수
# from math import sqrt
# def solution(arr):
#     answer = []
#     row = len(arr)
#     col = len(arr[0])
#     n = int(sqrt(row+1))
#     print(row, col,n, (row*col)// 4**(n-1))
#     # 영역에 다른 숫자가 없을 때까지 , 인덱스가 같은 자리끼리
#     while n != 0:
#         print(n)
#         tmp = [ [-1] * col for _ in range(row)] # row, col 변경되어야함
#         print(arr)
#         n -= 1
#         for i in range(row): # 0,2
#             for j in range(col):# 0,2
#                 if i != 0 or i != row // 2:
#                     continue
                    
#                 if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1]:

def solution(arr):
    result=[0,0]
    length=len(arr)
    
    def compression(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start:
                    l=l//2
                    compression(a,b,l)
                    compression(a,b+l,l)
                    compression(a+l,b,l)
                    compression(a+l,b+l,l)
                    return
                
        result[start]+=1
        
    compression(0,0,length)
    
    return (result)
                    
