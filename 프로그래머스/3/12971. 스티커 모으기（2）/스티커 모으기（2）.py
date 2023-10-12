# 최대값
# 인접해 있는것 같이 x 
# i로 접근 순서대로 -> 남은거에서 최대값 -> 남은거에서 최대값 x 
# dfs 반복 뽑기
# dp 문제 pick or not pick 
# from collections import deque
# def solution(sticker):
#     answer = 0
    
#     sticker = deque(sticker)
    
#     for i in range(len(sticker)):
#         start = sticker[i]
#         next_n = sticker[i+1] 
#         prev = sticker[i-1]
#         max_value += start
#         if i == 0:
#             dp = sticker[i] + max(sticker)
            
    
#         sticker.remove(start)
#         sticker.remove(next_n)
#         sticker.remove(prev)
#         sticker.remove()
#         print(sticker)
    
  
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2 = [0] * len(sticker)
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(max(dp1), max(dp2))