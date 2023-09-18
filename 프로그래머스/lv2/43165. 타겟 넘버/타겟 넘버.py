def solution(numbers, target):
    answer = 0
    
    def dfs(level,current_sum ,answer): 
        if level >= len(numbers):
            if current_sum == target:
                answer += 1
            return answer

        
        answer = dfs(level+1, current_sum + numbers[level], answer)
        answer = dfs(level+1, current_sum - numbers[level], answer)
        return answer
    
    return dfs(0,0,0)