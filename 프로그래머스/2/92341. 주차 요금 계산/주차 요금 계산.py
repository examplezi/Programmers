# 누적 시간 <= 180: 5000원
# 그게 아니라면
# out이 없다면 23: 59 -
# 시간은 다 분으로 통일 h * 60 
# fees = [기본시간, 기본 요금, 단위 시간, 단위요금]
# 차 번호로 오름정렬
from collections import deque
from math import ceil
def solution(fees, records):
    answer = []
    info = []
    for i in records:
        filt = i.split()
        info.append(filt)
    info.sort(key = lambda x : x[1])
    info = deque(info)
    #print(info)
    # 누적시간 구하기 시간 -> 분 
    # 분(시간) + 분 => 원래 자리에 삽입
    for i in range(len(info)):
        h = int(info[i][0].split(':')[0])
        time = (h * 60) +  int(info[i][0].split(':')[1])

        info[i][0] = time
    #print(info)
    total_time = 0
    calcu = {}
    # 시간 계산해서 주차요금 정산, in- out 짝 지어져 있음
    while info:
        total_time = 0
        time, plate, action = info.popleft()
        if not info and action == "IN":
            total_time = 1439 - time
            if not plate in calcu:
                calcu[plate] = total_time
            else:
                calcu[plate] += total_time
        if not info: # 탈출조건 다른걸로 해야함 
            break
        #if plate == info[0][1] and action == "IN":
        if plate == info[0][1] and action == "IN":
            total_time += info[0][0] - time
            if not plate in calcu:
                calcu[plate] = total_time
            else:
                calcu[plate] += total_time
        elif action == "OUT":
            continue
            
        else: # 출차기록 x, 23:59 -> 1439
            total_time = 1439 - time
            if not plate in calcu:
                calcu[plate] = total_time
            else:
                calcu[plate] += total_time
    #print(calcu)

    # fees[0] >= calcu[plate] -> answer.append(fees[1])
    # 초과면,  ceil((calcu[plate] - fees[0]) / fees[2]) * fees[3] + fees[0]
    for k,v in calcu.items():
        #print(k,v)
        if v <= fees[0]:
            answer.append(fees[1])
        else:
            #print(ceil((v - fees[0]) / fees[2]), fees[3], fees[1])
            answer.append((ceil((v - fees[0]) / fees[2]) * fees[3]) + fees[1])
    #print(answer)
    return answer
