def solution(number, k):
    answer = []

    for i in number:
       
        if not answer: # 비어있을 때 
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)
  