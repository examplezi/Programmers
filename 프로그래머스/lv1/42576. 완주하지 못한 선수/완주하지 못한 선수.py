# import collections
# def solution(participant, completion):
#     # 1. participant의 Counter를 구한다
#     # 2. completion의 Counter를 구한다
#     # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(collections.Counter(participant),collections.Counter(completion))
#     print(answer)
#     # 4. counter의 key값을 반환한다
#     return list(answer.keys())[0]

def solution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]