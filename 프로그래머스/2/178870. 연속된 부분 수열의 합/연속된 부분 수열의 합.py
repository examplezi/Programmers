# def solution(sequence, k):
#     answer = []
#     for i in range(len(sequence)):
#         total = 0
#         for j in range(i, len(sequence)):
#             if i != j:

#                 total = sum(sequence[i:j+1])
#             else: # 같다면
#                 total = sequence[i]
#             if total == k:
#                 answer.append([i,j])
    
#     length = [j-i for [i,j] in answer]
#     min_value = 1001
#     for i in range(len(length)):
#         if length[i] < min_value:
#             min_value = length[i]
#             idx = i
#     #print(min_value, idx)
#     return answer[idx]
        
    
def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):

        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    return res[0][:2]