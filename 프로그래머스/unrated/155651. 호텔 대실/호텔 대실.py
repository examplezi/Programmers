# import datetime
# def solution(book_time):
    
#     for slot in book_time:
#         checkout_time = datetime.datetime.strptime(slot[1], "%H:%M") + datetime.timedelta(minutes=10)
#         slot[1] = checkout_time.strftime("%H:%M")
#     room = 1
#     full = []
#     book_time.sort()
#     full.append(book_time[0])
#     book_time.pop(0)
#     for i in range(len(book_time)):
#         if full[0][1] > book_time[i][0]:
#             room += 1
#         else:
#             full.pop(0)

#         full.append(book_time[i])
#         full.sort(key=lambda x: x[1])# full은 퇴실시간 기준 정렬
#         print(full)
#     return room



import datetime
def solution(book_time):
    
    for i in range(len(book_time)):
        [fir,sec] = book_time[i]
        print(fir,sec)
        newFir = int(fir.split(":")[0]) * 60 + int(fir.split(":")[1])
        newSec = int(sec.split(":")[0]) * 60 + int(sec.split(":")[1]) + 10
        book_time[i] = [newFir,newSec]
        
    room = 1
    full = []
    book_time.sort()
    print(book_time)
    full.append(book_time.pop(0)[1]) # 퇴실시간만 
    print(book_time)
    print(full)
    
    for i in range(len(book_time)):
        
        if full[0] > book_time[i][0]: # 쓰고 있는 방의 퇴실시간이 더 크다면 
            room += 1 # 다른 방 내어줌 
        else: # 방이 비어있다면 
            full.pop(0)
        
        full.append(book_time[i][1]) # 퇴실시간 추가 
        full.sort()# full은 퇴실시간 기준 정렬
        
        
    return room
      