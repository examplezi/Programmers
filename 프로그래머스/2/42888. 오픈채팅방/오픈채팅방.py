# from collections import deque
# def solution(record):
#     answer = [] # 메시지 
#     filt = deque()
#     q= deque() # 채팅방
    
#     for info in record:
#         filt.append(info.split())
    
#     filt2 = filt.copy()
        
#     while filt:
#         info = filt.popleft()
#         if info[0] == 'Enter' and not any(entry[1] == info[1] for entry in q): 
#             #any로 조건을 검사
#             #단순 제너레이터 생성
#             q.append(info)
#             answer.append(info[2] + "님이 들어왔습니다.")
#             #print(info[2] + "님이 들어왔습니다.")
#             #print(q)
#         elif info[0] == 'Enter': # 재입장
#             # q에서 같은 userid가 있으면 닉네임을 변경해라 replace
#             #answer에서 처음 enter, leave 닉네임 변경
#             answer.append(info[2] + "님이 들어왔습니다.")
#             idx = -1
#             #print("이름 변경해서 재입장")
#             for i in range(len(q)):
#                 if info[1] in q[i][1]:
#                     #i[1].replace(i[1],info[1]) replace는 새로운 문자열 생성
#                     q[i][2] = info[2]
#                     idx = i
                   
#             if idx != -1:
#                 for i in range(len(answer)):
#                     if i == idx:
#                         answer[i] = f"{info[2]}님이 들어왔습니다." # 모양 왜? 
                        
#             for i in range(len(answer)):
#                 if filt2[i][0] == "Leave" and info[1] == filt2[i][1]: #2
#                     answer[i] = f"{info[2]}님이 나갔습니다."
            
#         elif info[0] == 'Leave':
#             for i in list(q): # list로 복사해서 사용 runtime error 방지
#                 if info[1] in i:
#                     #.remove(i) # 제거가 아니라 이름만 바꾸는 걸로 replace
#                     answer.append(i[2] + "님이 나갔습니다.")
#                     #print(i[2] + "님이 나갔습니다.")
#                 break
#         else: # change
#             idx = -1
#             for i in range(len(q)):
#                 if info[1] in q[i][1]: # 1
#                     q[i][2] = info[2]
#                     idx = i
                   
#             if idx != -1: # 1
#                 for i in range(len(answer)):
#                     if i == idx:
#                         answer[i] = f"{info[2]}님이 들어왔습니다." # 모양 왜? 
            
#     return answer
def solution(record):
    answer = []
    id={info.split()[1]:info.split()[2] for info in record if info.split()[0]!="Leave"}
    for info in record:
        if info.split()[0]=="Enter":
            answer.append(id[info.split()[1]]+"님이 들어왔습니다.")
        elif info.split()[0]=="Leave":
            answer.append(id[info.split()[1]]+"님이 나갔습니다.")
    return answer