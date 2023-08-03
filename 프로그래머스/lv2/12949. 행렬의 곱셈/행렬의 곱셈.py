import numpy as np

def solution(arr1, arr2):
#     answer = [[]]
#     d = [[1 for _ in range(len(arr2))] for _ in range(len(arr1))]
#     print(d)
#     #a = [[1 for _ in range(len(arr2))] for _ in range(len(arr1))]
#     #result = [a * b for a, b in zip(arr1, arr2)]
#     #print(result)
    
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             #print(i,j)
#             print(arr1[i][j], arr2[i][j])#, arr2[j][i]
#     #     for j in range(len(arr2)):
#     #         print(arr1[i][])

    mat1 = np.array(arr1)
    mat2 = np.array(arr2)
    #print(mat1)
    
    result = np.dot(mat1, mat2)

    return result.tolist()
