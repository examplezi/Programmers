# 끝까지 진행해서 타겟 넘버랑 같을 때, 
def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers): # 끝까지 닿았을 때 
        if sum(numbers) == target:# 끝까지 닿은 것 중에서 타겟이랑 같으면 
            return 1
        else: return 0
    else: #depth가 0,1,2,3 일 때 
        #answer = 0
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        #print(answer)
        return answer
     