# arr1[0][0] + arr2[0][0]
# arr1[0][1] + arr2[0][1]
# arr1[1][0] + arr2[1][0]
# arr1[1][1] + arr2[1][1]

def solution(arr1, arr2):
    row = len(arr1) #2
    col = len(arr1[0]) #2
    answer = [[0] * col for _ in range(row)]
    #print(row, col, answer)
    
    for i in range(row):
        for j in range(col):
            #print(i,j)
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer