def solution(numbers, target):
    """
    pick or not pick 으로 접근하는 문제입니다.
    여기서 pick은 양수를 더하고, not pick은 음수로 더하는 경우입니다.
    시간복잡도는 2^n으로, 최악의 경우 2^20이므로, 완전탐색(DFS)로 탐색이 가능합니다.
    그래프로 표기하는 것이 기억나지 않는다면, 강의 영상을 다시 찾아봐 주세요.
    """
    def dfs(level, current_sum, answer):
        # 탈출 조건 (레벨이 numbers의 길이와 같거나 클 경우)
        if level == len(numbers):
            if current_sum == target:
                answer += 1
            #print(answer)
            return answer

        # 현재 숫자 = numbers[level] 를 더하거나, 빼는 경우 -> 재귀 호출 해야함.
        # 재귀 호출할 때, level은 모두 증가해야 함.
        # answer 누적이라 파라미터
        answer = dfs(level + 1, current_sum + numbers[level], answer)
        answer = dfs(level + 1, current_sum - numbers[level], answer)
        return answer

    return dfs(0, 0, 0) # 스타트 
